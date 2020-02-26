# Welcome to The Opportunity Exchange Hiring Assignment

### Getting stared:  
**!! DO NOT CLONE THIS REPO- FORK ONLY !!**  
To get started, fork this repo and commit your solution to your repo.

The point of this assignment is to test your web based programming skills.

It is not required to complete this assignment using Django, but we have initiated a repository here using Django. Our code is based in Django so completing the assignment in Django will be considered a positive.

### Assignment

You are programmer for a Dog start-up trying to gather information from users about their dogs. You want to ask users 5 questions:

1. Do you walk your dog daily?  (BooleanField)
2. What is the breed of your dog? (CharField)
3. How old is your dog? (IntegerField)
4. What tricks does your dog know? Select all that apply: Sit, Fetch, Stay, Roll Over (MultipleChoiceField)
5. Email Address (CharField)

Output is a web page based application that takes input from a form and saves it to a database. Upon submit, the results are emailed to the user. Bonus points for making the data accessible via a REST API.


### TODO Checklist:
* Add a model to the database in _toe_hiring_2020/assignment/models.py_
* Create a form to add input to the new model in _toe_hiring_2020/assignment/forms.py_
* Display the form in _toe_hiring_2020/static/templates/index.html_
* Save results to db upon form submission in _toe_hiring_2020/assignment/views.py_
* Send email confirmation upon form submission in _toe_hiring_2020/assignment/views.py_
* (BONUS): Make results accessible via RESTFUL API


### Installing this repo
#### **Requirements**  
`pip install -r requirements.txt`

#### **Setting up the PostgreSQL db (optional)**  
This repo is set-up using postgreSQL. You are allowed to use another DB type such SQLite to implement your solution. Here are the instructions for installing postgresSQL.  

[_Download here._](https://www.postgresql.org/)

_On a MAC, run these commands:_     
Open Terminal and run the following commands:  
`psql` - runs psql   
`CREATE DB HIRING;` - creates DB    

_On a Windows, run these commands:_     
Install [pgadmin 4](https://www.pgadmin.org/download/pgadmin-4-windows/)  
Open pgadmin.  
In leftmost tab, open Servers > PostgreSQL 9.6 > Database.  
Right click on Database and click Create > Database.  
Write HIRING for Database. Click Save.

You have now created a postgres DB named Hiring. Now you will need to set your environment variables to match.

_Environment variables_   
To get django to connect to your postgressql db, you need to set the following variables:
- DATABASE_USER
- DATABASE_PASSWORD
- DATABASE_HOST
- DATABASE_PORT
You can set them in a env file or manually in _toe_hiring_2020/settings.py_ lines 80-84.

#### **Initiating the repo**  
Run the following commands to initialize the Django app.

`python manage.py migrate`  
`python manage.py runserver`  

The app should start and be viewable at: http://127.0.0.1:8000/  

### Grading criteria  
Code will graded in 3 equally important categories:
1. **Technicality** - Does the code run? Was it implemented correctly?
2. **Readability** - Do we understand the code the way it is written? Is candidate using a consistent naming convention for variables, functions, etc? Do they use of comments?
3. **Implementation** - Did implementation demonstrate understanding of computer science principles? Does applicant know how to correctly write functions, assign variables, etc? Do they understand Django concepts of models, forms and views?
