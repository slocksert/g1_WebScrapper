from datetime import datetime
from sqlalchemy import create_engine as ce
import pandas as pd 
import dotenv
import os

class Con():
    def __init__(self) -> None:
        dotenv.load_dotenv()
        self.host = os.getenv('MYSQL_HOST')
        self.user = os.getenv('MYSQL_USER')
        self.database = os.getenv('MYSQL_DATABASE')
        self.password = os.getenv('MYSQL_PASSWORD')
        self.port = os.getenv('MYSQL_PORT')

    def connect(self):
        engine = ce(f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}')
        self.con = engine.connect()
        
    def send_file(self):
        #current date
        current_date = str(datetime.now().date())
        n_date = datetime.strptime(current_date, "%Y-%m-%d").strftime("%d-%m-%Y")
        df = pd.read_csv(f'./csvs/G1_{n_date}.csv')
        for key, value in df.iterrows():
            news = value[0]
            link = value[1]
            dates = value[2]
            self.con.execute(f'INSERT INTO dbroot.crawler (news, link, date) VALUES("{news}", "{link}", "{dates}")')

p = Con()
p.connect()
p.send_file()


