# Getting started with Python and Django REST API
# Follow these Steps using Windows, Linux or macOS Terminal

1. installing Python run : sudo apt-get install python3 on windows download python3 here https://www.python.org/downloads/
2. installing pip run : sudo apt install python3-pip (on windows skip this python comes with pip3)
3. installing django run : pip3 install django on windows use pip install django
4. installing django rest framework run : pip3 install djangorestframework on windows use pip not pip3
5. create a django project run : django-admin startproject django_rest_API 
6. go inside your project run : cd django_rest_API
7. create a django app run : python3 manage.py startapp MyApp
8. go inside your project to configure app setting run : cd django_rest_API
9. open settings.py with your IDE then add 'rest_framework', 'MyApp' inside INSTALLED_APPS please see https://github.com/Nxele/django_rest_API/blob/master/django_rest_API/settings.py
10. now go inside you app run : cd .. then cd MyApp
11. now open views.py using your IDE : copy and plaste this code and save https://github.com/Nxele/django_rest_API/blob/master/MyApp/views.py
12. now go back to django_rest_API and open url.py copy this code and paste it the save https://github.com/Nxele/django_rest_API/blob/master/django_rest_API/urls.py
13. then go back ones you must see manage.py run : cd .. then run ls
14. now start your webserver by running run : python3 manage.py runserver
15. then go to your broswer run : 127.0.0.1:8000/test_api
16. then download and install postman for testing your POST request download postnman here https://www.getpostman.com/downloads/
