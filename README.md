# Deploy with python anywhere


#### In Bash
```bash
* mkvirtualenv --python=python3.5 myproj
* pip install -U Django==2.2.10
* which django-admin.py
* git clone [FILENAME]
*Do the Django STUFF  ----> Migrate, CreateSupruser
```

#### In Web

* click on add a new App
* click on Next
* click on Django 
* click on Python --version
* Go Back to manual configuration [ we already have an app ]
* click on next



### Now You are in Web

* Go to virtual env
* type /home/[username]/.virtualenvs/[projet name set for virtualenv]
* source code enter the dirname where proj is located


### WSGI conf file 

* delete hello_world code
* uncomment
42, 43, 47, 48, 49, 60, 61	 

* change path to yours
* os.chdir(path)
* os.environ.setdefault("DJANGO_SETTINGS_MODULE", "[filename].settings")
* import django
* django.setup()



### WSGI static files
* add /static/admin   /home/[username]/.virtualenvs/[name of virtaulenv]/lib/python[version]/site-packages/django/contrib/admin/static/admin 
* Go to files setting change allowed_host=[username.pythonanywhere.com]
* debug mode to false
* add /static  go to file and copy from top

