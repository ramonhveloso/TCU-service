from datetime import datetime
import pytest

import pytest

@pytest.mark.asyncio
async def test_get_extra_expenses(use_test_client):
    # Criando um usuário
    signup_payload = {
        "username": "devMaster",
        "password": "jujuba",
        "email": "master@dev.com",
        "name": "dev",
    }
    signup_response = use_test_client.post("/api/v1/auth/signup", json=signup_payload)
    assert signup_response.status_code == 201

    # Logando com o usuário criado
    login_payload = {"username": "master@dev.com", "password": "jujuba"}
    login_response = use_test_client.post("/api/v1/auth/login", data=login_payload)
    assert login_response.status_code == 200

    access_token = login_response.json()["access_token"]
    # Requisição para obter todas as despesas extras
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo extra expenses
    json_request = {
        "amount": 100.00,
        "description": "teste",
        "date": datetime.now()
    }

    post_expenses_response = use_test_client.post("/api/v1/extra-expenses/", headers=headers, params=json_request)
    assert post_expenses_response.status_code == 201

    
    get_expenses_response = use_test_client.get("/api/v1/extra-expenses/", headers=headers)
    assert get_expenses_response.status_code == 200

@pytest.mark.asyncio
async def test_post_extra_expenses(use_test_client):
    # Criando um usuário
    signup_payload = {
        "username": "devMaster",
        "password": "jujuba",
        "email": "master@dev.com",
        "name": "dev",
    }
    signup_response = use_test_client.post("/api/v1/auth/signup", json=signup_payload)
    assert signup_response.status_code == 201

    # Logando com o usuário criado
    login_payload = {"username": "master@dev.com", "password": "jujuba"}
    login_response = use_test_client.post("/api/v1/auth/login", data=login_payload)
    assert login_response.status_code == 200

    access_token = login_response.json()["access_token"]
    # Requisição para obter todas as despesas extras
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo extra expenses
    json_request = {
        "amount": 100.00,
        "description": "teste",
        "date": datetime.now()
    }

    post_expenses_response = use_test_client.post("/api/v1/extra-expenses/", headers=headers, params=json_request)
    assert post_expenses_response.status_code == 201

@pytest.mark.asyncio
async def test_get_by_id_extra_expenses(use_test_client):
    # Criando um usuário
    signup_payload = {
        "username": "devMaster",
        "password": "jujuba",
        "email": "master@dev.com",
        "name": "dev",
    }
    signup_response = use_test_client.post("/api/v1/auth/signup", json=signup_payload)
    assert signup_response.status_code == 201

    # Logando com o usuário criado
    login_payload = {"username": "master@dev.com", "password": "jujuba"}
    login_response = use_test_client.post("/api/v1/auth/login", data=login_payload)
    assert login_response.status_code == 200

    access_token = login_response.json()["access_token"]
    # Requisição para obter todas as despesas extras
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo extra expenses
    json_request = {
        "amount": 100.00,
        "description": "teste",
        "date": datetime.now()
    }

    post_expenses_response = use_test_client.post("/api/v1/extra-expenses/", headers=headers, params=json_request)
    assert post_expenses_response.status_code == 201

    extra_expense_id = post_expenses_response.json()["response"]["id"]
    get_expenses_response = use_test_client.get(f"/api/v1/extra-expenses/{extra_expense_id}", headers=headers)
    assert get_expenses_response.status_code == 200

@pytest.mark.asyncio
async def test_put_by_id_extra_expenses(use_test_client):
    # Criando um usuário
    signup_payload = {
        "username": "devMaster",
        "password": "jujuba",
        "email": "master@dev.com",
        "name": "dev",
    }
    signup_response = use_test_client.post("/api/v1/auth/signup", json=signup_payload)
    assert signup_response.status_code == 201

    # Logando com o usuário criado
    login_payload = {"username": "master@dev.com", "password": "jujuba"}
    login_response = use_test_client.post("/api/v1/auth/login", data=login_payload)
    assert login_response.status_code == 200

    access_token = login_response.json()["access_token"]
    # Requisição para obter todas as despesas extras
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo extra expenses
    json_request = {
        "amount": 100.00,
        "description": "teste",
        "date": datetime.now()
    }

    post_expenses_response = use_test_client.post("/api/v1/extra-expenses/", headers=headers, params=json_request)
    assert post_expenses_response.status_code == 201
    
    json_request = {
        "amount": 150.00,
        "description": "atualizado",
        "date": str(datetime.now())
    }

    extra_expense_id = post_expenses_response.json()["response"]["id"]
    put_expenses_response = use_test_client.put(f"/api/v1/extra-expenses/{extra_expense_id}", headers=headers, json=json_request)
    assert put_expenses_response.status_code == 200

    get_expenses_response = use_test_client.get(f"/api/v1/extra-expenses/{extra_expense_id}", headers=headers)
    assert get_expenses_response.status_code == 200
    assert get_expenses_response.json()["amount"] == 150.00
    assert get_expenses_response.json()["description"] == "atualizado"

@pytest.mark.asyncio
async def test_delete_by_id_extra_expenses(use_test_client):
    # Criando um usuário
    signup_payload = {
        "username": "devMaster",
        "password": "jujuba",
        "email": "master@dev.com",
        "name": "dev",
    }
    signup_response = use_test_client.post("/api/v1/auth/signup", json=signup_payload)
    assert signup_response.status_code == 201

    # Logando com o usuário criado
    login_payload = {"username": "master@dev.com", "password": "jujuba"}
    login_response = use_test_client.post("/api/v1/auth/login", data=login_payload)
    assert login_response.status_code == 200

    access_token = login_response.json()["access_token"]
    # Requisição para obter todas as despesas extras
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo extra expenses
    json_request = {
        "amount": 100.00,
        "description": "teste",
        "date": datetime.now()
    }

    post_expenses_response = use_test_client.post("/api/v1/extra-expenses/", headers=headers, params=json_request)
    assert post_expenses_response.status_code == 201
    
    extra_expense_id = post_expenses_response.json()["response"]["id"]
    delete_expenses_response = use_test_client.delete(f"/api/v1/extra-expenses/{extra_expense_id}", headers=headers)
    assert delete_expenses_response.status_code == 200

    get_expenses_response = use_test_client.get(f"/api/v1/extra-expenses/{extra_expense_id}", headers=headers)
    assert get_expenses_response.status_code == 404


@pytest.mark.asyncio
async def test_post_multiple_extra_expenses(use_test_client):
    # Criando um usuário
    signup_payload = {
        "username": "devMaster",
        "password": "jujuba",
        "email": "master@dev.com",
        "name": "dev",
    }
    signup_response = use_test_client.post("/api/v1/auth/signup", json=signup_payload)
    assert signup_response.status_code == 201

    # Logando com o usuário criado
    login_payload = {"username": "master@dev.com", "password": "jujuba"}
    login_response = use_test_client.post("/api/v1/auth/login", data=login_payload)
    assert login_response.status_code == 200

    access_token = login_response.json()["access_token"]
    # Requisição para obter todas as despesas extras
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo extra expenses
    json_request = [
        {
            "amount": 100.00,
            "description": "teste",
            "date": str(datetime.now())
        },
        {
            "amount": 120.00,
            "description": "teste 1",
            "date": str(datetime.now())
        },
        {
            "amount": 130.00,
            "description": "teste 2",
            "date": str(datetime.now())
        }
    ]

    post_expenses_response = use_test_client.post("/api/v1/extra-expenses/multiple", headers=headers, json=json_request)
    assert post_expenses_response.status_code == 201