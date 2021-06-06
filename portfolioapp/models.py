from django.db import models
import os
import random
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

# techlists={"Python":"Python",
# "Java":"Java",
# "HTML":"HTML",
# "CSS":"CSS",
# "Bootstrap":"Bootstrap",
# "PostgresSQL":"PostgresSQL",
# "Django":"Django",
# "PHP":"PHP",
# "MongoDB":"MongoDB",
# "Docker":"Docker",
# "Javascript":"Javascript",
# "jQuery":"jQuery",
# "ReactJS":"ReactJS",
# "NodeJS":"NodeJS",
# "SQLite":"SQLite",
# "REST_API":"REST API",
# "WordPress":"WordPress",
# "Drupal":"Drupal",
# "Magento":"Magento",
# "Figma":"Figma",
# "C":"C",
# "CPlusPlus":"C++"}

# Technologies=((techlists[i],techlists[i]) for i in techlists)
Technologies=(('Python', 'Python'),
('Java', 'Java'),
('HTML', 'HTML'),
('CSS', 'CSS'),
('Bootstrap', 'Bootstrap'),
('PostgresSQL', 'PostgresSQL'),
('Django', 'Django'),
('PHP', 'PHP'),
('MongoDB', 'MongoDB'),
('Docker', 'Docker'),
('Javascript', 'Javascript'),
('jQuery', 'jQuery'),
('ReactJS', 'ReactJS'),
('NodeJS', 'NodeJS'),
('SQLite', 'SQLite'),
('REST API', 'REST API'),
('WordPress', 'WordPress'),
('Drupal', 'Drupal'),
('Magento', 'Magento'),
('Figma', 'Figma'),
('C', 'C'),
('C++', 'C++'))
skillType=(("intermediate","Intermediate"),("expert","Expert"),("beginner","Beginner"))


def photo_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(15))
    return 'media/{basename}{randomstring}{ext}'.format(basename=basefilename, randomstring=randomstr, ext=file_extension)


class KeySkills(models.Model):
    skillname=models.TextField(blank=True)
    skillExperience=models.CharField(help_text="Enter year of experience or Intermediate, Beginner, and Expert.",blank=True,max_length=15)
    skillLevel=models.TextField(blank=True,max_length=15,help_text="Choose skill Level to show color accordingly",choices=skillType)
    priority=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.skillname
    
@receiver(post_save,sender=KeySkills)
def priority_update(sender,instance,created, **kwargs):
    if created:
        instance.priority=instance.id
        instance.save()

class ExtraSkills(models.Model):
    skillname = models.TextField(blank=True)
    skillExperience = models.CharField(help_text="Enter year of experience or Intermediate, Beginner, and Expert.",
                                       blank=True, max_length=15)
    skillLevel = models.TextField(blank=True, max_length=15, help_text="Choose skill Level to show color accordingly",
                                  choices=skillType)
    priority=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.skillname

@receiver(post_save,sender=ExtraSkills)
def priority_update(sender,instance,created, **kwargs):
    if created:
        instance.priority=instance.id
        instance.save()

class DegSkills(models.Model):
    skillname = models.TextField(blank=True)
    skillExperience = models.CharField(help_text="Enter year of experience or Intermediate, Beginner, and Expert.",
                                       blank=True, max_length=15)
    skillLevel = models.TextField(blank=True, max_length=15, help_text="Choose skill Level to show color accordingly",
                                  choices=skillType)
    priority=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.skillname
    
@receiver(post_save,sender=DegSkills)
def priority_update(sender,instance,created, **kwargs):
    if created:
        instance.priority=instance.id
        instance.save()

class Experience(models.Model):
    company=models.TextField(blank=True)
    logo = models.FileField(upload_to=photo_path, null=True)
    shortDescription=RichTextField(max_length=250,  null=True)
    position=models.TextField(blank=True)
    description=RichTextField()
    startDate=models.DateField(blank=True)
    endDate=models.DateField(blank=True,null=True)
    ispresent=models.BooleanField(default=False)
    priority=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.company

@receiver(post_save,sender=Experience)
def priority_update(sender,instance,created, **kwargs):
    if created:
        instance.priority=instance.id
        instance.save()

class Education(models.Model):
    college=models.TextField(blank=True)
    logo = models.FileField(upload_to=photo_path, null=True)
    shortDescription=RichTextField(max_length=250,  null=True)
    branch=models.TextField(blank=True)
    description=RichTextField()
    startDate=models.DateField(blank=True)
    endDate=models.DateField(blank=True,null=True)
    ispresent=models.BooleanField(default=False)
    priority=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.college

