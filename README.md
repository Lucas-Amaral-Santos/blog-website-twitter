# BLOG WEBSITE TWITTER DJANGO

## FILE SYSTEM

The compressed file includes the Django code named blog_website. The project is placed inside the virtual environment named blogwebsite_env. The tree view of the files are displayed next:

blogwebsite_env
|	blogwebsite 		-> The Django Project\
|	|	.git\
|	|	blogwebsite\
|	|	news			-> App created for News\
|	|	registrar		-> App created for authentication\
|	|	static		-> placing the static files \
|	|	templates		-> generical templates that doesn’t belong to any app\
|	|	db.sqlite3		-> Database sqlite\
|	|	manage.py		-> File for executing Django functions\
|	|	migra_app.bat	-> Batch file for automatization the migrations\
|	|	requirements.txt	-> Requirements file for set the environment\
|	Include\
|	Lib\
|	Scripts\
|	pip-selfcheck.json\
|	pyvenv.cfg\

## SETUP INSTRUCTIONS

After unzipping the Project get into the root directory of the Project:

```
cd blogwebsite_env\blogwebsite
```

Activate environment:
```
..\Scripts\activate.bat
```
Install necessary packages:
```
pip install -r requirements.txt
```
Execute Project:
```
python manage.py runserver
```

## TESTING

Github is setup to execute tests as soon as as something is pushed to master branch.
It's executing tests on forms, models, views and urls.
You can see the specification inside the directory /blogwebsite/news/tests/.

## ACCESS

The projects has two users setup

1. Administrator
        username: admin
        password: admin
2. Author
        username: lucasamasan
        password: Elefate20@

## DOCKER
        You can find the Docker Repository on https://hub.docker.com/r/lucasamasan/blogwebsite-bix

        ```
        docker pull lucasamasan/blogwebsite-bix
        ```