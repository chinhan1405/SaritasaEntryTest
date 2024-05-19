# ABOUT

This project is about building an application to save your places' memories.

The application only requires Google Authentication to use.


# SETUP LOCAL HOST

1. Install all the required library in requirements.txt

```
pip install -r requirements.txt
```

2. Migrate models and create database

```
py my_memories/manage.py migrate
```

3. Run server on 127.0.0.1:8000

```
py my_memories/manage.py runserver
```

# REFERENCE

This application use an Map API from www.openstreetmap.org