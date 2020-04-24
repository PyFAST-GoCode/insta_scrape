# Welcome to Insta Scrape

Insta Scrape is a simple script adopted from [tikseniia](https://github.com/tikseniia/get-location-instagram/blob/master/script.py) in order to scrape location data from Instagram without the need for an API key.

Insta Scrape currently sits in Jupyter Notebook for ease of debugging and sharing with team members.


### Table of Contents

<!--ts-->
   * [Table of Contents](#table-of-contents)
   * [Set Up](#set-up)
<!--te-->

## **Set Up**

### Clone repo
```
https://github.com/nathangthomas/insta_scrape
```
### Run Jupyter Notebook
run `jupyter notebook` in your terminal to open repo in Jupyter Notebook.

### Run the Code
Click on the `Run` button to run the code.
This should create two new files:
  - insta_posts.json
  - location_data.json

Additionally, you can edit and rerun your code by clicking on `Kernel` then selecting `Restart & Run All` from the drop down menu. Or run individual blocks by selecting that block and clicking the `Run` button.


### Useful Terminal Commands

`pip freeze > requirements.txt` saves all requirements in a requirements.txt file
`export FLASK_APP=run.py` tells system which app to run
`flask run` starts the server


### File Structure
run.py: This is the application's entry point. We'll run this file to start the Flask server and launch our application.
config.py: This file contains the configuration variables for your app, such as database details.
app/__init__.py: This file intializes a Python module. Without it, Python will not recognize the app directory as a module.
app/views.py: This file contains all the routes for our application. This will tell Flask what to display on which path.
app/models.py: This is where the models are defined. A model is a representation of a database table in code. However, because we will not be using a database in this tutorial, we won't be needing this file.

### Database Configuration
Database hosted here => https://www.freemysqlhosting.net/

https://flask-mysqldb.readthedocs.io/en/latest/

https://www.google.com/search?q=how+to+use+flask-mysqldb&oq=how+to+use+flask-mysqldb&aqs=chrome..69i57j0.7153j0j4&sourceid=chrome&ie=UTF-8#kpvalbx=_giujXsZLx9u0Bq3eu8gI34

### Helpful Tutorial on Flask Applications
https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework
