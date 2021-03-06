from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.utils import timezone
from django.core.mail import send_mail
from string import Template
from django.conf import settings
# Create your views here.
def index(request):
    popup=notification.objects.all()[0]
    extraSkills=ExtraSkills.objects.all().order_by("priority")
    keySkills=KeySkills.objects.all().order_by("priority")
    degSkills=DegSkills.objects.all().order_by("priority")
    experience=Experience.objects.all().order_by('-id')
    education=Education.objects.all().order_by('-id')
    recntWork=recentWork.objects.all().order_by('-id')
    personal_projects=personalProjects.objects.all().order_by('-id')
    about_section=about.objects.all()[0]
    profile=userProfile.objects.all()[0]
    endors=endorsement.objects.all()
    certificates=certification.objects.all()
    companies=companiesWorkedFor.objects.all()
    meta=meta_info.objects.all()[0]
    sections=sectionEnableDisable.objects.all()[0]
    return render(request,'index.html',{"popup":popup,"host_name": request.get_host(),"sections":sections,"meta":meta,"certificates":certificates,"comapnies":companies,"endorsment":endors,"profile":profile,"extraSkills":extraSkills,"keySkills":keySkills,"degSkills":degSkills,"experience":experience,"education":education,"recentWork":recntWork,"personalProject":personal_projects,"about":about_section})

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
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        status = 200
    except Exception as e:
        print(e)
        status = 400

    data = "done"

    return JsonResponse({"msg": data}, status=status)