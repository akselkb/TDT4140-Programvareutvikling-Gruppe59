from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('create/', views.create_activity, name='create_activity'),
    path('<int:id>/', views.activity_detail_view, name='activity_detail_view'),
    url(r'^register/(\d+)/$', views.register, name='register'),
    path('me/', views.organized_activities_view, name='organized_activities')
]
