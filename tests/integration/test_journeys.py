from datetime import datetime

import pytest


@pytest.mark.asyncio
async def test_get_journeys(use_test_client):
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
    # Requisição para obter todas as taxas de horas
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo journeys
    json_request = {
        "start": "2024-10-21T18:17:05.137Z",
        "end": "2024-10-21T22:17:05.137Z",
        "hourly_rate": 100.00,
        "start_date": datetime.now(),
    }

    post_expenses_response = use_test_client.post(
        "/api/v1/journeys/", headers=headers, params=json_request
    )
    assert post_expenses_response.status_code == 201

    get_expenses_response = use_test_client.get("/api/v1/journeys/", headers=headers)
    assert get_expenses_response.status_code == 200


@pytest.mark.asyncio
async def test_post_journeys(use_test_client):
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
    # Requisição para obter todas as taxas de horas
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo journeys
    json_request = {
        "start": "2024-10-21T18:17:05.137Z",
        "end": "2024-10-21T22:17:05.137Z",
        "hourly_rate": 100.00,
        "start_date": datetime.now(),
    }

    post_expenses_response = use_test_client.post(
        "/api/v1/journeys/", headers=headers, params=json_request
    )
    assert post_expenses_response.status_code == 201


@pytest.mark.asyncio
async def test_get_by_id_journeys(use_test_client):
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
    # Requisição para obter todas as taxas de horas
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo journeys
    json_request = {
        "start": "2024-10-21T18:17:05.137Z",
        "end": "2024-10-21T22:17:05.137Z",
        "hourly_rate": 100.00,
        "start_date": datetime.now(),
    }

    post_expenses_response = use_test_client.post(
        "/api/v1/journeys/", headers=headers, params=json_request
    )
    assert post_expenses_response.status_code == 201

    journey_id = post_expenses_response.json()["response"]["id"]
    get_expenses_response = use_test_client.get(
        f"/api/v1/journeys/{journey_id}", headers=headers
    )
    assert get_expenses_response.status_code == 200


@pytest.mark.asyncio
async def test_put_by_id_journeys(use_test_client):
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
    # Requisição para obter todas as taxas de horas
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo journeys
    json_request = {
        "start": "2024-10-21T18:17:05.137Z",
        "end": "2024-10-21T22:17:05.137Z",
        "hourly_rate": 100.00,
        "start_date": datetime.now(),
    }

    post_expenses_response = use_test_client.post(
        "/api/v1/journeys/", headers=headers, params=json_request
    )
    assert post_expenses_response.status_code == 201
    assert post_expenses_response.json()["response"]["hourly_rate"] == 100.00

    json_request = {
        "start": "2024-10-21T18:17:05.137Z",
        "end": "2024-10-21T22:17:05.137Z",
        "hourly_rate": 150.00,
        "start_date": str(datetime.now()),
    }

    journey_id = post_expenses_response.json()["response"]["id"]
    put_expenses_response = use_test_client.put(
        f"/api/v1/journeys/{journey_id}", headers=headers, json=json_request
    )
    assert put_expenses_response.status_code == 200

    get_expenses_response = use_test_client.get(
        f"/api/v1/journeys/{journey_id}", headers=headers
    )
    assert get_expenses_response.status_code == 200
    assert get_expenses_response.json()["hourly_rate"] == 150.00


@pytest.mark.asyncio
async def test_delete_by_id_journeys(use_test_client):
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
    # Requisição para obter todas as taxas de horas
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo journeys
    json_request = {
        "start": "2024-10-21T18:17:05.137Z",
        "end": "2024-10-21T22:17:05.137Z",
        "hourly_rate": 100.00,
        "start_date": datetime.now(),
    }

    post_expenses_response = use_test_client.post(
        "/api/v1/journeys/", headers=headers, params=json_request
    )
    assert post_expenses_response.status_code == 201

    journey_id = post_expenses_response.json()["response"]["id"]
    delete_expenses_response = use_test_client.delete(
        f"/api/v1/journeys/{journey_id}", headers=headers
    )
    assert delete_expenses_response.status_code == 200

    get_expenses_response = use_test_client.get(
        f"/api/v1/journeys/{journey_id}", headers=headers
    )
    assert get_expenses_response.status_code == 404


@pytest.mark.asyncio
async def test_post_multiple_journeys(use_test_client):
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
    # Requisição para obter todas as taxas de horas
    headers = {"Authorization": f"Bearer {access_token}"}

    # Inserindo journeys
    json_request = [
        {
            "start": "2024-10-19T18:17:05.137Z",
            "end": "2024-10-19T22:17:05.137Z",
            "hourly_rate": 100.00,
            "start_date": str(datetime.now()),
        },
        {
            "start": "2024-10-20T18:17:05.137Z",
            "end": "2024-10-20T22:17:05.137Z",
            "hourly_rate": 150.00,
            "start_date": str(datetime.now()),
        },
        {
            "start": "2024-10-21T18:17:05.137Z",
            "end": "2024-10-21T22:17:05.137Z",
            "hourly_rate": 200.00,
            "start_date": str(datetime.now()),
        },
    ]

    post_expenses_response = use_test_client.post(
        "/api/v1/journeys/multiple", headers=headers, json=json_request
    )
    assert post_expenses_response.status_code == 201
