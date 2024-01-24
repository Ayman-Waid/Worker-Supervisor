from django.urls import path
from .views import all,add,remove,download

app_name = 'Attendance'

urlpatterns = [

    path('all/', all, name='all'),
    path('add/',add,name='add'),
    path('remove/<int:attendance_id>',remove, name='remove'),
    path('remove/', remove, name='remove'),
    path('download/',download,name='download'),

    
]
