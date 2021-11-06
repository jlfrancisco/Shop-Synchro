Synchro shop
============

The information stored by the app is a stock reading. In a shop, using a mobile application, an employee can for any reference, enter the current shortest expiry date present on the shelves.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/cookiecutter/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

:License: MIT

Basic Commands
--------------

Setting Up Your Local Installation
^^^^^^^^^^^^^^^^^^^^^

    $ python3.8 -m venv <virtual env path>

    $ source <virtual env path>/bin/activate

    $ pip install -r requirements/local.txt

    $ createdb synchro_shop -U postgres --password <password>

    $ export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/synchro_shop

    $ python manage.py migrate

    $ python manage.py runserver


Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Administration
^^^^^^

See detailed `Django administration`_.

.. _`Django administration`: https://blooming-mesa-26098.herokuapp.com/bjqRZhVJBLWzesMeskE7xotzZXZ6BENC

OpenAPI Doc
^^^^^^

See detailed `OpenAPI Doc`_.

.. _`OpenAPI Doc`: https://blooming-mesa-26098.herokuapp.com/docs/
