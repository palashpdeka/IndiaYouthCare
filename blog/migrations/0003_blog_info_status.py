# Generated by Django 4.2.3 on 2023-08-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_info_date_alter_blog_info_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_info',
            name='status',
            field=models.CharField(default='a', max_length=1),
            preserve_default=False,
        ),
    ]
