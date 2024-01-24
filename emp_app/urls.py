
from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [    
    path('', views.index, name='index'),
    
    path('all', views.all, name='all'),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove'),
    path('remove/<int:emp_id>', views.remove, name='remove'),
    path('filter/', views.filter, name='filter'),
    path('download/',views.download,name='download'),

    

]
