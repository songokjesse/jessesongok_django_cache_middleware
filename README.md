# jessesongok_django_cache_middleware
Django Middleware that takes urls from the settings file and caches them

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

```
- Django
- django-redis 
- Redis 
- loadtest

```

### Installing

A step by step series of examples that tell you how to get a development env running

######  Install redis on to your environment (sudo apt install redis-server && nmp install -g loadtest )

#Setup
1. Activate the virtual environment and install the project requirements.
```
- source venv/bin/activate
 
- pip install django
 
- pip install django-redis
 
- pip install djangorestframework
```
 

2. Clone the repository
```
- git clone https://github.com/songokjesse/jessesongok_django_cache_middleware.git
- cd jessesongok_django_cache_middleware
```

3. Migrations
```
- python manage.py migrate
```
4. Create superuser
```
- python manage.py createsuperuser
```

Configuring Redis on setting.py
```
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/',  #<== "enter your redis setting
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
 ```  

5. Run Server
```
- python manage.py runserver
```

6. Access the admin dashboard using 
```
- http://127.0.0.0:8000/admin
```
7. Access the REST API using 
```
- http://127.0.0.0:8000/api/v1/
```

8. Test the cache middleware
```
- loadtest -n 100 -k  http://localhost:8000/api/v1/test/
```

