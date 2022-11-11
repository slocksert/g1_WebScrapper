# G1 CRAWLER

## O que faz?
- Um buscador de manchetes do site G1, basicamente pega como dados a manchete, o link para a manchete e a data.

## Como foi feito?
- Utilizando a biblioteca 'scrapy', a qual se especializa em crawlers utilizei seletores CSS para conseguir filtrar o que queria exatamente do site, apos isso, salvo esses dados em um arquivo csv e os mando para um banco de dados.

## Como Usar ?
- Clone este repositorio em sua maquina:
```bash
$ git clone https://github.com/slocksert/g1_crawler
```
- Baixe a imagem docker que esta no DockerHub com este comando:
```bash
$ docker pull slocksert/g1crawler
```
- Execute este comando para iniciar o banco de dados:
```bash
$ docker compose -f "docker/docker-compose2.yaml" up -d --build
```

- Baixe o Dbeaver para poder visualizar o banco de dados.

    - Arch Linux, Manjaro e derivados:
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

- Inicie uma nova conexao:
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/dbeaver.jpeg?raw=true"></h1>

- Escolha MYSQL
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/image_2022-11-10_215713354.png?raw=true"></h1>

- No campo "password" coloque root e avance
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/image_2022-11-10_215917309.png?raw=true"></h1>

- Execute este comando para iniciar o Crawler:
```bash
$ docker compose -f "docker/docker-compose.yaml" up -d --build
```

- Aperte F5 no DBeaver e ira aparecer a tabela crawler
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/image_2022-11-10_220316704.png?raw=true"></h1>

- Ao acessar a tabela crawler:
<h1 align="center"><img src="https://github.com/slocksert/arranger_imgs/blob/main/image_2022-11-10_220452957.png?raw=true"></h1>
