from django.db import models
import os
import random
from ckeditor.fields import RichTextField
# Create your models here.
def photo_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(15))
    return 'media/{basename}{randomstring}{ext}'.format(basename=basefilename, randomstring=randomstr, ext=file_extension)


class KeySkills(models.Model):
    skillname=models.TextField(blank=True)
    skilllevel=models.TextField(blank=True)
    skilltype=models.TextField(blank=True)

    def __str__(self):
        return self.skillname

class ExtraSkills(models.Model):
    skillname=models.TextField(blank=True)
    skilllevel=models.TextField(blank=True)
    skilltype=models.TextField(blank=True)

    def __str__(self):
        return self.skillname

class DegSkills(models.Model):
    skillname=models.TextField(blank=True)
    skilllevel=models.TextField(blank=True)
    skilltype=models.TextField(blank=True)

    def __str__(self):
        return self.skillname

class Experience(models.Model):
    company=models.TextField(blank=True)
    logo = models.FileField(upload_to=photo_path, null=True)

    position=models.TextField(blank=True)
    description=RichTextField()
    startDate=models.DateField(blank=True)
    endDate=models.DateField(blank=True,null=True)
    ispresent=models.BooleanField(default=False)

    def __str__(self):
        return self.company

class Education(models.Model):
    college=models.TextField(blank=True)
    logo = models.FileField(upload_to=photo_path, null=True)

    branch=models.TextField(blank=True)
    description=RichTextField()
    startDate=models.DateField(blank=True)
    endDate=models.DateField(blank=True,null=True)
    ispresent=models.BooleanField(default=False)

    def __str__(self):
        return self.college

class personalProjects(models.Model):
    logo = models.FileField(upload_to=photo_path, null=True)
    name=models.TextField(blank=True)
    link=models.URLField(blank=True)
    startDate=models.DateField(blank=True,null=True)
    endDate=models.DateField(blank=True,null=True)
    description=RichTextField()

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.ForeignKey(personalProjects,related_name='technologies', on_delete=models.CASCADE)
    techName=models.TextField(blank=True)
    def __str__(self):
        return self.name.name


class recentWork(models.Model):
    logo=models.FileField(upload_to=photo_path,null=True)
    name=models.TextField(blank=True)
    link=models.URLField(blank=True)
    startDate=models.DateField(blank=True,null=True)
    endDate=models.DateField(blank=True,null=True)
    description=RichTextField()

    def __str__(self):
        return self.name

class Technology2(models.Model):
    name = models.ForeignKey(recentWork,related_name='technologies2', on_delete=models.CASCADE)
    techName=models.TextField(blank=True)
    def __str__(self):
        return self.name.name

class notification(models.Model):
    enabled=models.BooleanField(default=False)
    msg=models.TextField(null=True)
    btn=models.TextField(null=True)

class testimonial(models.Model):
    enabled=models.BooleanField(default=False)

class about(models.Model):
    about=RichTextField()
    logo=models.FileField(upload_to=photo_path,null=True)
