from fastapi.testclient import TestClient
from main import app  # Plus de problème E402

client = TestClient(app)


def test_create():
    response = client.post(
        "/items",
        json={"name": "TestItem", "price": 99.99, "in_stock": True},
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "message" in response.json()


def test_read_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert isinstance(response.json()["data"], list)


def test_read_only_item():
    # D'abord créer l'item
    client.post(
        "/items",
        json={"name": "SingleItem", "price": 15.0, "in_stock": False},
    )
    # Ensuite le récupérer
    response_all = client.get("/items")
    last_item = response_all.json()["data"][-1]
    item_id = last_item["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["id"] == item_id


def test_update():
    # Créer un item à mettre à jour
    client.post(
        "/items",
        json={"name": "UpdateMe", "price": 25.0, "in_stock": True},
    )
    response_all = client.get("/items")
    item_id = response_all.json()["data"][-1]["id"]

    # Mettre à jour l'item
    response = client.put(
        f"/items/{item_id}",
        json={"name": "UpdatedItem", "price": 30.0, "in_stock": False},
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Item mis à jour avec succès"


def test_delete():
    # Créer un item à supprimer
    client.post(
        "/items",
        json={"name": "DeleteMe", "price": 5.0, "in_stock": False},
    )
    response_all = client.get("/items")
    item_id = response_all.json()["data"][-1]["id"]

    # Supprimer l'item
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Item supprimé avec succès"

    # Vérifier qu’il a bien été supprimé
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["success"] is False
