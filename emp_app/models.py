# models.py

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salaries')
    basic_salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    deductions = models.IntegerField(default=0)
    net_salary = models.IntegerField(default=0)

    def __str__(self):
        return f"Salary for {self.employee.first_name} {self.employee.last_name}"
    
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Attendance')
    first_part = models.BooleanField(default=False)
    second_part = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return f"Attendance for {self.employee.first_name} {self.employee.last_name}"

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
