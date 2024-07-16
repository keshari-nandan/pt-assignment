# PT Assignment

### Installation & Configuration
- Install the Docker Desktop and Start It
- Clone this repository in your local machine by typing ``. 
- Open the Terminal and navigate to the project folder.
- Run `docker volume create pesto_mysql_data` to create a docker volume in you machine. Required to persist the mysql data.
- Below will be your mysql connection details
```bash
MYSQL_HOST=127.0.0.1
MYSQL_USER=root
MYSQL_PASSWORD=Pesto&123
MYSQL_DB=pesto
MYSQL_PORT=3306
```
You do not need to change anything here, but if you would like to change the username, password or database name, you can modify it at this point in the `.env` file attached to this project. 