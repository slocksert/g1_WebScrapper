from datetime import datetime
from sqlalchemy import create_engine as ce
import pandas as pd 
import dotenv
import os

class Con():
    def __init__(self) -> None:
        dotenv.load_dotenv()
        self.host = os.getenv('MYSQL_HOST')
        self.database = os.getenv('MYSQL_DATABASE')
        self.password = os.getenv('MYSQL_ROOT_PASSWORD')
        self.port = os.getenv('MYSQL_PORT')

    def connect(self):
        self.engine = ce(f'mysql+pymysql://root:{self.password}@{self.host}:{self.port}/{self.database}')
        self.con = self.engine.connect()
        
    def create(self):
        self.con.execute('CREATE DATABASE IF NOT EXISTS dbroot')

    def send_file(self):
        current_date = str(datetime.utcnow().date())
        df = pd.read_csv(f'./csvs/G1_{current_date}.csv')
        df.to_sql(name='crawler', con=self.engine, if_exists='replace', index=False)
        print(f'The file G1_{current_date}.csv has been sent to the DataBase!')

database = Con()
database.connect()
database.create()
database.send_file()


