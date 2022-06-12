from django.urls import path
from dtlapp import views

urlpatterns = [
    path('',views.home , name='home')
]
