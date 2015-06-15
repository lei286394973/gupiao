#coding: utf-8

import os, sys
# 引入父目录来引入其他模块
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([
    os.path.abspath(os.path.join(SITE_ROOT, '../')),
    os.path.abspath(os.path.join(SITE_ROOT, '../../')),
])
os.environ['DJANGO_SETTINGS_MODULE'] = 'gupiao.settings'

import requests, datetime, time
from pyquery import PyQuery as pq

from article.models import Article

def sync_zskx():
	url = "http://news.cnstock.com/bwsd/"
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36"}
	rep = requests.get(url, headers=headers)

	tags = pq(rep.text).find('#bw-list .title a')

	for x in range(len(tags)):
	 	# title = tags.eq(x).attr('title').encode('latin1')
	 	article_url = tags.eq(x).attr('href')

	 	# 获取文章信息
	 	rep = requests.get(article_url, headers=headers)
	 	dom = pq(rep.text)
	 	title = dom.find('h1.title').text()
	 	create_time = dom.find('.bullet .timer').text()
	 	content = dom.find('#qmt_content_div').html()
	 	
	 	try:
		    Article.objects.create(
		        title = title,
		        content = content,
		        article_type = 1,
		        from_url = article_url,
		        create_time = datetime.datetime.strptime(create_time, '%Y-%m-%d %H:%M:%S')
		    )
		except Exception, e:
		    print e
		    break

		time.sleep(15)


if __name__ == "__main__":
	sync_zskx()