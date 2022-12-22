from fastapi.testclient import TestClient
from main import app
from auth.models import User

client = TestClient(app)

# create a new user
def test_create_user(client,db_session): # antes sin client
    response = client.post(
        "/auth/users",
        #headers={"X-Token": "coneofsilence"},
        json={"name": "nico","last_name":"las"},
    )

    assert response.status_code == 201
    data = response.json()
    assert data['name'] == "nico"
    assert "id" in data
    # que efectivamente haya sido ingresado
    esta = db_session.query(User).filter(User.id==data['id']).first()
    assert esta



# try to create an user with invalida data
def test_create_user_invalid_data(client):
    response = client.post(
        "/auth/users",
        json={},
    )
    assert response.status_code == 422


# inserto un usuario y testeo que haya quedado bien
def test_get_single_user(client,add_user):
    
    # given
    user = add_user(name='nombre',last_name='df')
    
    # when
    response = client.get(f"/auth/users/{user.id}/")
    data = response.json()

    # then
    assert response.status_code == 200
    assert data["name"] == "nombre"
    for key in data.keys():
        assert key in ["id", "name", "last_name","groups"] # da error si no están todas las claves



# todos los usuarios
def test_get_all_users(client, add_user):
    # given
    user_one = add_user(name='nombre1',last_name='a1')
    user_two = add_user(name='nombre2',last_name='a2')
    
    # when
    response = client.get(f"/auth/users/")
    data = response.json()

    # then
    assert response.status_code == 200
    assert data[0]["name"] == user_one.name
    assert data[1]["name"] == user_two.name





#from .fixtures import add_user



# edit an user
def test_edit_user(client, add_user, db_session):
    # inserto un nuevo usuario
    user = add_user(name='nombre',last_name='apellido')
    # edito
    response = client.put(
        f"/auth/users/{user.id}/",
        json={"name": "nombreEditado","last_name": "apellidoEditado"},
    )
    data = response.json()
    assert response.status_code == 201
    assert data["name"] == 'nombreEditado'
    # que efectivamente lo haya editado en la base
    esta = db_session.query(User).filter(User.id==user.id).first()
    assert esta.name == 'nombreEditado'



# edit an user
def test_delete_user(client, add_user,db_session):
    # inserto un nuevo usuario
    user = add_user(name='nombre',last_name='apellido')
    temp = user.id
    # borro
    response = client.delete(
        f"/auth/users/{user.id}/",
    )
    assert response.status_code == 200
    # chequeo que efectivamente lo haya borrado
    esta = db_session.query(User).filter(User.id==temp).first()
    assert esta == None














# delete an user
# inserto,
# lo borro y me fijo que no esté en la base



#https://blog.j-labs.pl/index.php?page=2017/02/Given-When-Then-pattern-in-unit-tests




"""
from auth import models
def test_get_single_user(client, db_session,name='nombre',last_name='vblah'):
    db_user = models.User(name=name,last_name=last_name)
    db_session.add(db_user)
    db_session.commit()
    resp = client.get(f"/auth/users/{db_user.id}/")
    assert resp.status_code == 200
    assert resp.json()["name"] == "nombre"
"""




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