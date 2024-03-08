from unittest.mock import Mock

import pytest
from sqlalchemy import select

from src.models.models import User
# from tests.conftest import TestingSessionLocal
from src.conf import messages

user_data = {"username": "Steve", "email": "jobs@gmail.com", "password": "66677788"}

    
def test_signup(client, monkeypatch):
    mock_send_email = Mock()
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
    response = client.post("api/auth/signup", json=user_data)
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["username"] == user_data["username"]
    assert data["email"] == user_data["email"]
    assert "password" not in data
    assert "avatar" in data


# def test_signup_exist_user(client, monkeypatch):
#     mock_send_email = Mock()
#     monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
#     response = client.post("api/auth/signup", json=user_data)
#     assert response.status_code == 409, response.text
#     data = response.json()
#     assert data["detail"] == messages.ACCOUNT_EXIST


# def test_login_not_confirmed_email(client):
#     response = client.post("api/auth/login",
#                            data={"username": user_data.get("email"), "password": user_data.get("password")})
#     assert response.status_code == 401, response.text
#     data = response.json()
#     assert data["detail"] == messages.EMAIL_NOT_CONFIRMED
    
# @pytest.mark.asyncio
# async def test_login(client):
#     async with TestingSessionLocal() as session:
#         current_user = await session.execute(select(User).where(User.email == user_data.get("email")))
#         current_user = current_user.scalar_one_or_none()
#         if current_user:
#             current_user.confirmed = True
#             await session.commit()

#     response = client.post("api/auth/login",
#                            data={"username": user_data.get("email"), "password": user_data.get("password")})
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert "access_token" in data
#     assert "refresh_token" in data
#     assert "token_type" in data


# def test_login_wrong_password(client):
#     response = client.post("api/auth/login",
#                            data={"username": user_data.get("email"), "password": "idontknow"})
#     assert response.status_code == 401, response.text
#     data = response.json()
#     assert data["detail"] == messages.INVALID_PASSWORD


# def test_login_wrong_email(client):
#     response = client.post("api/auth/login",
#                            data={"username": "email@gmail.com", "password": user_data.get("password")})
#     assert response.status_code == 401, response.text
#     data = response.json()
#     assert data["detail"] == messages.INVALID_EMAIL

# def test_confirmed_email_invalid_token(client):
#     response = client.get("api/auth/confirmed_email/{token}")
#     assert response.status_code == 422, response.text
#     data = response.json()
#     assert data["detail"] == messages.INVALID_TOKEN
    

# @pytest.mark.asyncio
# async def test_confirmed_email(client, get_email_token):
    # async with TestingSessionLocal() as session:
    #     current_user = await session.execute(select(User).where(User.email == user_data.get("email")))
    #     current_user = current_user.scalar_one_or_none()
    #     if current_user:
    #         current_user.confirmed = True
    #         await session.commit()
    
            
    # token = get_email_token
    # headers = {"Authorization": f"Bearer {token}"}
    # response = client.get("api/auth/confirmed_email/{token}", headers=headers)
    # assert response.status_code == 200, response.text
    # data = response.json()
    # assert "access_token" in data
    # # assert data["access_token"] == token
    # assert data["detail"] == messages.EMAIL_CONFIRMED