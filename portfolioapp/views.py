from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    popup=notification.objects.get(id=1)
    testimoni=testimonial.objects.get(id=1)
    extraSkills=ExtraSkills.objects.all().order_by("priority")
    keySkills=KeySkills.objects.all().order_by("priority")
    degSkills=DegSkills.objects.all().order_by("priority")
    experience=Experience.objects.all().order_by('-id')
    education=Education.objects.all().order_by('-id')
    recntWork=recentWork.objects.all().order_by('-id')
    pProjects=personalProjects.objects.all().order_by('-id')
    abo=about.objects.all()[0]
    profile=userProfile.objects.all()[0]
    endors=endorsement.objects.all()
    certificates=certification.objects.all()
    companies=companiesWorkedFor.objects.all()
    sections=sectionEnableDisable.objects.all()[0]
    return render(request,'index.html',{"popup":popup,"sections":sections,"certificates":certificates,"comapnies":companies,"endorsment":endors,"profile":profile,"extraSkills":extraSkills,"keySkills":keySkills,"degSkills":degSkills,"experience":experience,"education":education,"recentWork":recntWork,"personalProject":pProjects,"testimonial":testimoni,"about":abo})