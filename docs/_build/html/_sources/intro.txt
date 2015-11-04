************
Installation
************

Clone Bulbs using git or download the .zip::

 git clone https://github.com/galileo94/bulbs.git

https://github.com/galileo94/bulbs/archive/master.zip

It is advised that you switch into a virtual environment now, as we will be installing the package and dependencies::

   python setup.py develop

Configuring the database::

   python setup.py configure

All done. If you encounter any errors please file a bug report on github.



.. autofunction:: bulbs.auth.controller.generate_password

.. autofunction:: bulbs.auth.controller.authorize
