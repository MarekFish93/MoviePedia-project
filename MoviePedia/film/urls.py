from django.urls import path, re_path
from . import views

app_name = 'film'

urlpatterns = [
    path('<int:pk>', views.FilmDetailView, name = 'detail'),
]
