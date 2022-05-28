# Api Rest with Django Rest Framework
> This is an api rest example
> This project contains two services:
> - **api/blog**: CRUD operations for notes

## Installation, Enable your virtual environment before run this project
```bash
  pip install -r requirements.txt
```

## Create docker container to run the application
```bash
docker run -it --link postgres:postgres postgres psql -h postgres -U postgres
```
```bash
docker run -d  --link postgres:db -p 8080:8080 adminer
```
## Configure your .env file based on .env.example file, you can copy this template
