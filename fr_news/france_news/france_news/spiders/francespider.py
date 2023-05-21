'''Module for parsing the web-site'''
import scrapy


class FrancespiderSpider(scrapy.Spider):
    '''class of the spider'''

    name = "francespider"

    urls_dct = {'2022-04-15': 'https://www.lemonde.fr/en/archives-du-monde/15-04-2022/',
                '2022-07-14': 'https://www.lemonde.fr/en/archives-du-monde/14-07-2022/',
                '2022-09-08': 'https://www.lemonde.fr/en/archives-du-monde/08-09-2022/',
                '2022-09-11': 'https://www.lemonde.fr/en/archives-du-monde/11-09-2022/',
                '2022-11-11': 'https://www.lemonde.fr/en/archives-du-monde/11-11-2022/',
                '2023-01-16': 'https://www.lemonde.fr/en/archives-du-monde/16-01-2023/',
                '2023-05-18': "https://www.lemonde.fr/en/archives-du-monde/18-05-2023/"}


    def start_requests(self):

        for url in self.urls_dct.keys():
            yield scrapy.Request(url=self.urls_dct[url],
                                 callback=self.parse,
                                 meta={'date': url})


    def parse(self, response):
        '''Function for response from the website'''
        for article in response.css('h3.teaser__title::text').getall():
            yield {
                "title": article.strip(),
                'date': response.meta['date']
            }
