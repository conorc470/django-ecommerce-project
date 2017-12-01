# Non-Fiction Summaries
**Ecommerce & Blog Web Application with User Authentication and Stripe Payments**

This Web App was built as a final project for the Code Institute's classroom bootcamp. 
It is a **fictional** Ecommerce site built with Python's *Django* framework - no template was used.

## Live Demo

**Follow this link to view deployed version of the web app https://conor-dev-summaries.herokuapp.com/**

## Built with 
1. Django
2. Python
2. HTML
3. CSS
4. Bootstrap
5. SQLite database

## Deployment / Hosting

This Project was deployed and is hosted on Heroku with automatic deploys from GitHub

## Databases / Static Files

When running locally, SQLite database was used & static and media files were stored locally. 
When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set 
up to host all the static files. settings.py file was amended for the database & static files 
to point to the online resources.

## Installation

Follow the below instructions to clone this project for Mac (commands will be slightly different for Windows)

1. Go to folder you want to put the cloned project in your terminal & type:
    `$ git clone https://github.com/conorc470/django-ecommerce-project.git`
2. Create & Activate a new Virtual Environment in terminal:
    Create: `$ python3 -m venv ~/virtualenvs/name_of_environment`
    Activate: `$ source ~/virtualenvs/name_of_environment/bin/activate`
3. Install the project dependancies:
    `$ pip install -r requirements.txt`
4. Create env.sh file at the top level (this will contain all sensitive information)
    **MAKE SURE IT IS IN THE .gitignore FILE**
5. Copy the following into the env.sh file:
```
#!/bin/sh

export SECRET_KEY=''
export DEBUG='True'

export STRIPE_PUBLISHABLE_KEY=''
export STRIPE_SECRET_KEY=''
```

* A new SECRET_KEY can be generated [here](https://www.miniwebtool.com/django-secret-key-generator/)
* Set up an account with Stripe [here](https://stripe.com/gb) & input STRIPE_PUBLISHABLE_KEY & STRIPE_SECRET_KEY 

6. Go to settings.py, change the following(lines 177-205):

```
# TO RUN LOCALLY HAVE THESE TWO UNCOMMENTED #

# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'


# TO RUN ON HEROKU HAVE THESE UNCOMMENTED #

AWS_S3_OBJECT_PARAMETERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

```

To this:

```
# TO RUN LOCALLY HAVE THESE TWO UNCOMMENTED #

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# TO RUN ON HEROKU HAVE THESE UNCOMMENTED #

# AWS_S3_OBJECT_PARAMETERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
#        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#        'CacheControl': 'max-age=94608000',
#    }
#
# AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')
# AWS_S3_REGION_NAME = 'eu-west-1'
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# 
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#
# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
#
# MEDIAFILES_LOCATION = 'media'
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

```

7. Also in settings.py change the following:
```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
```

To this:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
```
8. In the terminal:
    `$ python manage.py migrate` - this will apply migrations to your local sqlite database
    `$ python manage.py createsuperuser` - this will create admin support
    `$ python manage.py runserver` - should say starting development server..
9. Go to your browser & type '127.0.0.1:8000' in the address bar
10. The App should run on your browser - note that there will be no products/blog posts as you are running off your own blank database
11. Log in to the admin panel by going to '127.0.0.1:8000/admin' & log in using the credentials you created for the superuser
12. You can add products from here