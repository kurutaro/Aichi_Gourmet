from django.db import models


class Review(models.Model):
    #id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    store_name = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    comment = models.CharField(max_length=255)
    picture = models.FileField(null=True)
#     geom = models.PointField(srid=4326)