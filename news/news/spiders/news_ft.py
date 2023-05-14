import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    urls_dct = {'28.02.2022': 'https://web.archive.org/web/20220227233905/https://www.ft.com/world',
                '09.03.2022': 'https://web.archive.org/web/20220306115846/https://www.ft.com/world',
                '15.04.2022': 'https://web.archive.org/web/20220415182232/https://www.ft.com/world',
                '14.07.2022': 'https://web.archive.org/web/20220714002245/https://www.ft.com/world',
                '08.09.2022': 'https://web.archive.org/web/20220908201457/https://www.ft.com/world',
                '11.09.2022': 'https://web.archive.org/web/20220911060914/https://www.ft.com/world',
                '11.11.2022': 'https://web.archive.org/web/20221111200310/https://www.ft.com/world',
                '16.01.2023': 'https://web.archive.org/web/20230111162834/https://www.ft.com/world',
                '14.05.2023': "https://www.ft.com/world"}
    # urls = ["https://www.ft.com/world", "https://web.archive.org/web/20220227233905/https://www.ft.com/world"]

    def start_requests(self):
        for url in self.urls_dct.keys():
            # for i in range(1, 3):
                # new_url = self.urls_dct[url] + f"?page={i}"
            yield scrapy.Request(url=self.urls_dct[url], callback=self.parse, meta={'date': url})


    def parse(self, response):
        for article in response.css("a.js-teaser-heading-link::text").getall():
            yield {
                "Type": article.strip(),
                # 'URL': response.url,
                'Date': response.meta['date']
            }
        # for i in range(2, 4):
        #     next_page = response.urljoin(f"?page={i}")
        #     if next_page is not None:
        #         yield response.follow(next_page, callback=self.parse)

# class NewsSpider(scrapy.Spider):
#     name = 'news'
#     urls = ['https://web.archive.org/web/20220227233905/https://www.ft.com/world', 'https://www.ft.com/world']

#     def start_requests(self):
#         for url in self.urls:
#             yield scrapy.Request(url=url, callback=self.parse)