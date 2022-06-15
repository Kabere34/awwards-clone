# awwards-clone


>[Kabere34](https://github.com/Kabere34)

# Description
This is an application that will allow a user to post a project he/she has created and get it reviewed by other users.
Users can sign up, login, view and post projects, search and rate other users' projects.
##  Live Link
 Click [View Site](https://zawadee.herokuapp.com/)  to visit the site

## Screenshot
###### Home page

<img src="">

 ###### user profile
 <img src="">

###### user credentials
 username- daisymacharia
 password- 0717579032

## User Story

* Sign in to the application to start using.
* Upload a project to the application.
* Search for different projects using their names.
* See your projects with all your details.
* Rate other users projects.



## Setup and Installation
To get the project .......

##### Cloning the repository:
 ```bash
 https://github.com/Kabere34/awwards-clone.git
```
##### Navigate into the folder and install requirements
 ```bash
cd insta-lite pip install -r requirements.txt
```
##### Install and activate Virtual
 ```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies
 ```bash
 pip install -r requirements.txt
```
 ##### Setup Database
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations awards
 ```
 Now Migrate
 ```bash
 python manage.py migrate
```
##### Run the application
 ```bash
 python manage.py runserver
```
##### Running the application
 ```bash
 python manage.py server
```
##### Testing the application
 ```bash
 python manage.py test
```
Open the application on your browser `127.0.0.1:8000`.


## Technology used

* [Python3.10.4](https://www.python.org/)
* [Django 4.0.5](https://docs.djangoproject.com/en/2.2/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information
If you have any question or contributions, please email me at [kabereivy@gmail.com]

## License

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Kabere34/Picture-Globe/blob/master/LICENSE)
* Copyright (c) 2019 **Ivy Kabere**
