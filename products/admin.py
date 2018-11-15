from django.contrib import admin

# Register your models here.
from .models import whiskey,beer,wine,rum,vodka

admin.site.register(whiskey)
admin.site.register(beer)
admin.site.register(wine)
admin.site.register(rum)
admin.site.register(vodka)

