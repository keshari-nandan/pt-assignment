# PT Assignment

### Installation & Configuration
- Install the Docker Desktop and Start It
- Clone this repository in your local machine by typing `https://github.com/keshari-nandan/pt-assignment.git`. 
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

### Building the Project
- We can start building our projects by running `docker-compose build`
- One build is done, run `docker-compose up` to start the services. Leave this terminal open to check the logs.
- To stop the services you can press `Ctrl + C` - (Control + C)

# Accessing the Docker Containers
- FastAPI Application Status [http://localhost:8000](http://localhost:8000)
- API Documentation [http://localhost:8000/docs](http://localhost:8000/docs)
- Database Access [http://localhost:8080](http://localhost:8080) - use the above detail to log in.
- Mailpit [http://localhost:8025](http://localhost:8025)


# API Details
This project app's contains 3 api groups
1. Users
2. Auth
3. Tasks

### Users API Group
This group has 4 api as below - 
- Register User - This api is used to create a new user account.
- Verify User Account - This api is used to verify the user email and then activate his/her account for login.
- Fetch User (Authenticated) - This api is used the fetch the authenticated user details.
- Get User Info - This api is used to fetch any user details with user_id.

### Auth API Group
This group also has 4 api as below - 
- User Login - This api is used to fetch the user login token. This token (Bearer Token) is further passed in the header with protected apis.
- Refresh Token - This api can be used to generate a new login token with the help of refresh token.
- Forgot Password - This api is used to trigger a forgot password request.
- Reset Password - This api is used to reset the user password.

### Task API Group
Task API group has 5 api as below - 
- Create Task  - This api is used to create a new user task in the system.
- Update Task - This api is used to update an existing task data in the system.
- Delete Task - This api is used to delete a user task in the system.
- Get Task By ID - This api can be used to fetch the task detail by ID. 
- Get All User Task - This api can be used to fetch all the task related to the logged-in user.


### Sorting the Task List
`Get All User Task` api support the sorting functionality by field/column name. Below is an example of sorting the tasks by title in descending order.
```bash
http://127.0.0.1:8000/tasks?sort=title:asc
```

### Searing the Matching Task
`Get All User Task` api support the search functionality. At the moment it support searching only in title column but this can extended to other columns too. Below is an example of search.
```bash
http://127.0.0.1:8000/tasks?q=pesto
```


### Filtering the Task
`Get All User Task` api support the filtering functionality by status. Below is an example of filter.
```bash
http://127.0.0.1:8000/tasks?status=Done
```


### Searching, Sorting & Filtering Together
```bash
http://127.0.0.1:8000/tasks?q=pesto&status=Done&sort=titme:asc
```


# Additional Things

## Migrations
This project is integrated with ``Alembic`` to generate the migration files automatically based on the `SQLAlchemy Models` you define.
- To Generate the Migration From Model
```
docker-compose run fastapi-service /bin/sh -c "alembic revision --autogenerate -m "create my table table""
```
- To Apply the Migration to Database
```
docker-compose run fastapi-service /bin/sh -c "alembic upgrade head"
```
- To Revert last applied migration
```
docker-compose run fastapi-service /bin/sh -c "alembic downgrade -1"
```

## Unit/API Testing
This project is integrated with `pytest` to do the unit testing. During the unit
This project includes the API testing, and covers all the user authenticated and authorization apis. This can further be extended to cover the task related apis as well. 
- Use the below command to run the test cases - 
```
docker-compose run fastapi-service /bin/sh -c "pytest"
```

- Display the info logs in the test
```
docker-compose run fastapi-service /bin/sh -c "pytest --log-cli-level=INFO"
```

- Running a single test file
```
docker-compose run fastapi-service /bin/sh -c "pytest tests/test_folder/test_file.py"
```


# Notes
- This project also includes the email functionality and can send email when user account is created, forgot password request etc. But at the moment is disabled/commented.
- Since email functionality is disabled, a new user account is activated by default.
- Please use the Swagger to check the API related details. 
- Thanks.