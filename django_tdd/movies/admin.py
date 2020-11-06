from django.contrib import admin
from .models import Movie, CustomUser

admin.site.register(Movie)# Register your models here.
admin.site.register(CustomUser)