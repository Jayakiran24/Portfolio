from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Portfolio
def home(request):
    return render(request,'Home.html')

def about(request):
    return render(request,'about.html')

def project(request):
    project_show=[
        {'title':'Ecommerce',
         'path':'images/ecomm1.png'},
        {'title':'Music Straming',
         'path':'images/ecomm2.png'},
         {'title':'Portfolio',
          'path':'images/port.png'}
         ]
    return render (request,'project.html',{'project_show':project_show})

def certificates(request):
    certificate_show=[
        {'title':'Python 101 for Data Science',
        'path':'images/IBM2.png'},
        {'title':'Hadoop 101',
         'path':'images/IBM1.jpg'},
         {'title':'Introduction to internet of Things',
          'path':'images/NPTEL.png'}
            ]
    return render (request,'certificates.html',{'certificate_show':certificate_show})


def contact(request):
    if request.method=='POST':
        name = request.POST.get("name")  # Get form data
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("message")
        Portfolio.objects.create(name=name,email=email,number=number,message=message)
        print("data saved succefully")
        # return redirect('success_page')
    return render(request,'contact.html')
def resume(request):
    resume_path="myapp/Resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type='application/pdf')
            response['content-Disposition']='attachment';filename="Resume.pdf"
            return response
    else:
        return HttpResponse("Resume not found",status=404)