# Fisupassi

This application allows users to submit their caught fish after registration. The application will have all the submitted caught fish, their species and their weight. The user can also check what they've caught, and modify or delete caught fish.

## Features
- [x] User can register an account and log in.
- [x] Registered user can add a catch and its information.
- [x] Registered user can see what they've caught on their profile page.
- [x] Registered user can modify and delete their caught fish on their profile page.
- [x] Registered user can search the database with a fish species or username.
- [x] Registered user can go to another user's profile and see their caught fish.
- [x] Registered user can leave a comment on another user's profile page.

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
### Running the application  
- Open the browser and go to http://127.0.0.1:5000 to see the application.
- Register an account and log in.
- On the front page you can navigate to your profile, highscores, search caught fish and usernames, and go to add a new fish.  
- From the listed fish after searching for fish and username, the user can go to another user's profile and add a comment.
- Profle page lists all the fish the user has caught. The user can also modify or delete the caught fish.

## Using the application
- A new user can register before logging in to the application.
- After registration and login. The user can add a fish and check their profile.
- After adding a caught fish and its information, the fish will be visible in the user's profile.
- The user can check what they've caught on their profile. They can also search for a specific fish to see how many they've caught.


