#! /bin/bash

echo "开始进行爬虫..."
#/home/admin/python/CeicDataCrawl/CeicData
time=`date +%Y%m%d%H%i%s`
py3=`which python3`
$py3 /home/admin/python/CeicDataCrawl/CeicData/main.py > log/pull_$time.log

echo "爬虫结束"


