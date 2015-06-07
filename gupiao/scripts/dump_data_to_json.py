# coding: utf-8

import sqlite3, os, json

sql = "select log_ID, log_cateid, log_authorid, log_level, log_url, log_title, log_intro, log_content, log_posttime from blog_Article"
db_path = "%s/data/gupiao.sqlite" % os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print u"数据库路径===> %s" % db_path

con = sqlite3.connect(db_path)
cur = con.cursor()
cur.execute(sql)
results = cur.fetchall()

data = []
total = 0

for x in results:
	total += 1
	data.append({
		"id": x[0],
		"category_id": x[1],
		"author_id": x[2],
		"level": x[3],
		"url": x[4],
		"title": x[5],
		"info": x[6],
		"content": x[7],
		"time": x[8]
	})

# print data
# datetime.date.fromtimestamp(1380114841000/1000)
print u"共导出 [ %s ] 条数据" % total
