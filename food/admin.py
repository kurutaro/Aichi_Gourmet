from django.contrib import admin
from food.models import Genre, Location, User, Store, Picture



#インラインでの管理画面
class PictureInline(admin.StackedInline):
    model = Picture
    extra = 10

class StoreAdmin(admin.ModelAdmin):
    inlines = [PictureInline]



#単体の管理画面
admin.site.register(Genre)
admin.site.register(Location)
admin.site.register(User)
admin.site.register(Picture)
admin.site.register(Store, StoreAdmin)
