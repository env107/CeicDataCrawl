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
import time
import log

class CeicdataPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect("localhost","root","root","ceicdata",charset='utf8')
        # db = pymysql.connect("127.0.0.1","ceicdata","aU13#25cPl371","ceicdata",charset='utf8',port=37390)
        #首先查找hash值是否存在
        hashstr = base64.b64encode(pickle.dumps(item))
        cursor = db.cursor()
        checkSql = 'SELECT id as length FROM `current_data` WHERE `code`=%s'
        cursor.execute(checkSql,(hashstr))
        checkData = cursor.fetchone()
        self.show_time("检查数据是否已经存在？")
        self.show_time(item)
        log.debug("检查数据是否已经存在？")
        log.debug(item)
        
        if(checkData == None):
            self.show_time("准备写入数据")
            log.debug("准备写入数据...")
            
            #写入数据库
            sql = 'INSERT INTO `current_data`(level,happenTime,lat,lon,deep,position,code) VALUES(%s,%s,%s,%s,%s,%s,%s)'
            
            try:
                cursor.execute(sql,(item['level'],item['time'],item['lat'],item['lon'],item['deep'],item['position'],hashstr))
                db.commit()
                self.show_time("写入数据成功")
                log.debug("数据成功写入数据库")
            except BaseException:
                self.show_time("处理程序出现错误")
                log.error("程序出现错误,该数据停止写入")
                log.error(traceback.format_exc())
                print(traceback.format_exc())
                db.rollback()
            
        else:
            log.debug("该数据已经存在，数据ID为"+str(checkData[0]))
            self.show_time("数据["+str(checkData[0])+"]已存在!")
        pass

        db.close()

        return item

    def show_time(self,text):
        print ("#",str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())),"-> ",text)

        
