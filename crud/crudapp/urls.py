from .views import index
from django.urls import path
from crudapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('show/', views.show, name="show"),
    path('edit/<id>', views.edit, name="edit"),
    path('delete/<id>', views.destroy, name="destroy"),

]
