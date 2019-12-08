from django.urls import path, include, re_path
from register_login import views
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.FilmView, basename = 'Film')

urlpatterns = [
    re_path('(?P<filmid>[-\w]+)/comments/$', views.CommentsListView.as_view()),
    re_path('(?P<rateid>[-\w]+)/rating/$', views.RateListView.as_view()),
    path('', include(router.urls)),
]
