from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show'),
    path('edit/<id>', views.edit, name='show'),
    path('delete/<id>', views.destroy, name='show')
]