from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"id": 1, "title": "Test Item", "description": "This is a test"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Test Item", "description": "This is a test"}

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Test Item", "description": "This is a test"}

def test_update_item():
    response = client.put("/items/1", json={"id": 1, "title": "Updated Item", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Updated Item", "description": "Updated description"}

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Item deleted"}
