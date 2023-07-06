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
        titles = response.css('*.gui-color-primary.gui-color-hover > div > a > h2::text').extract()
        links = response.css('*.gui-color-primary.gui-color-hover > div > a::attr(href)').extract()
        current_date = str(datetime.utcnow().date())
        new_date = current_date.replace('-', '/')
        with open(f'./csvs/G1_{current_date}.csv', 'w') as file:
            header = ['news', 'link', 'date']
            csv_writer = csv.DictWriter(file, fieldnames=header)
            csv_writer.writeheader()
            for title, link in zip(titles,links):
                csv_writer.writerow({'news':f'{title}', 'link':f'{link}', 'date':f'{new_date}'})

crawler = CrawlerProcess()
crawler.crawl(G1Spider)
crawler.start()