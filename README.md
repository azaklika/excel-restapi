# CSV/XLSX REST API

This repository contains a simple FastAPI application that exposes data from a
CSV file over a REST API. It can also read data from an `xlsx` spreadsheet if a
`data.xlsx` file is present. In that case the file is converted on the fly using
`openpyxl`. Authentication is token-based via the `Authorization` header or
`token` query parameter.

The application now includes basic error handling. Any unexpected server errors
return a 500 status with a generic JSON response, while missing CSV files are
logged and result in an empty data set on startup.

## Setup

Install the required packages (if not already available) with:

```bash
pip install -r requirements.txt
```

To run the server manually, use:
=======
All required Python packages are preinstalled in the Codex environment. The
application looks for `data.csv` by default, falling back to `data.xlsx` if the
CSV file is missing. To run the server manually, use:

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
=======

## OpenAPI Specification

The `openapi.json` file in this repository contains the API description in the OpenAPI v3 format. It was generated from the FastAPI application and can be used to explore the endpoints or generate API clients.



## Running Tests

Tests are written with `pytest`. From the repository root run:

```bash
pytest
```

If `pytest` is not installed, you can add it via `pip install pytest`.
=======
