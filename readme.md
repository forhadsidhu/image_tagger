uvicorn api.main:app --reload
set NODE_OPTIONS=--openssl-legacy-provider 


---------------In backend folder----------------------------

1. change alembic init file for database path
2. add backend model in alembic .env file

alembic init alembic
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
