from django.urls import path
from .views import all,add,remove,download

app_name = 'salary'

urlpatterns = [

    path('all_Salary/', all, name='all_Salary'),
    path('add_Salary/',add,name='add_Salary'),
    path('remove/<int:salary_id>',remove, name='remove'),
    path('remove/', remove, name='remove'),
    path('download/',download,name='download'),

    
]
