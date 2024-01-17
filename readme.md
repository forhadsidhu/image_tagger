# AI enabled Image Searching in APP
This project is based on applying AI in image search functionality. For AI model we are using Hugging face and Langchain.They provide easy way to integrate promising deep learning model in the application.


# Installation

---------------In Frontend folder----------------------------
uvicorn api.main:app --reload
set NODE_OPTIONS=--openssl-legacy-provider 


---------------In backend folder----------------------------
1. change alembic init file for database path
2. add backend model in alembic .env file

alembic init alembic
alembic revision --autogenerate -m "changes occured"
alembic upgrade head
