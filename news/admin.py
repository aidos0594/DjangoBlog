from django.contrib import admin
from news.models import News, Tag, Category

admin.site.register(News)
admin.site.register(Tag)
admin.site.register(Category)
