FROM python:3.10.8

WORKDIR /app

COPY . . 

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

RUN apt-get update -y && apt-get install -y python3-pymysql

CMD [ "./entrypoint.sh" ]
