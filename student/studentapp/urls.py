from django.urls import path
from studentapp import views

urlpatterns = [
     path('',views.index,name='index'),
     path('show/',views.show,name='show'),
     path('edit/<id>',views.edit,name='edit'),
     path('delete/<id>',views.delete,name='delete')


]
