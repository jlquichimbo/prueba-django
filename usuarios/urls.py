from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_turismo', views.login_turismo, name='login_turismo'),
]