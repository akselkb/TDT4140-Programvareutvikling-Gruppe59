from django.urls import path
from . import views

app_name = 'usermanagement'

urlpatterns = [
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('modify-profile/', views.modify_profile, name='modify_profile')
]
