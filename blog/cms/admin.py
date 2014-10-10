# -*- coding: utf-8 -*-

from django.contrib import admin

from cms.models import Blog
from cms.models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "user",
        "name",
        'description',
        'created_at',
        'updated_at'
    )

    search_fields = ['^id', 'name', "description"]


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "blog_name",
        "contents",
        'created_at',
        "updated_at",
    )

    def blog_name(self, obj):
        return obj.blog.name

    blog_name.short_description = 'ブログ名'

admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)