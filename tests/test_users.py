from jose import jwt
import pytest
from app import schemas
from app.oauth2 import ALGORITHM, SECRET_KEY


def test_root(client):
    res = client.get('/')
    print(res.json().get('message'))
    assert res.json().get('message') == 'Server is active'
    assert res.status_code == 200


def test_create_users(client, session):
    res = client.post("/users/", json={"email": "hello1234@gmail.com",
                      "password": "password123", "phone_number": "08102829960"})

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello1234@gmail.com"
    assert res.status_code == 201


def test_login_users(client, test_user):
    res = client.post("/login", data={"username": test_user["email"], "password": test_user["password"],
                                      })
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,
                         SECRET_KEY, algorithms=[ALGORITHM])
    id = payload.get("user_id")

    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ("wrongEmail@gmail.com", "password123", 403),
    ("hello123@gmail.com", "wrongpasswpeod", 403),
])
def test_incorrect_login(client, test_user, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password,
                                      })

    assert res.status_code == status_code
    # assert res.json().get('detail') == "Invalid Credentials"
