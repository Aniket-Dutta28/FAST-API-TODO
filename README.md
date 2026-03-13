# FastAPI Todo CRUD API

A simple Todo CRUD API built using FastAPI, SQLAlchemy, and MySQL.

## Features

* Create a new todo
* Read all todos
* Read a todo by ID
* Update a todo
* Delete a todo
* Connect FastAPI with MySQL database

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* MySQL
* Pydantic

## Project Structure

* `main.py` → FastAPI application and API routes
* `model.py` → Database table model
* `database.py` → Database connection setup

## API Endpoints

* `GET /` → Get all todos
* `GET /todo/{id}` → Get todo by ID
* `POST /todo` → Create new todo
* `PUT /todo/{id}` → Update todo
* `DELETE /todo/{id}` → Delete todo

## Run the Project

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pymysql
```

Start server:

```bash
uvicorn main:app --reload
```

Open in browser:

```bash
http://127.0.0.1:8000/docs
```

## Database

Make sure MySQL is running and update database credentials inside `database.py`.

## Purpose

This project is created for learning FastAPI CRUD operations with database integration.
