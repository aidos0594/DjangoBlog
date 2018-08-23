from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from news.models import News, Tag, Category, Comments


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_min', 'text')


admin.site.register(News, NewsAdmin)
admin.site.register(Tag)
admin.site.register(Category)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'text', 'created', 'moderation')


admin.site.register(Comments, CommentAdmin)
