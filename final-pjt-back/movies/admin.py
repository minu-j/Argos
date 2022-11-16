from django.contrib import admin
from .models import Movie, Review, Rating

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Rating)