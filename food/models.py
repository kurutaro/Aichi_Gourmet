from django.db import models


class Genre(models.Model):
    #id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    GENRE_SELECT = (
        ('居酒屋', '居酒屋'),
        ('カフェ', 'カフェ'),
        ('うなぎ', 'うなぎ'),
        ('ラーメン', 'ラーメン'),
    )

    genre = models.CharField(max_length=5, choices=GENRE_SELECT)

    def __str__(self):
        return self.genre


class Location(models.Model):
    #id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    LOCATION_SELECT = (
        ('名古屋市内', '名古屋市内'),
        ('一宮・犬山・瀬戸', '一宮・犬山・瀬戸'),
        ('知多・半田・中部国際空港', '知多・半田・中部国際空港'),
        ('豊田・岡崎・安城', '豊田・岡崎・安城'),
        ('豊橋・蒲郡・伊良湖', '豊橋・蒲郡・伊良湖'),
    )

    locate = models.CharField(max_length=15, choices=LOCATION_SELECT)

    def __str__(self):
        return self.locate



class User(models.Model):
    #id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要

    SEX_SELECT = (
        ('男性', '男性'),
        ('女性', '女性'),
    )

    user_name = models.CharField(max_length=10)
    sex = models.CharField(max_length=2, choices=SEX_SELECT)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.user_name


class Store(models.Model):
    #id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    store_name = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    link = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.store_name



class Picture(models.Model):
    #id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    picture = models.ImageField(upload_to='documents/', default='defo')
    store = models.ForeignKey(Store, related_name='pictures', on_delete=models.CASCADE)





