# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# import json
import base64
import traceback
import pickle

class CeicdataPipeline(object):
    def process_item(self, item, spider):
        # db = pymysql.connect("localhost","root","root","ceicdata",charset='utf8')
        db = pymysql.connect("mysqlserver","ceicdata","aU13#25cPl371","ceicdata",charset='utf8')
        #首先查找hash值是否存在
        hashstr = base64.b64encode(pickle.dumps(item))
        cursor = db.cursor()
        checkSql = 'SELECT count(`hash`) as length FROM `current_data` WHERE `hash`=%s'
        cursor.execute(checkSql,(hashstr))
        checkData = cursor.fetchone()
        if(checkData[0] > 0 ):
            print("该数据已经存在,无需再记录!")
        else:
            print("开始写入数据")
            print(item)
            #写入数据库
            sql = 'INSERT INTO `current_data`(level,happenTime,lat,lon,deep,position,hash) VALUES(%s,%s,%s,%s,%s,%s,%s)'
            
            try:
                cursor.execute(sql,(item['level'],item['time'],item['lat'],item['lon'],item['deep'],item['position'],hashstr))
                db.commit()
            except BaseException:
                print(traceback.format_exc())
                db.rollback()
        pass

        db.close()

        return item
