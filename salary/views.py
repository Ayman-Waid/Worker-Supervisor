# salary/views.py
from emp_app.models import Salary,Employee
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
import csv






def all(request):
    salary = Salary.objects.all()
    context = {
        'salary': salary
    }
    
    return render(request, 'all_Salary.html', context)




def add(request):
    if request.method == "POST":
        try:
            employee_id = int(request.POST.get('employee_id', 0))
            basic_salary = int(request.POST.get('basic_salary', 0))
            bonus = int(request.POST.get('bonus', 0))
            deductions = int(request.POST.get('deductions', 0))

            employee = Employee.objects.get(id=employee_id)

            new_salary = Salary(
                employee=employee,
                basic_salary=basic_salary,
                bonus=bonus,
                deductions=deductions,
                net_salary=basic_salary + bonus - deductions
            )
            new_salary.save()

            messages.success(request, 'Salary added successfully')
            return redirect('index')

        except (ValueError, Employee.DoesNotExist) as e:
            messages.error(request, f"Invalid input or Employee not found: {e}")
            return redirect('add_Salary')

    elif request.method == "GET":
        employees = Employee.objects.all()
        return render(request, "add_Salary.html", {'employees': employees})

    else:
        return render(request, "add_Salary.html", {'error_message': "An exception occurred! Salary has not been added!"})


def remove(request, salary_id=0):
    if salary_id:
        try:
            salary_delete = Salary.objects.get(id=salary_id)
            salary_delete.delete()
            
        except Salary.DoesNotExist:
            return HttpResponse("salary not found.")
        except Exception as e:
            return HttpResponse(f"Oops! Something went wrong: {e}")

    salary = Salary.objects.all()
    context = {
        'salary': salary
    }
    return render(request, 'all_Salary.html', context)


def download(request):
    try:
        salary_data = Salary.objects.all()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employee_salary_data.csv"'

        writer = csv.writer(response)
        writer.writerow(['Employee ID', 'Employee Name', 'Basic Salary', 'Bonus', 'Deductions', 'Net Salary'])

        for salary in salary_data:
            writer.writerow([salary.employee.id,
                             f'{salary.employee.first_name} {salary.employee.last_name}',
                             salary.basic_salary,
                             salary.bonus,
                             salary.deductions,
                             salary.net_salary])

        return response

    except Exception as e:
        return HttpResponse(f"Oops! Something went wrong: {e}")
