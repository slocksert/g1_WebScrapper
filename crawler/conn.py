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
        self.engine = ce(f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}')
        self.con = self.engine.connect()
        
    def create(self):
        self.con.execute('CREATE DATABASE IF NOT EXISTS dbroot')

    def send_file(self):
        #current date
        current_date = str(datetime.now().date())
        n_date = datetime.strptime(current_date, "%Y-%m-%d").strftime("%d-%m-%Y")
        df = pd.read_csv(f'./csvs/G1_{n_date}.csv')
        df.to_sql(name='crawler', con=self.engine, if_exists='append', index=False)

p = Con()
p.connect()
p.create()
p.send_file()


