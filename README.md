# **PERSONAL ASSISTANT**
###### goit python web group project - group № 2

------------
**Description and instructions for working with Personal Helper**

**The personal assistant can:**
- registration and authorization user;
- creating, editing, deleting and previewing contacts in the phonebook, search for contacts by name, number and email;
- creating, editing, deleting and previewing notes, search notes by name and description;
- creating and deleting tags, search notes by tag;
- news monitoring;
- save and delete files, search for files by category;
- personal user account with the ability to change the name and password.


### Installation

To install this personal assistant you need to have python 3.10.
We can launch Personal Helper in two ways.

The first with python:
- Install git,
- Copy the repository to your computer with command <code>git clone https://github.com/Iabellavita/Personal-Helper-Web</code> ,
- Change directory to personal-helper-web,
- Install Docker and execute command setup PosrgreSQL in conteiner with help command: <br>
<code>docker run --name <cont_name> -p 5432:5432 -e POSTGRES_USER=<user_db> -e POSTGRES_PASSWORD=<pass_db> -e POSTGRES_DB=<db_name_1> -d postgres</code>
- Create .env file and fill values (DATABASE_URL=<code>postgres://<user_db>:<pass_db>@localhost:5432/<db_name></code>, DEBUG=True, SECRET_KEY=, ALLOWED_HOSTS=)
- Install requirements.txt with command <code>pip install -r requirements.txt</code>,
- Start the server with <code>python manage.py runserver</code>,
- Then go to 127.0.0.0:8000 and enjoy the functions of a personal assistant. 😊

The second with docker:
- Install Docker Desktop and launch him,
- Install git,
- Copy the repository to your computer with command <code>git clone https://github.com/Iabellavita/Personal-Helper-Web</code>,
- Change directory to personal-helper-web,
- Open terminal in directory with Personal Helper and enter this command <code>docker-compose up --build</code>,
- If you already have a built project, enter <code>docker-compose up</code> to run it.


------------
