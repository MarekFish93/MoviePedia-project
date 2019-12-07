from django.urls import path, include
from register_login import views
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies', views.FilmView)

urlpatterns = [
    path('', include(router.urls))
]
