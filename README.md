## So you want to run this Flask app from scratch?

It's easy! \*

\* (for certain definitions of easy)

This repo is a Flask application attempting to use the latest and greatest version of Python (3.4 at the time of this writing), Postgres/SQLite (9.4, 3.8.10 respectively) etc.

### To use:

Clone this repo, and cd into it:

    $ git clone <repo url> oktired
    $ cd oktired

Now let's set up a Python virtual environment like all the cool kids do:

    $ pyvenv venv

Now there's a new directory, `venv`, which'll contain all the miscellania specific to this project.

Let's activate the virtual environment using the `source` command:

    $ source venv/bin/activate

If this worked, you should find yourself in a command prompt with the environment name displayed in parenthesis, e.g. `(venv)`.

Delightfully, Python 3.4 comes with the package manager `pip`, which we'll use to go get the various libraries this project depends on to work:

    (venv) $ pip install -r requirements.txt

(note that *this* particular project is set up to use the Heroku platform and thus, needs postgresql installed on the system)

Now that we have all the dependencies loaded into the venv, let's run the management script and pass the arguments to initialize the database and environment:

    (venv) $ python manage.py db upgrade

You should now see a local sqlite data file `data-dev.sqlite`.

Here's where I should tell you how to set up some of the crucial metadata, such as the `roles` records that I expect to be present to manage privileges in the application, but I don't know how it's done yet.

But the good news is that the dev web application is ready to roll. The loader script simply needs to be called with the argument `runserver` like so:

    (venv) $ python manage.py runserver

This will start a locally accessible web server at http://127.0.0.1:5000. So, using your favorite web browser open the url and give the full-featured web application a spin!

Now, there are other things I haven't covered that're important to get *all* the features working, such as setting local environment variables to determine who the admin is, and what email account and password to use to send account registration emails, or how to actually use this in a production-esque environment like Heroku, but this'll have to do for starters.

Cheers!

-Kit
