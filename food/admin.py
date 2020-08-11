from django.contrib import admin
from food.models import Genre, Location, User, Store, Picture

# Register your models here.
admin.site.register(Genre)
admin.site.register(Location)
admin.site.register(User)
admin.site.register(Store)
admin.site.register(Picture)
