from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    # path('room/', views.room, name='room')
    path('room/<str:pk>/', views.room, name='room')
]
