# To Do App [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
## A Basic To-Do Web Application using Django Framework
### Features
- User Authentication - Users can register, login and logout
- Add, Edit, Mark tasks as Complete/Incomplete and Delete Tasks
- Created API End points to get the ```User Data``` and ```User Tasks```

### Steps to be followed for first time use
- Create an Environment variable `DJANGO_ENV=DEV` to run the app in local.
- Generate a secret key using the below code and save it to an Environment variable `SECRET_KEY`.
  ```python
  import secrets
  secret_key = secrets.token_hex()
  ```
- Install all the dependencies using the below command
  ```
  pip install -r requirements.txt
  ```
- Run the below command - This will create the tables (by the Model definition) in the Database
  ```
  python manage.py migrate
  ```
- Create an ```admin``` user by running these following command
  ```
  $ python manage.py createsuperuser
  ```
### API End Points

  - To get the User information - ```/api/profile_info/user=<Username>/```
  
  - To get the Tasks of a User - ```/api/user_tasks/user=<Username>/```


### Project Descriptions

There are many ways to create a To-Do app project with Python. One way is to build a command-line interface (CLI) application using Python and Typer, a relatively young library for creating powerful CLI applications in almost no time1. Another way is to create a web app using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design2.

In the first approach, you’ll learn how to build a functional to-do application with a Typer CLI in Python, use Typer to add commands, arguments, and options to your to-do app, and test your Python to-do application with Typer’s CliRunner and pytest1. In the second approach, you’ll learn how to create a web app using Django, build a data model with one-to-many relationships, use the Django admin interface to explore your data model and add test data, design templates for displaying your lists, leverage class-based views to handle the standard database operations, and control the Django URL dispatcher by creating URL configurations2.

Both approaches have their own advantages and can be used depending on your needs and preferences. You can find more detailed information about these projects by following the links provided
