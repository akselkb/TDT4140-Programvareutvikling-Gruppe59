from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.view_login, name='view_login'),
    path('logout/', views.view_logout, name='view_logout'),
]