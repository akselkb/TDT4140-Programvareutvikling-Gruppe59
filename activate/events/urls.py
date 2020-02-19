from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('create/', views.create_activity, name='create_activity'),
    path('<int:index>/', views.activity_detail_view, name='activity_detail_view'),
]
