import csv
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from time import sleep
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine as ce
from decouple import config

sys.path.append(os.getcwd())

from src.models import G1Scrapper

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WebScrapper:
    def __init__(self) -> None:
        self.host = config('MYSQL_HOST')
        self.database = config('MYSQL_DATABASE')
        self.password = config('MYSQL_ROOT_PASSWORD')
        self.port = config('MYSQL_PORT') 
        self.url = 'https://g1.globo.com'
        self.date = str(datetime.now().date())
        self.new_date = self.date.replace('-','/')
        self.csv_file_path = os.path.join(os.getcwd(), "app",f'G1_{self.date}.csv')
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.engine = ce(f'mysql+pymysql://root:{self.password}@{self.host}:{self.port}/{self.database}')
        self.Session = sessionmaker(bind=self.engine)
        logging.info("INITIALIZATING WEBSCRAPPER...")

    def scroll(self) -> None:
        SCROLL_PAUSE_TIME = 0.5
        scroll_clicks = 0
        max_scroll_clicks = 0

        while scroll_clicks < max_scroll_clicks:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(SCROLL_PAUSE_TIME)

            try:
                button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "load-more")))
                button.click()
                scroll_clicks += 1
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            except:
                continue 
    
    def get_links(self) -> list[str]:
        link_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.feed-post-link.gui-color-primary.gui-color-hover"))
        )
        links = [link.get_attribute("href") for link in link_elements if link.get_attribute("href").startswith(self.url)]
        return links

    def get_data_from_link(self, link) -> tuple:
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(link)

        try:
            news = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h1.content-head__title"))
            ).text
            
            image = None
            try:
                image = self.driver.find_element(By.CSS_SELECTOR, "img[decoding='async']").get_attribute("src")
            except:
                try:
                    image = self.driver.find_element(By.CSS_SELECTOR, "video").get_attribute("poster")
                except:
                    logging.warning(f"Neither image nor video poster found for {link}")
        except Exception as e:
            logging.error(f"Error getting data from {link}")
            news, image = None, None
        
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        return news, link, image

    def get_data(self) -> list[tuple]:
        links = self.get_links()
        data = [self.get_data_from_link(link) for link in links]
        return data
    
    def check_if_exists(self, news) -> bool:
        try:
            session = self.Session()
            result = session.query(G1Scrapper).filter(G1Scrapper.news == news).first()
            if result:
                logging.info(f"ALREADY ON DB {news}")
            session.close()
            return result is not None
        except Exception as e:
            logging.error("ERROR while checking if news exists in database: ", e)
            return False
    
    def write_csv(self) -> None:
        logging.info("WRITING CSV...")
        data = self.get_data()
        logging.info(f"CSV: {self.csv_file_path}")
        try:
            with open(self.csv_file_path, 'w') as file:
                header = ['news', 'link', 'date', 'image']
                csv_writer = csv.DictWriter(file, fieldnames=header)
                csv_writer.writeheader()
                for news, link, image in data:
                    if news and link and image:
                        if self.check_if_exists(news):
                            continue
                        csv_writer.writerow({'news': news, 'link': link, 'date': self.new_date, 'image': image})
                        logging.info(f"ADDED {news}")
            logging.info("CSV File created successfully")
        except Exception as e:
            logging.error(f"Error: {e}")
        
    def delete_csv(self) -> None:
        try:
            os.remove(self.csv_file_path)
        except FileNotFoundError:
            logging.error("CSV File not found")
