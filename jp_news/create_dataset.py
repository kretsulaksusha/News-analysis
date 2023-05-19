"""
modul for creating dateset from scrapy crawl json file
"""

import json
import re
import datetime


def creating_datebase():
    """
    create datebese json file from json spiders file
    """
    with open("news.json", "r", encoding='utf-8') as file:
        data = json.load(file)['htmlContent']
        print(data)

if __name__ == '__main__':
    creating_datebase()
