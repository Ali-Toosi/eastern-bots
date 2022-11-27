Getting Started
===============

Local Environment Setup
-----------------------

You will need docker and docker compose installed to run the project locally.

Once your requirements are installed, fork the repository and clone your fork.

To run the project, run::

    docker-compose -f local.yml up

This will create the app and db instances and once it's done, you should be able to see the admin page at
http://localhost/admin

For running ``manage.py`` commands use either::

    docker-compose -f local.yml run --rm django python manage.py ...

or::

    make manage cmd=<your command>


This will obtain a shell in the same container your app is running in and runs the command inside the container.

If you need to run these with the production settings, use ``-f production.yml`` instead.

Working on Documentation
------------------------

This project uses Sphinx with rST for its documentation engine. All docs are then published to https://eastern-bots.readthedocs.io/en/latest/

To see a live version of the docs on your local while making changes, run::

    docker-compose -f local.yml up docs

Then head to http://localhost:9000

Creating a New Bot
------------------

Create a new app in ``eastern_bots`` directory for your bot. You can use ``eastern_bots/bot_template`` as a template for your
bot with some basic configurations in place.
It's worth checking out :ref:`new_bots_requirements` page before working on your bot.
