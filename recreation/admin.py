from django.contrib import admin
from .models import Article, Video


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Critical Information', {'fields': ['title', 'publisher', 'time']}),
        ('Others', {'fields': ['description', 'part_1', 'part_2', 'part_3']}),
    ]
    list_display = ('title', 'publisher', 'time')
    search_fields = ['title']
    list_filter = ['time', 'publisher']


class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Critical Information', {'fields': ['title', 'publisher', 'url', 'time']}),
        ('Others', {'fields': ['description']}),
    ]
    list_display = ('title', 'publisher', 'time')
    search_fields = ['title']
    list_filter = ['time', 'publisher']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Video, VideoAdmin)

