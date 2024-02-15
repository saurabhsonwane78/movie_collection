from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.user_registration, name='user_registration'),
    path('api/login/', views.user_login, name='user_login'), 
    path('api/collections/', views.collection_list, name='collection_list'),
    path('<str:collection_uuid>/', views.collection_detail, name='collection_detail'),
    path('', views.create_collection, name='create_collection'),
]
