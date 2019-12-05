from django.urls import path
from . import views
from .views import IndexPageView, register

app_name = 'register_login'

urlpatterns = [
    path('user_login/', views.user_login, name = 'user_login' ),
    path('register/', views.register, name = 'register')
]
