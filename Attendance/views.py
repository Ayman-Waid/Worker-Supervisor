from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from emp_app.models import Employee, Attendance  # Assuming the models are in the same directory as views.py
from datetime import datetime
import csv


def add(request):
    if request.method == "POST":
        try:
            employee_id = int(request.POST.get('employee_id', 0))
            date = request.POST.get('date')
            first_part = request.POST.get('first_part')
            second_part = request.POST.get('second_part')

            employee = Employee.objects.get(id=employee_id)

            new_attendance = Attendance(
                employee=employee,
                date=date,
                first_part=(first_part == 'Present'),
                second_part=(second_part == 'Present')
            )
            new_attendance.save()

            messages.success(request, 'Attendance marked successfully')
            return redirect('index')

        except (ValueError, Employee.DoesNotExist) as e:
            messages.error(request, f"Invalid input or Employee not found: {e}")
            return redirect('addA')

    elif request.method == "GET":
        employees = Employee.objects.all()
        return render(request, "addA.html", {'employees': employees})

    else:
        return render(request, "addA.html", {'error_message': "An exception occurred! Attendance has not been marked!"})









def all(request):
    attendance = Attendance.objects.all()
    context = {
        'attendance': attendance
    }
    
    return render(request, 'all.html', context)



def download(request):
    try:
        attendance_data = Attendance.objects.all()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employee_attendance_data.csv"'

        writer = csv.writer(response)
        writer.writerow(['Employee ID', 'Employee Name', 'first part', 'second part', 'date'])

        for att in attendance_data:
            writer.writerow([att.employee.id,
                             f'{att.employee.first_name} {att.employee.last_name}',
                             att.first_part,
                             att.second_part,
                             att.date
                             ])

        return response

    except Exception as e:
        return HttpResponse(f"Oops! Something went wrong: {e}")

def remove(request, attendance_id=0):
    if attendance_id:
        try:
            attendance_delete = Attendance.objects.get(id=attendance_id)
            attendance_delete.delete()
            
        except Attendance.DoesNotExist:
            return HttpResponse("attendance not found.")
        except Exception as e:
            return HttpResponse(f"Oops! Something went wrong: {e}")

    attendance = Attendance.objects.all()
    context = {
        'attendance': attendance
    }
    return render(request, 'all.html', context)