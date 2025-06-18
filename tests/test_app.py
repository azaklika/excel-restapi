import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
TOKEN = "secret-token"


def test_get_items_success():
    response = client.get("/items", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0]["id"] == 1


def test_get_item_success():
    response = client.get("/items/2", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 2
    assert data["name"] == "Item B"


def test_get_item_not_found():
    response = client.get("/items/999", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 404


def test_missing_token():
    response = client.get("/items")
    assert response.status_code == 401
