from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_create_user():
    response = client.post(
        "/auth/users",
        #headers={"X-Token": "coneofsilence"},
        json={"name": "user"},
    )
    assert response.status_code == 201
    assert response.json()['name'] == "user"







#https://cosasdedevs.com/posts/tests-fastapi/







"""
def test_create_user():
    response = client.post(
        "/users/",
        json={"email": "deadpool@example.com", "password": "chimichangas4life"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert data["id"] == user_id
"""