# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User


class Blog(models.Model):
    def __unicode__(self):
        return self.name

    user = models.ForeignKey(
        User,
    )

    name = models.CharField(
        u"ブログ名",
        max_length=256
    )

    description = models.TextField(
        u"説明",
        max_length=1024,
        blank=True
    )

    header = models.TextField(
        u"ヘッダー",
        max_length=1024,
        blank=True
    )

    footer = models.TextField(
        u"フッター",
        max_length=1024,
        blank=True
    )

    created_at = models.DateTimeField(
        u"作成日時",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        u"更新日時",
        auto_now=True
    )

    class Meta:
        ordering = ['-updated_at']
        verbose_name = u'ブログ'
        verbose_name_plural = u'ブログ'


class Post(models.Model):
    def __unicode__(self):
        return self.title

    blog = models.ForeignKey(
        Blog
    )

    title = models.CharField(
        u"タイトル",
        max_length=255,
    )

    contents = models.TextField(
        u"コンテンツ",
    )

    created_at = models.DateTimeField(
        u"作成日時",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        u"更新日時",
        auto_now=True
    )

    class Meta:
        ordering = ['-updated_at']
        verbose_name = u'投稿'
        verbose_name_plural = u'投稿'