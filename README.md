# RedisProject 
Project built using django-redis

### Requirements:
Python 3.10.12
Django 5.0.7
django-redis 5.4.0
django-redis-cache 3.0.1

### Steps to run this project:
1. Create virtual environment using python -m venv 'redisvenv' command. 
2. Activate virtual environment using source 'redisvenv/bin/activate' command. 
3. Install requirements using pip install -r requirements.txt command. 
4. Start project using django-admin startproject foodland command. 
5. Change directory to django project cd foodland. 
6. Start django application using command python manage.py startapp food_recipe. 
7. Add app name to setting.py file of django project in INSTALLED_APP 
8. Create templates for home page and to view recipe details. 
9. Run python manage.py migrations and migrate command to create database table. 
10. Create superuser using python manage.py createsuperuser command. 
11. Run server using python manage.py runserver command.
