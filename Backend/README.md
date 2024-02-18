# Installation

Make sure that you are currently on the BACKEND directory.
Run docker compose build.
Then run docker compose up -d to start the application in detached mode.

## api routes

The api routes are specified by the openapi schema. You can access the routes via <http://localhost:80>
If docker is not working as expected, go to the debugging section. With the debugging section, you can access the api routes via <http://localhost:8000>
Once the localhost is started, you can access the api routes via <http://localhost:8000/docs>
This is an example of how the api routes are accessed using postman.
![alt text](<Screenshot 2024-02-18 at 2.14.16 PM.png>)

## Usage

MongoDB is running on port 27017.

## Debugging

Currently the application in docker is working as expected.
If the docker fails as a result of different port names of mongo in dp.py, it is possible to bypass it.
On top of running docker compose up -d, you will need to run the following commands to start the application and access the api.:

```cd app && uvicorn main:app --host 0.0.0.0 --port 8000 --reload```

Note that this means that the api routes will be accessible via <http://localhost:8000>

Alternatively, you can run the following command to start the application:

```cd app && python3 run.py```

## Closing the application

Run docker compose down to stop the application.
