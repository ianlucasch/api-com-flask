from http import HTTPStatus
from sqlalchemy import func
from src.app2 import User, Role, db

def test_get_user_success(client):
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()

    user = User(username="john-doe", password="test", role_id=role.id)
    db.session.add(user)
    db.session.commit()

    response = client.get(f"/users/{user.id}")

    assert response.status_code == HTTPStatus.OK
    assert response.json == {"id": user.id, "username": user.username}

def test_get_user_not_found(client):
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()

    user_id = 1

    response = client.get(f"/users/{user_id}")

    assert response.status_code == HTTPStatus.NOT_FOUND

def test_create_user(client, access_token):
    role_id = db.session.execute(db.select(Role.id).where(Role.name == "admin")).scalar()
    payload = {"username": "user3", "password": "user3", "role_id": role_id}

    response = client.post("/users/", json=payload, headers={"Authorization": f"Bearer {access_token}"})

    assert response.status_code == HTTPStatus.CREATED
    assert response.json == {"message": "User created!"}
    assert db.session.execute(db.select(func.count(User.id))).scalar() == 2

def test_list_users(client, access_token):
    user = db.session.execute(db.select(User).where(User.username == "john-doe")).scalar()
    response = client.post("/auth/login", json={"username": user.username, "password": user.password})

    response = client.get("/users/", headers={"Authorization": f"Bearer {access_token}"})

    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        "users": [
            {
                "id": user.id,
                "username": user.username,
                "role": {
                    "id": user.role.id,
                    "name": user.role.name,
                },
            }
        ]
    }