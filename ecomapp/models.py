from django.db import models

# Create your models here.
class customerrole(models.Model):
   Group_Name= models.CharField(max_length=100)
   Group_Level= models.IntegerField()
   Status= models.CharField(max_length=8,choices=(("Active",'Active'), ("Deactive",'Deactive')))
   Image=models.ImageField(upload_to="models/", null=False, blank=False)

class managecustomer(models.Model):
   Group_Name= models.CharField(max_length=100)
   Group_Level= models.IntegerField()
   Status= models.CharField(max_length=8,choices=(("Active",'Active'), ("Deactive",'Deactive')))