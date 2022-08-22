import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime
import csv

class G1Spider(scrapy.Spider):
    name = 'g1_spider'

    def start_requests(self):
        urls = ['https://g1.globo.com']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        titles = response.css('*.gui-color-primary::text').extract()
        links = response.css('*.gui-color-primary::attr(href)').extract()
        current_date = str(datetime.now().date())
        n_date = datetime.strptime(current_date, "%Y-%m-%d").strftime("%d-%m-%Y")
        n_date_bar = n_date.replace('-', '/')
        with open(f'./csvs/G1_{n_date}.csv', 'w') as file:
            header = ['news', 'link', 'date']
            csv_writer = csv.DictWriter(file, fieldnames=header)
            csv_writer.writeheader()
            for title, link in zip(titles,links):
                if title.find('%'):
                    title = title.replace('%', ' porcento')
                csv_writer.writerow({'news':f'{title}', 'link':f'{link}', 'date':f'{n_date_bar}'})

process = CrawlerProcess()
process.crawl(G1Spider)
process.start()