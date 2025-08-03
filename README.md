# Fisupassi

This application allows users to compete against eachother in fishing. The application will give scores depending on the user's catch: type of the fish, size of the fish and so on. Users can also check what fishes others have caught and where they have caught them. Users can register and thus save their catches and scores on the database, or use the application unregistered to view the highscores.  

The application is not runable currently, although the documentation is on relatively good form. 

## Documentation
* [Application description]
* [Time used]
* [Architecture]
* [SRS]
## Releases
TBA - When the application is close to finishing  

## Instructions
### Installation
- Cloning the project: 
``````
$ git clone https://github.com/ilkkaluu/Fisupassi.git
```

- Move to the application directory

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

## Features
- [x] User can register an account and log in.
- [ ] User can add a catch and its information.
- [ ] User can see what they've catched.
