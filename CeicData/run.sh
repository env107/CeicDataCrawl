#! /bin/bash

echo "开始进行爬虫..."
cd /home/admin/python/CeicDataCrawl/CeicData #进入目录
# time=`date +%Y%m%d%H%I%S`

/usr/local/bin/python3 /home/admin/python/CeicDataCrawl/CeicData/main.py > /home/admin/python/CeicDataCrawl/CeicData/log/parse.log

echo "爬虫结束"


