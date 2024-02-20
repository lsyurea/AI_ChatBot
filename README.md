# AI_ChatBot

## Introduction

This is a simple AI chatbot that uses GPT 3 turbo engine to generate responses.
This project has a front-end folder and a back-end folder. The front-end folder contains the code for the user interface and the back-end folder contains the code for the server and the GPT 3 engine.

## Frontend

I will use NextJS with tailwindcss to build the frontend of the chatbot.

## Installation for the frontend

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Demo

### Our Chat

![Demo](<docs/chat.png>)

## Our Dashboard

![Demo](<docs/dashboard.png>)

## Backend

I will use Python >= 3.8, FastAPI, Pydantic Beanie and GPT 3 engine to build the backend of the chatbot.


## Installation for the backend

Download the project and navigate to the backend folder. 
Run ```docker compose build```.
Then run ```docker compose up -d``` to start the application in detached mode.

## api routes

The api routes are specified by the openapi schema. You can access the routes via <http://localhost:80>
If docker is not working as expected, go to the debugging section. With the debugging section, you can access the api routes via <http://localhost:8000>
Once the localhost is started, you can access the api routes via <http://localhost:8000/docs>
This is an example of how the api routes are accessed using postman.
![example](<Backend/docs/example.png>)
![example](<Backend/docs/exampletwo.png>)

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

Run ```docker compose down``` to stop the application.