from django.contrib import admin
from db.models import Film, Rate, Comment

# Register your models here.
admin.site.register(Film)
admin.site.register(Rate)
admin.site.register(Comment)
