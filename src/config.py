from decouple import config

host = config('MYSQL_HOST')
database = config('MYSQL_DATABASE')
password = config('MYSQL_ROOT_PASSWORD')
port = config('MYSQL_PORT')
fastapi_port = int(config('FASTAPI_PORT'))