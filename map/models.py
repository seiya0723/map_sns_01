from django.db import models

#追加の制約
from django.core.validators import MinValueValidator,MaxValueValidator


class Category(models.Model):

    name        = models.CharField(verbose_name="カテゴリ名",max_length=20)


class Place(models.Model):

    comment     = models.CharField(verbose_name="コメント",max_length=500)

    category    = models.ForeignKey(Category,verbose_name="カテゴリ",on_delete=models.CASCADE)
    
    lat         = models.DecimalField(verbose_name="緯度",max_digits=9, decimal_places=6)
    lon         = models.DecimalField(verbose_name="経度",max_digits=9, decimal_places=6)

    photo       = models.ImageField(verbose_name="写真",upload_to="map/place/photo")

    #TODO:ここにユーザーモデルとつながるForeignKeyを追加する。(誰が投稿したかを記録するため）


class Review(models.Model):

    place       = models.ForeignKey(Place,verbose_name="レビュー対象の投稿",on_delete=models.CASCADE)
    comment     = models.CharField(verbose_name="コメント",max_length=500)

    #評価の星アイコン
    #https://noauto-nolife.com/post/django-star-average/
    star        = models.IntegerField(verbose_name="星",validators=[MinValueValidator(1),MaxValueValidator(5)])


    #TODO:ここにユーザーモデルとつながるForeignKeyを追加する。(誰が投稿したかを記録するため）





