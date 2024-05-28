import sqlalchemy
import pandas as pd 
import os
import logging
from webscraper import WebScraper

class FileHandler():
    def __init__(self, webscraper:WebScraper) -> None:
        self.host = webscraper.host
        self.database = webscraper.database
        self.password = webscraper.password
        self.port = webscraper.port  
        self.date = webscraper.date
        self.csv_file_path = webscraper.csv_file_path
        self.engine = webscraper.engine

    def connect(self) -> None:
        try:
            self.con = self.engine.connect()
        except Exception as e:
            logging.error("ERROR while conecting to database: ", e)
            quit()

    def send_file(self) -> None:
        try:
            if not os.path.exists(self.csv_file_path):
                logging.error(f'The file G1_{self.date}.csv does not exist!')
                return
            
            df = pd.read_csv(self.csv_file_path)
            df.to_sql(name=self.database, con=self.engine, if_exists="append", index=False, dtype={
                "index": sqlalchemy.Integer(),
                "news": sqlalchemy.Text(),
                "link": sqlalchemy.Text(),
                "date": sqlalchemy.Date(),
                "image": sqlalchemy.Text()
            })
            logging.info(f'The file G1_{self.date}.csv has been sent SUCCESSFULLY to the DataBase!')
        except Exception as e: 
            logging.error("ERROR while sending file to database: ", exc_info=True)