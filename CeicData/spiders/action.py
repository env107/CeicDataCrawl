import scrapy
from CeicData.items import CeicdataItem
import sys

class action(scrapy.Spider):

    name = "CeicData"
    allowed_domain = ['http://news.ceic.ac.cn']
    start_urls = ['http://news.ceic.ac.cn/index.html']

    def parse(self , response):
        print ("======= 开始挖掘数据 =======")
        #爬取每一行地震内容
        rawData = response.xpath("//div[@class='news-content']/table//tr[position()>1]")

        dataItem = CeicdataItem()
        
        #获取每一行内容
        for raw in rawData:
            info = raw.xpath(".//td//text()").extract()
            dataItem['level'] = info[0]
            dataItem['time'] = info[1]
            dataItem['lat'] = info[2]
            dataItem['lon'] = info[3]
            dataItem['deep'] = info[4]
            dataItem['position'] = info[5]
            print ("======= 已解析数据 =======")
             ##抛出生成器
            yield dataItem
        pass

       
        
        print ("======= 数据解析结束 =======")






