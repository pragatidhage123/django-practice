from django.shortcuts import render
from django.http import request, HttpResponse
from .models import *


# Create your views here.

def login(request):
    return HttpResponse("this is login page")

def get_add_data(request):

    #return HttpResponse("this is working")
    #print(request)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        Student.objects.create(first_name=first_name,last_name=last_name,address=address,contact_number=contact_number)


        return HttpResponse("data added")
    
    return render (request,'student.html')

def all_data(request):
    student_data = Student.objects.all()
    return render (request,'student_details.html', {'student_data' : student_data})
    

def teacher_get_data(request):

    #return HttpResponse(" this is working")

    if request.method == 'POST':
        
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        qualification = request.POST.get('qualification')
        blood_group = request.POST.get("blood_group")
        married_status = request.POST.get("married_status")
        gender = request.POST.get("gender")

        Teacher.objects.create(last_name=last_name,age=age,qualification=qualification,blood_group=blood_group,married_status=married_status,gender=gender)


        return HttpResponse("teacher data added")
    
    return render (request,'teacher.html')

def all_teacher_data(request):
    teacher_data = Teacher.objects.all()
    return render (request,'teacher_details.html', {'teacher_data' : teacher_data})


    


    



    
        
    
