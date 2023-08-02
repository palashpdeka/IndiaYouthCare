from django.db import models

class course_details(models.Model):
     course_name=models.CharField(max_length=100)
     course_poster=models.ImageField(upload_to="courses/",max_length=300,null=True,default=None)
     course_details=models.TextField(blank=True)

class registrant(models.Model):
     name=models.CharField(max_length=100)
     email=models.EmailField()
     phone=models.CharField(max_length=15)
     course=models.CharField(max_length=100)
     time=models.DateTimeField()
     comment=models.TextField()
