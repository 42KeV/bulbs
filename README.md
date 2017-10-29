## What is Bulbs?
Bulbs is an open source message board developed in Python using the Pyramid Web Framework. 


## Requirements
* Python 3.4+
* Pyramid
* PostgreSQL

## How to install
* Install postgresql

CREATE DATABASE bulbs_db;
CREATE USER bulbs_user WITH PASSWORD 'lambdatest';
GRANT ALL PRIVILEGES ON DATABASE "bulbs_db" TO bulbs_user;

* `pip install -r requirements.txt` will install bulbs' dependencies.
* `python setup.py develop` will install the bulbs' package.
* `pserve development.ini --reload` will start the server
* point to /install to configure the database









* `pip install -r requirements.txt` - Install Bulbs' dependencies.

* Clone the repository, `git clone https://github.com/CrystallineEntity/bulbs.git`

`python setup.py develop` to install the package and dependencies
`pthon setup.py dbadmin` to configure database

If nothing exploded, you should be ready to rock and roll

`pserve development.ini --reload` to start the server in development mode and automatically reload files as you change them. It is not recommended to use the reload argument in production environments.



CREATE DATABASE bulbs_db;
CREATE USER bulbs_user WITH PASSWORD 'lambdatest';
GRANT ALL PRIVILEGES ON DATABASE "bulbs_db" TO bulbs_user;