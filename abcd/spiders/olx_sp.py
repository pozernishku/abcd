# -*- coding: utf-8 -*-
import scrapy


class OlxSpSpider(scrapy.Spider):
    name = 'olx_sp'
    allowed_domains = ['www.olx.ua']
    start_urls = ['https://www.olx.ua/']

    def parse(self, response):
        pass
