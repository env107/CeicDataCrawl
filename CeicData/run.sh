#! /bin/bash

echo "开始进行爬虫..."
#/home/admin/python/CeicDataCrawl/CeicData
time=date +%Y%m%d%H%i%s
python3 /home/admin/python/CeicData/CeicData/main.py > log/pull_$time.log

echo "爬虫结束"


