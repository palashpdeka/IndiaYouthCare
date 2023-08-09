from django.db import models

class blog_info(models.Model):
    name=models.CharField(max_length=100)
    comment=models.TextField()
    email=models.EmailField()
    social_media=models.CharField(max_length=100, null=True, default="Social Media") 
    link=models.URLField(max_length=300)
    date=models.DateField()
    time=models.TimeField()
    #image=models.ImageField(upload_to="blog_images/",max_length=300,null=True,default=None)
    status=models.CharField(max_length=1) #a=approved, r=review