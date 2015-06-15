# -*- coding: utf-8 -*-
import json, datetime

from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.http import Http404

from common import page
from article.models import Article

def home(request, template_name='article/article_home.html'):
    articles_0 = Article.objects.filter(article_type=0)[:5]
    articles_1 = Article.objects.filter(article_type=1)[:5]
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def article_list(request, article_type=0, template_name='article/article_list.html'):

    article_type = int(article_type)
    article_type_dis = dict(Article.TYPE_CHOICES)[article_type]
    articles = Article.objects.filter(article_type=article_type)

    # 分页
    page_num = int(request.REQUEST.get('page', 1))
    page_objs = page.Cpt(articles, count=10, page=page_num).info
    articles = page_objs[0]
    page_params = (page_objs[1], page_objs[4])

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def article_detail(request, article_id=1, template_name='article/article_detail.html'):
    article = Article.objects.get(id=article_id)
    article_type = int(article.article_type)
    article_type_dis = dict(Article.TYPE_CHOICES)[article_type]
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def article_old_news(request):
    print request.path
    obj = Article.objects.filter(from_url=request.path[1:])
    if not obj:
        raise Http404

    obj = obj[0]

    return redirect('/article/%s' % obj.id)