from django.contrib import admin
from db.models import Film, Rate, Comment, SubComment

# Register your models here.
admin.site.register(Film)
admin.site.register(Rate)
admin.site.register(Comment)
admin.site.register(SubComment)
