# G1 CRAWLER

## What it does?
- A headline finder from the G1 site, basically takes as data the headline, the link to the headline, and the date.

## How it was made?
- Using the library 'scrapy', which specializes in crawlers, I used CSS selectors to filter out exactly what I wanted from the site, then saved the data in a csv file and sent it to a database.

## How to use?
- Clone this repository:
```bash
$ git clone https://github.com/slocksert/g1_crawler
```
- Get the docker image:
```bash
$ docker pull slocksert/g1crawler
```
- To start the MySQL database type this:
```bash
$ docker compose -f "docker/docker-compose2.yaml" up -d --build
```

- Download DBeaver to visualiaze the database.

    - Arch Linux, Manjaro and etc:
    ```bash
    $ sudo pacman -S dbeaver
    ``` 
    ```bash
    $ yay -S dbeaver-ce
    ```
    - Snap:
    ```bash
    $ sudo snap install dbeaver-ce
    ```

- Start a new conection:
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/dbeaver.jpeg?raw=true"></h1>

- Choose MYSQL.
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/image_2022-11-10_215713354.png?raw=true"></h1>

- In the "password" field type root and click finish.
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/image_2022-11-10_215917309.png?raw=true"></h1>

- To start the Crawler type this:
```bash
$ docker compose -f "docker/docker-compose.yaml" up -d --build
```

- Press F5 in DBeaver to reload it crawler table will appear
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/image_2022-11-10_220316704.png?raw=true"></h1>

- Click in the crawler table:
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/image_2022-11-10_220452957.png?raw=true"></h1>
