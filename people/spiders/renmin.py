# -*- coding: utf-8 -*-
import scrapy
from people.items import PeopleItem

class RenminSpider(scrapy.Spider):
    name = 'renmin'
    allowed_domains = ['opinion.people.com.cn']
    start_urls = ['http://opinion.people.com.cn/GB/8213/49160/49219/']

    def parse(self, response):
        src = response.xpath('//td[@class="t10l14bl"]//a/@href').extract()[1:]
        for i in src:
            detail_url =  'http://opinion.people.com.cn{}'.format(i)
            yield scrapy.Request(
                detail_url,
                callback=self.parse_detail,
            )

        next_url = "http://opinion.people.com.cn/GB/8213/49160/49219/" + response.xpath('//td[@class="t10l14bl"]//td[@align="right"]/a[last()]/@href').extract_first()
        if next_url != 'http://opinion.people.com.cn/GB/8213/49160/49219/index7.html':
            yield scrapy.Request(
                next_url,
                callback=self.parse,
            )


    def parse_detail(self,response):
        item = PeopleItem()
        item['title'] = response.xpath('//div[@class="clearfix w1000_320 text_title"]/h1/text()').extract_first()
        # content['date'] = response.xpath('//div[@class="box01"]/div/text()').extarct_first()
        item['author'] = response.xpath('//div[@class="clearfix w1000_320 text_title"]/p/text()').extract_first()
        item['text'] = response.xpath('//div[@id="rwb_zw"]/p/text()').extract()

        yield item
