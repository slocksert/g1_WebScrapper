import os
import dotenv

dotenv.load_dotenv()
database = os.getenv('MYSQL_DATABASE')
password = os.getenv('MYSQL_ROOT_PASSWORD')
port = os.getenv('MYSQL_PORT')