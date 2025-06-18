# CSV REST API

This repository contains a simple FastAPI application that exposes data from a CSV file over a REST API. Authentication is token-based via the `Authorization` header or `token` query parameter.

## Setup

All required Python packages are preinstalled in the Codex environment. To run the server manually, use:

```bash
uvicorn app:app --reload
```

## Example Usage

Assuming the server is running on `http://localhost:8000` and using the token `secret-token`:

- Retrieve all items:

  ```bash
  curl -H "Authorization: Bearer secret-token" http://localhost:8000/items
  ```

- Retrieve a single item:

  ```bash
  curl -H "Authorization: Bearer secret-token" http://localhost:8000/items/1
  ```

## Docker

To build the Docker image locally run:

```bash
docker build -t csv-rest-api .
```

Start the container exposing port 8000:

```bash
docker run -p 8000:8000 csv-rest-api
```

