# -*- coding: utf-8 -*-
import re

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PeoplePipeline(object):
    def process_item(self, item, spider):
        item['text'] = self.process_content(item['text'])
        item['author'] = self.process_author(item['author'])
        item['title'] = self.process_title(item["title"])
        print(item)
        # return item


    def process_content(self,text):
        text = [re.sub(r'\n|\t|\u3000\u3000|\xa0|\u3000','',i)for i in text]
        text = [i for i in text if len(i)>0]
        text = ''.join(text) # 将列表里的字符串拼接成一个完整的字符串
        # >>>>>用法：list = ["life","is","short",",","i","use","python"]
        # >>>>> list_str = ''.join(list)
        return text

    def process_author(self,author):
        author = re.sub(r'\xa0','',author)
        return author



    def process_title(self,title):
        title =re.sub(r'\xa0','',title)
        return title
