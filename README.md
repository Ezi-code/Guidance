# Guidance and Councelling Booking App

This project is designed to solve the problem of continuous check in witht the guidance and coucelling unit of aamusted for availability before one can have a conselling session with them.

the project is built with python `Django` framework.

It is cuurently under development. If you wish to contribute to this project, reach out to <ezrayendau2000@gmail.com> with refrence to this project in you mail subject.

# Get the server runnning

- Run

```bash
pip install -r requirements.txt
```

on your terminal to install the project requirements on you device. It will be nice to create a virtual environment before this step, but if yiu don't want to, it's totally fine.

- Run

```bash
python manage.py migrate
```

to migrate and create the database schema.
You man also need to run

```bash
python manage.py makemigrations
```

before running migrate command in some cases to get the database schemas ready for migration.

- Create a superuser accounts for testing purposes

```bash
python manage.py creatsuperuser
```

and follow the prompts to create a superuser accoutns .

# Note

- The app is still under the stage of development
- Anyone can contribute, following best practices of opensource contribution guidelines.
- All tasks that needs to be done are stated in TODO.md file
