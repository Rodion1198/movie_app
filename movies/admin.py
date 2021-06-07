from django.contrib import admin   # noqa: F401

from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
