#coding: utf-8
import datetime
from django.db import models

from common.utils import get_summary_from_html, sub_string


class Article(models.Model):
    TYPE_CHOICES = (
        (0, '老站数据'),
        (1, '国内财经'),
    )
    
    title = models.CharField(max_length=128)
    content = models.TextField()
    article_type = models.IntegerField(choices = TYPE_CHOICES, default=1)
    from_url = models.CharField(max_length=128, unique=True)
    img = models.CharField(max_length=128, null=True, blank=True)
    sort_num = models.IntegerField(default=0, db_index=True)
    state = models.BooleanField(default=True, db_index=True)
    create_time = models.DateTimeField(default=datetime.datetime.now, db_index=True)

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
