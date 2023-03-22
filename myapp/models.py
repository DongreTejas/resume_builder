from django.db import models

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100,default="anderson")
    phone = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    website=models.CharField(max_length=100)
    country=models.CharField(max_length=50,default="country")
    aboutyou=models.CharField(max_length=50,default="null")
    linkedin=models.CharField(max_length=50,default="username")
    github=models.CharField(max_length=50,default="username")
    company=models.CharField(max_length=50,default="null")
    company_exp=models.CharField(max_length=50,default="null")
    experience_title=models.CharField(max_length=50,default="null")
    hobbies=models.CharField(max_length=100,default="null")
    htmlskill=models.CharField(max_length=100,default="0")
    cssskill=models.CharField(max_length=100,default="0")
    pythonskill=models.CharField(max_length=100,default="0")
    javascriptskill=models.CharField(max_length=100,default="0")
    csskill=models.CharField(max_length=100,default="0")
    dbmsskill=models.CharField(max_length=100,default="0")
    codingskill=models.CharField(max_length=100,default="0")