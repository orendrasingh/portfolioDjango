# Portfolio using Django
This project is made to use by anyone. You just need a server and required packages .
# Features of this project
1. You can enable or disable sections of portfolio.
2. You can easily update anything you want by browsing your django admin panel.
3. You can set priority to the elements. 
   For example : If you want to set some of your project at first position in project section then you can set priority 1 in the field of that project.
5. Latest UI.
6. Responsive layout.
7. Meta tags information can be updated easily.
8. Free to use no license needed.

# How you can support 
1. You can suggest new features and create issues regarding that.
2. You can make changes in codebase and can create pull request by creating new branch with describing all the changes you made.

# Installation Guide
1. Development Environment setup on windows/linux.
2. Production Environment setup on Server using apache/nginx.

- ``` $ Fork and clone this repo. ```
- ```$ Rename demo_env.py file with env.py and replace all the credentials with your credentials```
- ``` Development Environment Guide ```<br><br>
### For Linux Users
- ``` sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib  ``` 
- ``` $ pip3 install virtualenv ```
- ``` $ virtualenv name_of_your_virtual_environment ```
- ``` $ source name_of_your_virtual_environment/bin/activate ```
- ``` $ cd portfolioDjango```
- ``` $ pip3 install -r requirements.txt ```
- ``` $ python manage.py makemigrations ```
- ``` $ python manage.py migrate ```
- ``` $ python3 manage.py createsuperuser  ```               ```  //create the superuser for the project.```
- ``` $ python3 manage.py runserver ```                       ``` //running the server..ohh yes it is working.```
- ``` $ now browse your localhost/admin and create some enteries like your profile, about, popup, Popup, Enable_Disable sections. It's madatory to create only 1 enteries in each of these sections and if you want to change information in those sections just edit recent enteries you created. ```

### For Windows Users

- ``` $ pip install virtualenv ```
- ``` $ py -m venv name_of_your_virtual_environment ```
- ``` $ cd venv\Scripts ```
- ``` $ activate ```
- ``` $ cd.. cd..  ```
- ``` $ cd portfolioDjango ```
- ``` $ pip install -r requirements.txt ```
- ``` $ python manage.py makemigrations ```
- ``` $ python manage.py migrate ```
- ``` $ python3 manage.py createsuperuser  ```               ```  //create the superuser for the project.```
- ``` $ python3 manage.py runserver ```                       ``` //running the server..ohh yes it is working.```
- ``` $ now browse your localhost/admin and create some enteries like your profile, about, popup, Popup, Enable_Disable sections. It's madatory to create only 1 enteries in each of these sections and if you want to change information in those sections just edit recent enteries you created. ```


### DATABASE SETUP

- Edit the database section of this project according to your database name , user and password.

### For using postgres as your database
- Install Postgres for your machine.
- Create postgres User, Database and password.
- User localhost as host and 5432 as port.
- Replace your database section with this format

``` Replace env file enteries like ```
- DATABASE_NAME="WITH YOUR DB NAME"
- DATABASE_HOST="WITH YOUR HOST ADDRESS"
- DATABASE_PORT="WITH YOUR PORT ADDRESS"
- DATABASE_USER="WITH YOUR DB USER"

 
 ### For using sqlite as your default Database
 
Replace database section with this it will automatically create your database and user and all other required things.
 ```
 # DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
 ```
 <br><br>
 -``` Remove following enteries from env file like or you can let it remain also. ```<br><br>
- DATABASE_NAME
- DATABASE_HOST
- DATABASE_PORT
- DATABASE_USER
                 
                 
# For production setup follow these 2 docs.

- Server setup using apache.
``` https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04 ```
- Server setup using nginx.
``` https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04 ```

# Suggested features you can add

- Add multiple template formats with using same database enteries to give users more number of options to present their portfolio.
