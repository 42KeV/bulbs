## What is Bulbs?
Bulbs is an open source message board developed in Python using the Pyramid Web Framework. 


## Requirements
* Python 3.4+
* Pyramid
* PostgreSQL

## How to install

* `pip install -r requirements.txt` - Install Bulbs' dependencies.

* Clone the repository, `git clone https://github.com/mystogan2000/bulbs.git`

`python setup.py develop` to install the package and dependencies
`pthon setup.py dbadmin` to configure database

If nothing exploded, you should be ready to rock and roll

`pserve development.ini --reload` to start the server in development mode and automatically reload files as you change them. It is not recommended to use the reload argument in production environments.
