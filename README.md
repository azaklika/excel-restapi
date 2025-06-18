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


## OpenAPI Specification

The `openapi.json` file in this repository contains the API description in the OpenAPI v3 format. It was generated from the FastAPI application and can be used to explore the endpoints or generate API clients.

