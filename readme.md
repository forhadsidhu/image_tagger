# AI enabled Image Searching in APP
This project is based on applying AI in image search functionality. For AI model we are using Hugging face and Langchain.They provide easy way to integrate promising deep learning model in the application.

# Initial System Design
![Figure](https://github.com/forhadsidhu/image_tagger/blob/main/image_tagger_backend_system_design.png)


## Installation

* Python >= 3.6
* Dependencies: ```pip install -r requirements.txt```
* Nodejs
* Reactjs

## Running
For backend
```uvicorn api.main:app --reload```
For Frontend
```npm start```


## Notes
uvicorn api.main:app --reload
set NODE_OPTIONS=--openssl-legacy-provider 

1. change alembic init file for database path
2. add backend model in alembic .env file

alembic init alembic
alembic revision --autogenerate -m "changes occured"
alembic upgrade head