@receiver(post_save,sender=Education)
def priority_update(sender,instance,created, **kwargs):
    if created:
        instance.priority=instance.id
        instance.save()

class personalProjects(models.Model):
    logo = models.FileField(upload_to=photo_path, null=True)
    backgroundImage=models.FileField(upload_to=photo_path,null=True)
    name=models.TextField(blank=True)
    link=models.URLField(blank=True)
    startDate=models.DateField(blank=True,null=True)
    endDate=models.DateField(blank=True,null=True)
    description=RichTextField()
    shortDescription=RichTextField(max_length=175,  null=True)
    priority=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
@receiver(post_save,sender=personalProjects)
def priority_update(sender,instance,created, **kwargs):
    if created:
        instance.priority=instance.id
        instance.save()

class Technology(models.Model):
    name = models.ForeignKey(personalProjects,related_name='technologies', on_delete=models.CASCADE)
    techName=models.CharField(choices=Technologies,blank=True,max_length=100)
    def __str__(self):
        return self.name.name


class recentWork(models.Model):
    logo=models.FileField(upload_to=photo_path,null=True)
    backgroundImage=models.FileField(upload_to=photo_path,null=True)
    name=models.TextField(blank=True)
    link=models.URLField(blank=True)
    startDate=models.DateField(blank=True,null=True)
    endDate=models.DateField(blank=True,null=True)
    description=RichTextField()
    shortDescription=RichTextField(max_length=175,  null=True)
    priority=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
@receiver(post_save,sender=recentWork)
def priority_update(sender,instance,created, **kwargs):
    if created:
        instance.priority=instance.id
        instance.save()


class Technology2(models.Model):
    name = models.ForeignKey(recentWork,related_name='technologies2', on_delete=models.CASCADE)
    techName = models.CharField(choices=Technologies, blank=True, max_length=100)

    def __str__(self):
        return self.name.name

class notification(models.Model):
    enabled=models.BooleanField(default=False)
    msg=models.TextField(null=True)
    btn=models.TextField(null=True)

class about(models.Model):
    about=RichTextField()
    logo=models.FileField(upload_to=photo_path,null=True)
    email=models.EmailField(null=True)
    def __str__(self):
        return self.email


class userProfile(models.Model):
    name=models.CharField(max_length=100)
    greetingTxt=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    shortDescription=models.CharField(max_length=1000)
    resumeLink=models.URLField(help_text="Upload it somewhere like google drive and paste the link here.")
    logo=models.FileField(upload_to=photo_path,null=True)
    def __str__(self):
        return self.name

class socialIcon(models.Model):
    insta=models.URLField(null=True)
    yt=models.URLField(null=True)
    fb=models.URLField(null=True)
    twitter=models.URLField(null=True)
    github=models.URLField(null=True)
    linkedin=models.URLField(null=True)
    def __str__(self):
        return "Social Icons"


class companiesWorkedFor(models.Model):
    logo = models.FileField(upload_to=photo_path, null=True)
    url=models.URLField(null=True)
    name=models.CharField(max_length=150)
    priority=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    

@receiver(post_save,sender=companiesWorkedFor)
def priority_update(sender,instance,created, **kwargs):
    if created:
        instance.priority=instance.id
        instance.save()

class certification(models.Model):
    logo = models.FileField(upload_to=photo_path, null=True)
    url=models.URLField(null=True)
    name=models.CharField(max_length=150)
    priority=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
@receiver(post_save,sender=certification)
def priority_update(sender,instance,created, **kwargs):
    if created:
        instance.priority=instance.id
        instance.save()

class sectionEnableDisable(models.Model):
    testimonial=models.BooleanField(default=True)
    companies=models.BooleanField(default=True)
    aboutus=models.BooleanField(default=True)
    socialIcons=models.BooleanField(default=True)
    certification=models.BooleanField(default=True)

class endorsement(models.Model):
    name=models.CharField(max_length=100)
    subHeading=models.CharField(max_length=120,null=True)
    comment=models.TextField()
    image = models.FileField(upload_to=photo_path, null=True)
    priority=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
@receiver(post_save,sender=endorsement)
def priority_update(sender,instance,created, **kwargs):
    if created:
        instance.priority=instance.id
        instance.save()

class meta_info(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(null=True)
    tags=models.TextField()
    img = models.FileField(upload_to=photo_path, null=True)
    url=models.URLField()

    def __str__(self):
        return self.title
