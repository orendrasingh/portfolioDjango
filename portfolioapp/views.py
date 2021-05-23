from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    popup=notification.objects.get(id=1)
    testimoni=testimonial.objects.get(id=1)
    extraSkills=ExtraSkills.objects.all()
    keySkills=KeySkills.objects.all()
    degSkills=DegSkills.objects.all()
    experience=Experience.objects.all().order_by('-id')
    education=Education.objects.all().order_by('-id')
    recntWork=recentWork.objects.all().order_by('-id')
    pProjects=personalProjects.objects.all().order_by('-id')
    abo=about.objects.all()[0]
    return render(request,'index.html',{"popup":popup,"extraSkills":extraSkills,"keySkills":keySkills,"degSkills":degSkills,"experience":experience,"education":education,"recentWork":recntWork,"personalProject":pProjects,"testimonial":testimoni,"about":abo})