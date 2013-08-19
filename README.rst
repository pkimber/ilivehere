ilivehere
*********

Django application

Install
=======

Virtual Environment
-------------------

Note: replace ``patrick`` with your name (checking in the ``example`` folder to make sure a file
has been created for you).

::

  mkvirtualenv dev_ilivehere
  pip install -r requirements/local.txt

  echo "export DJANGO_SETTINGS_MODULE=example.dev_patrick" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

  add2virtualenv ../base
  add2virtualenv ../login
  add2virtualenv .
  deactivate

To check the order of the imports:

::

  workon dev_ilivehere
  cdsitepackages
  cat _virtualenv_path_extensions.pth

Check the imports are in the correct order e.g:

::

  /home/patrick/repo/dev/app/ilivehere
  /home/patrick/repo/dev/app/login
  /home/patrick/repo/dev/app/base

Testing
=======

Using ``pytest-django``:

::

  workon dev_ilivehere
  find . -name '*.pyc' -delete
  py.test

To stop on first failure:

::

  py.test -x

Usage
=====

::

  workon dev_ilivehere
  django-admin.py syncdb --noinput
  django-admin.py migrate --all --noinput
  django-admin.py demo_data_login
  django-admin.py demo_data_ilivehere
  django-admin.py runserver

Release
=======

To release the application:

::

  fab -f fabric/release.py dist:prefix=pkimber,pypirc=dev
  git push -u origin master

To check the contents of the distribution:

::

  tar -ztvf dist/pkimber-ilivehere-0.1.0.tar.gz
