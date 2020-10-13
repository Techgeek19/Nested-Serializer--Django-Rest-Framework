# Django-CRUD-Rest-Api with JWT Authentication

## Quick Start

``` bash
$ virtualenv env

# Activate venv
$ source env/bin/activate

# Install requirements
$ pip3 install -r requirements.txt

# Migrations
$ python manage.py makemigrations
$ python manage.py migrate

# Run Server (http://localhst:8000)
python3 manage.py runserver
```

## Example of a sample question: 
```
{
Text: “Explain Garbage collection in Java”,
Image: any sample image file
Tags: “moderate”, “java”
}
```

## APIs:
```
POST: This API should be able to add a single question to the system. To post a single question, the user will provide the text, image_file and some tags to the POST request.
PUT: Given the question id, this API will update the data related to that particular question. User can update text or image file for a particular question. A user can also add or remove some tags from the question.
GET: Given a single tag or a list of tags, this API will return a list of questions which have those tags. For example →

/GET
{
“tag”: “java”
}
Above mentioned sample get request will return all the questions which have the “java” tag in it.

/GET
{
“tag”: “java”, “simple”
}
Above mentioned sample get request will return all the questions which have both ‘java’ and “simple” tags in them.
```
