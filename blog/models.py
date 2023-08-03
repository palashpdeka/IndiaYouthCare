from django.db import models

class blog_info(models.Model):
    name=models.CharField(max_length=100)
    comment=models.TextField()
    social_media=models.CharField(max_length=100) 
    link=models.URLField(max_length=300)
    date=models.DateField()
    time=models.TimeField()
    image=models.ImageField(upload_to="blog_images/",max_length=300,null=True,default=None)