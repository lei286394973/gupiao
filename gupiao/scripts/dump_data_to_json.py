# coding: utf-8

import sqlite3, os, json, sys, datetime

# 引入父目录来引入其他模块
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([
    os.path.abspath(os.path.join(SITE_ROOT, '../')),
    os.path.abspath(os.path.join(SITE_ROOT, '../../')),
])
os.environ['DJANGO_SETTINGS_MODULE'] = 'gupiao.settings'


from article.models import Article

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

CATEGORYS = {
    1: "cqgupiaokaihu",
    2: "gushi",
    3: "cqgtja",
    4: "touzizheshouce",
    5: "yanjiubaogao",
    6: "sichuan",
    7: "qihuo",
    8: "pinglun",
    9: "rumen",
}

total = 0
for x in data:
    try:
        Article.objects.create(
            title = x['title'],
            content = x['content'],
            article_type = 0,
            from_url = "/%s/%s/%s" % (CATEGORYS[x['category_id']], x['id'], x['id']),
            create_time = datetime.date.fromtimestamp(x['time']/1000)
        )
        total += 1
    except Exception, e:
        print e
        continue


print u"共导入 [ %s ] 条数据" % total