import os
import sys
import configparser

from bulbs.components import db
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_mako',
    'pyramid_debugtoolbar',
    'waitress',
    'pyramid_beaker',
    'bcrypt',
    'psycopg2'
    ]
    
setup(name='Bulbs',
      version='0.2dev',
      description='Bulbs is a free, highly customizable, minimal open source bulletin board.',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='John Murphy',
      author_email='john@yepperx.ca',
      url='',
      keywords='web pyramid pylons python internet forum yepperx bulletin board message',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="bulbs",
      entry_points="""\
      [paste.app_factory]
      main = bulbs:main
      """,
      )
