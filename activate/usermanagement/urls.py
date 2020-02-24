from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.view_login, name='view_login'),
    path('logout/', views.view_logout, name='view_logout'),
    path('signup/', views.view_signup, name='view_signup'),
    path('profile/', views.view_profile, name='view_profile'),
    path('modify_profile', views.view_modify_profile, name='view_modify_profile')
]
