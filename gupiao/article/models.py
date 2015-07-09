#coding: utf-8
import datetime
from django.db import models

from common.utils import get_summary_from_html, sub_string


class Article(models.Model):
    TYPE_CHOICES = (
        (0, '老站数据'),
        (1, '国内财经'),
    )
    
    title = models.CharField(max_length=128, verbose_name=u"标题")
    content = models.TextField(verbose_name=u"文章内容")
    article_type = models.IntegerField(choices = TYPE_CHOICES, default=1, verbose_name=u"文章类型")
    from_url = models.CharField(max_length=128, unique=True, verbose_name=u"来源")
    img = models.CharField(max_length=128, null=True, blank=True, verbose_name=u"图片")
    sort_num = models.IntegerField(default=0, db_index=True, verbose_name=u"排序")
    state = models.BooleanField(default=True, db_index=True, verbose_name=u"是否有效")
    create_time = models.DateTimeField(default=datetime.datetime.now, db_index=True, verbose_name=u"创建时间")

    class Meta:
        ordering = ["-sort_num", "-create_time"]

    def get_url(self):
        if self.article_type == 0:
            return self.from_url
        return "/article/%s" % self.id

    def get_date(self):
        return self.create_time.strftime('%Y-%m-%d')

    def get_info(self):
        return sub_string(get_summary_from_html(self.content, 100), 65)


class Link(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"名称")
    site = models.CharField(max_length=256, verbose_name=u"网址")