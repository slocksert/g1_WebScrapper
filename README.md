# G1 CRAWLER

## What it does?
- A headline finder from the G1 site, basically takes as data the headline, the link to the headline, and the date.

## How it was made?
- Using the library 'scrapy', which specializes in crawlers, I used CSS selectors to filter out exactly what I wanted from the site, then saved the data in a csv file and sent it to a database.

## How to use?
- Clone this repository:
```bash
$ git clone https://github.com/slocksert/g1_crawler.git
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

- Start the WebScrapper:
```bash
$ python3 app/main.py
```

### To visualize the database install a database admnistration tool, example right below.
<br>
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/image_2022-11-10_220452957.png?raw=true"></h1>