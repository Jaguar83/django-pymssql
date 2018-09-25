django-pymssql
===================
*django-pymssql* is a fork of
`django-pyodbc-azure <https://github.com/michiya/django-pyodbc-azure>`__, a
`Django <https://www.djangoproject.com/>`__ Microsoft SQL Server external
DB backend that uses pymssql
`pymssql <http://www.pymssql.org/>`__ library. It supports
Microsoft SQL Server

*It is currently in alpha, so there are probably lots of bugs*

Features
--------

-  Supports Django 2.1
-  Supports any server supported by pymssql

Dependencies
------------

-  Django 2.1
-  pymssql 2.1 or newer

Installation
------------

1. Install pymssql and Django

2. Install django-pymssql 

3. Now you can point the ``ENGINE`` setting in the settings file used by
   your Django application or project to the ``'django_pymssql'``
   module path ::

    'ENGINE': 'django_pymssql'

Configuration
-------------

Standard Django settings
~~~~~~~~~~~~~~~~~~~~~~~~

The following entries in a database-level settings dictionary
in DATABASES control the behavior of the backend:

-  ENGINE

   String. It must be ``"django_pymssql"``.

-  NAME

   String. Database name. Required.

-  HOST

   String. SQL Server instance in ``"server"`` format.

-  PORT

   String. Server instance port.
   An empty string means the default port.

-  USER

   String. Database user name in ``"user"`` format.

-  PASSWORD

   String. Database user password.

-  AUTOCOMMIT

   Boolean. Set this to False if you want to disable
   Django's transaction management and implement your own.

and the following entries are also available in the TEST dictionary
for any given database-level settings dictionary:

-  NAME

   String. The name of database to use when running the test suite.
   If the default value (``None``) is used, the test database will use
   the name "test\_" + ``NAME``.

-  COLLATION

   String. The collation order to use when creating the test database.
   If the default value (``None``) is used, the test database is assigned
   the default collation of the instance of SQL Server.

-  DEPENDENCIES

   String. The creation-order dependencies of the database.
   See the official Django documentation for more details.

-  MIRROR

   String. The alias of the database that this database should
   mirror during testing. Default value is ``None``.
   See the official Django documentation for more details.

OPTIONS
~~~~~~~

Dictionary. Current available keys are:

-  query_timeout

   Integer. Sets the timeout in seconds for the database query.
   Default value is ``0`` which disables the timeout.


Example
~~~~~~~

Here is an example of the database settings:

::

    DATABASES = {
        'default': {
            'ENGINE': 'django_pymssql',
            'NAME': 'mydb',
            'USER': 'user',             
            'PASSWORD': 'password',
            'HOST': 'myserver',
            'PORT': '',
        },
    }
    

Limitations
-----------

Currently in alpha so many limitations may apply. Also,
much code has been ported from the home project, and many
of the features are untested.

Notice
------

This version of *django-pymssql* only supports Django 2.1.
