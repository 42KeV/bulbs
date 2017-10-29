## What is Bulbs?
Bulbs is an open source message board developed in Python using the Pyramid Web Framework. 


## Requirements
* Python 3.4+
* Pyramid
* PostgreSQL

## How to install
* `pip install -r requirements.txt` will install bulbs' dependencies.
* `python setup.py develop` will install the bulbs' package.
* `pserve development.ini --reload` will start the server
* go to /install in your web browser to configure the database

CREATE DATABASE bulbs_db;
CREATE USER bulbs_user WITH PASSWORD 'lambdatest';
GRANT ALL PRIVILEGES ON DATABASE "bulbs_db" TO bulbs_user;