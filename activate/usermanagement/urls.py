from django.urls import path
from django.contrib.auth import views as auth_views
from activate.settings import LOGOUT_REDIRECT_URL as LOGOUT
from . import views

app_name = 'usermanagement'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usermanagement/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page=LOGOUT), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
