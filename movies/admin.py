from django.contrib import admin

from .models import MoviesCategory, Cinemas, Movies

admin.site.register(MoviesCategory)
admin.site.register(Cinemas)
admin.site.register(Movies)