from django.contrib import admin
from .models import Article,Reporter,studentModel

admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(studentModel)
# Register your models here.
