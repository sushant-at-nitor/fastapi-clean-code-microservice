# FastAPI Clean Code Microservice
This is a sample project that demonstrates how to build a microservice using FastAPI framework and PostgreSQL database. It follows the principles of clean architecture and hexagonal design. The project consists of two services: movies and casts, each with its own REST API and database. The services communicate with each other using HTTP requests.

## Features
- CRUD operations for movies and casts
- Pagination, filtering, and sorting for movies
- Validation and error handling
- Unit testing and code coverage
- Docker and docker-compose support
- Nginx reverse proxy
- OpenAPI documentation

## Requirements
- Python 3.9+
- Pipenv
- PostgreSQL
- Docker and docker-compose
- Installation

## Clone the repository and install the dependencies using pipenv:
```
git clone https://github.com/sushant-at-nitor/fastapi-clean-code-microservice.git
cd fastapi-clean-code-microservice
pipenv install --dev
```

Create a .env file in the root directory and add the following environment variables:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_SERVER=db
POSTGRES_PORT=5432
POSTGRES_DB=fastapi
API_PORT=8000
API_HOST=0.0.0.0
```

## Usage
To run the application locally, use the following command:
```
pipenv run uvicorn main:app --reload
```
To run the application using docker-compose, use the following command:
```
docker-compose up -d --build
```

To access the API documentation, visit http://localhost:8000/docs for movies service and http://localhost:8001/docs for casts service.

To access both services using a single host address, visit http://localhost/api/movies and http://localhost/api/casts.

## Testing
To run the tests and generate the coverage report, use the following command:
```
pipenv run pytest --cov-report xml --cov .
```

## License
None
