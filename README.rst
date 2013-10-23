======
Fabsvc
======

Fabsvc is a simple Django app to watch and control services on multi host.
With fabsvc, you can config/watch/start/stop your service in one web page.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "fabsvc" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'fabsvc',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^fabsvc/', include('fabsvc.urls')),

3. Run `python manage.py syncdb` to create the fabsvc models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a fabsvc config (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/fabsvc/ to participate in the fabsvc.
