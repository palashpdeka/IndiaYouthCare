# Generated by Django 4.2.3 on 2023-08-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_info_email_alter_blog_info_social_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_info',
            name='social_media',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
