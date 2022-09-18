from django.contrib import admin
from .models import Member,Blog,Author,Entry

class Memberadmin(admin.ModelAdmin):
    list_display=['username','password']
admin.site.register(Entry)
admin.site.register(Blog)
admin.site.register(Member,Memberadmin)
admin.site.register(Author)

# Register your models here.
