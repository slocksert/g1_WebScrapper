# G1 WEBSCRAPER

## What it does?
- A headline finder from the G1 site, basically takes as data the headline, link, date and respective image.

## How it was made?
- The software utilizes SQLAlchemy for database interaction and FastAPI for web framework. It scrapes news data from G1 website, stores it in a CSV file, and then checks if each news already exists in the database before sending the new data to the database.

## How to use?
- Clone this repository:
```bash
$ git clone https://github.com/slocksert/g1_WebScrapper.git
```

- Activate Poetry env and install dependencies

- To start the MySQL database using a docker-compose file:
    - Create a *.env* file with these variables:
        - MYSQL_HOST
        - MYSQL_ROOT_PASSWORD
        - MYSQL_DATABASE
        - MYSQL_PORT

- Start the MySQL compose:
```bash
$ docker compose up
```

- Start the WebScraper:
```bash
$ python3 app/main.py
```

### To visualize the database install a database admnistration tool, example right below.
<br>
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/image_2022-11-10_220452957.png?raw=true"></h1>