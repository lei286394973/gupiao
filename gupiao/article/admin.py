from django.contrib import admin

from models import Article, Link

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # fields = ('title', 'content', 'article_type', 'from_url', 'state')
    list_display = ('title', 'from_url', 'state')
    search_fields = ['title',]

admin.site.register(Article, ArticleAdmin)

class LinkAdmin(admin.ModelAdmin):

    list_display = ('name', 'site')
    search_fields = ['name',]

admin.site.register(Link, LinkAdmin)