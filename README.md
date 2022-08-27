# How to Install and Run this project?
1. Install Git Version Control 

2. Install Python Latest Version 

3. Install Pip (Package Manager) 

# Installation
1. Create a Folder where you want to save the project

2. Create a Virtual Environment and Activate

Install Virtual Environment First

``` $  pip install virtualenv ```

``` $  python -m venv venv ```

Actiavte Virtual Enviroment

```$  source venv/scripts/activate```

3. Clone this project

```$  git clone https://github.com/vijaythapa333/django-student-management-system.git```

Then, Enter the project

```$  cd django-student-management-system```

4. Install Requirements from 'requirements.txt'

```$  pip install -r requirements.txt```

5. Add the hosts

- Got to settings.py file
- Then, On allowed hosts, Add [‘*’].

```ALLOWED_HOSTS = ['*']```

No need to change on Mac.

6. Now Run Server

```$ python manage.py runserver```

7. Login Credentials

Create Super User (HOD)

```$  python manage.py createsuperuser```
