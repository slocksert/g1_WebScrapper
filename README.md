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
- Install Docker and Docker Compose on your machine if you haven't already done so (https://docs.docker.com/).
- Navigate into project directory, build images for both services by running command in terminal:
```bash
$ cd g1_crawler/
```
- Get the application docker image:
```bash
$ docker pull slocksert/g1crawler:v3
```
- To start the MySQL database using a docker-compose file:
    - Create a *.env* file with these variables:
        - MYSQL_HOST
        - MYSQL_ROOT_PASSWORD
        - MYSQL_DATABASE
        - MYSQL_PORT

- To create a network between containers:
```bash
$ docker network create api-python
```

- Start the MySQL compose:
```bash
$ docker compose up
```
- Start the crawler docker:
```bash
$ docker compose -f "docker-compose2.yaml" up
```

### To visualize the database install a database admnistration tool, example right below.
<br>
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/image_2022-11-10_220452957.png?raw=true"></h1>