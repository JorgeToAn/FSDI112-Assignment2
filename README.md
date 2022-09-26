# FSDI 112 - Assignment 2
This here presents a simple Django project which contains a home page and an about me page.

## Steps to follow for making a Django project
### Creating the project
1.	Create venv
2.	Activate venv
3.	Install Django
4.	Create project – Django-admin startproject config .
5.	Create app – python3 manage.py startapp <NAME>
6.	Make default migrations – python3 manage.py migrate
7.	Create super user – python3 manage.py createsuperuser
8.	Run server – python3 manage.py runserver

### Basic setup for settings
1.	Add your app to the list of installed apps.
2.	Add your ‘templates’ directory
3.	Set a time zone
4.	Set your static directories
5.	Add your app urls to the config urls.py