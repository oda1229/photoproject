from django.db import models

# Create your models here.
from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(verbose_name="カテゴリー", max_length=20)

    def __str__(self):
        return self.title


class PhotoPost(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="ユーザ", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, verbose_name="カテゴリ", on_delete=models.PROTECT
    )
    title = models.CharField(verbose_name="タイトル", max_length=200)
    comment = models.TextField(verbose_name="コメント")
    image1 = models.ImageField(verbose_name="イメージ1", upload_to="photos", blank=True)
    posted_at = models.DateTimeField(verbose_name="投稿日時", auto_now=True)

    def __str__(self):
        return self.title
