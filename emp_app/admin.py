# admin.py

from django.contrib import admin
from .models import Department, Role, Employee, Salary, Author, Category , Attendance

admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Author)
admin.site.register(Category)
