from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.utils import timezone
from django.core.mail import send_mail
from string import Template
<<<<<<< HEAD
=======
from django.conf import settings
>>>>>>> 81015634b8e36a993e3ca7cd80617fe763251824
# Create your views here.
def index(request):
    popup=notification.objects.all()[0]
    extraSkills=ExtraSkills.objects.all().order_by("priority")
    keySkills=KeySkills.objects.all().order_by("priority")
    degSkills=DegSkills.objects.all().order_by("priority")
    experience=Experience.objects.all().order_by('-id')
    education=Education.objects.all().order_by('-id')
    recntWork=recentWork.objects.all().order_by('-id')
<<<<<<< HEAD
    pProjects=personalProjects.objects.all().order_by('-id')
    abo=about.objects.all()[0]
=======
    personal_projects=personalProjects.objects.all().order_by('-id')
    about_section=about.objects.all()[0]
>>>>>>> 81015634b8e36a993e3ca7cd80617fe763251824
    profile=userProfile.objects.all()[0]
    endors=endorsement.objects.all()
    certificates=certification.objects.all()
    companies=companiesWorkedFor.objects.all()
    meta=meta_info.objects.all()[0]
    sections=sectionEnableDisable.objects.all()[0]
<<<<<<< HEAD
    return render(request,'index.html',{"popup":popup,"host_name": request.get_host(),"sections":sections,"meta":meta,"certificates":certificates,"comapnies":companies,"endorsment":endors,"profile":profile,"extraSkills":extraSkills,"keySkills":keySkills,"degSkills":degSkills,"experience":experience,"education":education,"recentWork":recntWork,"personalProject":pProjects,"about":abo})
=======
    return render(request,'index.html',{"popup":popup,"host_name": request.get_host(),"sections":sections,"meta":meta,"certificates":certificates,"comapnies":companies,"endorsment":endors,"profile":profile,"extraSkills":extraSkills,"keySkills":keySkills,"degSkills":degSkills,"experience":experience,"education":education,"recentWork":recntWork,"personalProject":personal_projects,"about":about_section})
>>>>>>> 81015634b8e36a993e3ca7cd80617fe763251824

def contact(request):

    name = request.POST.get("name")
    print(name)
    msg = request.POST.get("msg")
    email = request.POST.get("email")
    print(email)
    msg=Template('Name: $name , Email: $email , Msg: $msg').substitute(name=name,email=email,msg=msg)
    try:
        send_mail(
            'Query',
            msg,
<<<<<<< HEAD
            'contact@orendra.com',
            ['contact@orendra.com'],
=======
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
>>>>>>> 81015634b8e36a993e3ca7cd80617fe763251824
            fail_silently=False,
        )
        status = 200
    except Exception as e:
        print(e)
        status = 400

    data = "done"

    return JsonResponse({"msg": data}, status=status)