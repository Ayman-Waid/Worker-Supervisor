from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ValidationError
from django.utils.html import escape
from django.http import JsonResponse
from .models import Employee, Role, Department
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q, Count
import csv





def index(request):
    return render(request, 'index.html')

def all(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'view.html', context)

def add(request):
    if request.method == "POST":
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            salary = int(request.POST['salary'])
            bonus = int(request.POST['bonus'])
            phone = int(request.POST['phone'])
            dept = int(request.POST['dept'])
            role = int(request.POST['role'])

            new_emp = Employee(
                first_name=first_name,
                last_name=last_name,
                salary=salary,
                bonus=bonus,
                dept_id=dept,
                role_id=role,
                phone=phone,
                hire_date=datetime.now()
            )
            new_emp.save()

            messages.success(request, 'Employee added successfully')
            return redirect('all')

        except ValueError as ve:
            messages.error(request, f"Invalid input: {ve}")
            return redirect('add')

    elif request.method == "GET":
        return render(request, "add.html")

    else:
        return HttpResponse("An exception occurred! Employee has not been added!")

def all(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'view.html', context)

def remove(request, emp_id=0):
    if emp_id:
        try:
            emp_delete = Employee.objects.get(id=emp_id)
            emp_delete.delete()
            
        except Employee.DoesNotExist:
            return HttpResponse("Employee not found.")
        except Exception as e:
            return HttpResponse(f"Oops! Something went wrong: {e}")

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'view.html', context)

def filter(request):
    emps = Employee.objects.all()
    title_contains_query = request.GET.get('title_contains')

    if title_contains_query is not None and title_contains_query.strip() != '':
        emps = emps.filter(
            Q(first_name__icontains=title_contains_query) |
            Q(last_name__icontains=title_contains_query) |
            Q(dept__name__icontains=title_contains_query) |
            Q(salary__icontains=title_contains_query) |
            Q(bonus__icontains=title_contains_query) |
            Q(role__name__icontains=title_contains_query) |
            Q(phone__icontains=title_contains_query) |
            Q(hire_date__icontains=title_contains_query)
        ).distinct()

    context = {'emps': emps}

    return render(request, 'filter.html', context)




def validate_integer_inputs(*args):
    for arg in args:
        if not isinstance(arg, int):
            raise ValueError(f"Invalid input: {arg} is not a valid integer")


def download(request):
    try:
        emp_data = Employee.objects.all()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employee_salary_data.csv"'

        writer = csv.writer(response)
        writer.writerow(['first_name', 'last_name', 'dept', 'salary', 'role', 'phone','hire_date'])

        for emp in emp_data:
            writer.writerow([emp.first_name,
                             emp.last_name,
                             emp.bonus,
                             emp.dept,
                             emp.role,
                             emp.phone,
                             emp.hire_date
                             ])

        return response

    except Exception as e:
        return HttpResponse(f"Oops! Something went wrong: {e}")
