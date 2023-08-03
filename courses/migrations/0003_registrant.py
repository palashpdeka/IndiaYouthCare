# Generated by Django 4.2.3 on 2023-08-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_details_course_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('course', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
    ]