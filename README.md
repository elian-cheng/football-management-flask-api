## FC Manager REST API

API service for management Football Clubs written on Flask REST API. With functionality managing teams and players.

Features:

- JWT authenticated
- Documentation is located via /swagger-ui/
- Implementing 4 models with many-to-many and many-to-one relationships
- Creating and updating teams and players of the club

### Installing using GitHub:

- Fork the project into your GitHub
- Clone it into your desktop

```
git clone https://github.com/elian-cheng/football-management-flask-api.git
cd football-management-flask-api
```

- Set up virtual environment

```
python3 -m venv venv
source venv/bin/activate # for Unix-based system
venv\Scripts\activate # for Windows
```

- Install requirements

```
pip install -r requirements.txt
```

- Open .env.example and change environment variables on yours! Rename the file from .env.example to .env

### Run API service

```
flask migrate
flask run
```

### Getting access instructions:

- Create a user via **/register/**
- Get access token via **/login/**
- Install **ModHeader** browser extension and create a Request header with the value **Authorization Bearer** `<Your access token>` to test with Swagger or use Postman

###Used tech stack:

- Flask
- SQLAlchemy
- SQLite
- Black & Flake8
- flask-smorest
- marshmallow
