# IndiaYouthCare
```How to run the above project in your system```

1. Install "python" and "mysql" in your system.

2. To create a virtual environment-
> python -m venv virtual_env_name

3. To work on virtual env (for windows)-
> virtual_env_name/Scripts/activate

4. To install django-
> pip install django

5. To connect with database-  
***Go to settings.py and change credentials according to your system***

6. To use mysql with django-
> pip install mysqlclient

7. To make model migrations-
> python manage.py makemigrations  
> python manage.py migrate

8. To create superuser to access the admin panel-
> python manage.py createsuperuser

9. To run the server-
> python manage.py runserver
