# Fisupassi

This application allows users to submit their caught fish after registration. The application will have all the submitted caught fish, their species and their weight. The user can also check what they've caught, and modify or delete caught fish.

## Instructions
### Installation
- Cloning the project: 
```
$ git clone https://github.com/ilkkaluu/Fisupassi.git
```

- Move to the application directory
```
$ cd Fisupassi
```

- Create the Python-virtual environment: 
```
$ python -m venv venv
```

- Activate the virtual environment: 
```
$ source venv/bin/activate
```

- Install the flask-library: 
```
$ pip install flask
```

- Create the database "database.db": 
```
$ sqlite3 database.db < schema.sql
```

- Run the application: 
```
$ flask run
```
## Using the application
- A new user can register before logging in to the application.
- After registration and login. The user can add a fish and check their profile.
- After adding a caught fish and its information, the fish will be visible in the user's profile.
- The user can check what they've caught on their profile. They can also search for a specific fish to see how many they've caught.
## Features
- [x] User can register an account and log in.
- [x] User can add a catch and its information.
- [x] User can see what they've catched.

## Possible future features for the application
- More fish species and different ways of catching them.
- Leaderboards for users.
