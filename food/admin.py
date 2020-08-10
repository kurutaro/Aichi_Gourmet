from django.contrib import admin
from food.models import Genre, Location, User, Store, Comment, Picture

# Register your models here.
admin.site.register(Genre)
admin.site.register(Location)
admin.site.register(User)
admin.site.register(Store)
admin.site.register(Comment)
admin.site.register(Picture)
