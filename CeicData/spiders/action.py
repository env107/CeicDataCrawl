import scrapy
from CeicData.items import CeicdataItem
import sys
import time

class action(scrapy.Spider):

    name = "CeicData"
    allowed_domain = ['http://news.ceic.ac.cn']
    start_urls = ['http://news.ceic.ac.cn/index.html']

    def parse(self , response):
        self.show_time("开始解析数据工作")
        #爬取每一行地震内容
        rawData = response.xpath("//div[@class='news-content']/table//tr[position()>1]")
        rawline = 0
        dataItem = CeicdataItem()
        
        #获取每一行内容
        for raw in rawData:
            rawline = rawline+1
            info = raw.xpath(".//td//text()").extract()
            dataItem['level'] = info[0]
            dataItem['time'] = info[1]
            dataItem['lat'] = info[2]
            dataItem['lon'] = info[3]
            dataItem['deep'] = info[4]
            dataItem['position'] = info[5]
            self.show_time("抛出第"+str(rawline)+"行数据")
             ##抛出生成器
            yield dataItem
        pass

       
        
        self.show_time("数据解析结束!")

    def show_time(self,text):
        print ("#",str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())),"-> ",text)






