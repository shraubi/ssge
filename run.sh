#!/bin/sh
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
python3 -m scrapy crawl s2sge
