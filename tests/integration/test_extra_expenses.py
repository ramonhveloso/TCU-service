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
    get_expenses_response = use_test_client.get("/api/v1/extra-expenses/", headers=headers)
    assert get_expenses_response.status_code == 200

    response_json = get_expenses_response.json()
    assert "extra_expenses" in response_json
    assert isinstance(response_json["extra_expenses"], list)
    
@pytest.mark.asyncio
async def test_post_extra_expense(use_test_client):
    # Criando e logando o usuário
    signup_payload = {
        "username": "user456",
        "password": "password456",
        "email": "user456@example.com",
        "name": "User 456"
    }
    signup_response = use_test_client.post("/api/v1/auth/signup", json=signup_payload)
    assert signup_response.status_code == 201

    login_payload = {"username": "user456@example.com", "password": "password456"}
    login_response = use_test_client.post("/api/v1/auth/login", data=login_payload)
    assert login_response.status_code == 200

    access_token = login_response.json()["access_token"]

    # Criando uma despesa extra
    headers = {"Authorization": f"Bearer {access_token}"}
    expense_payload = {
        "amount": 120.50,
        "description": "Office supplies",
        "date": "2024-10-17T00:00:00"
    }
    post_expense_response = use_test_client.post("/api/v1/extra-expenses/", json=expense_payload, headers=headers)
    assert post_expense_response.status_code == 201

    response_json = post_expense_response.json()
    assert response_json["message"] == "Expense created successfully"
    assert response_json["response"]["amount"] == 120.50

@pytest.mark.asyncio
async def test_put_extra_expense(use_test_client):
    # Logando com o usuário
    login_payload = {"username": "user456@example.com", "password": "password456"}
    login_response = use_test_client.post("/api/v1/auth/login", data=login_payload)
    assert login_response.status_code == 200

    access_token = login_response.json()["access_token"]

    # Atualizando uma despesa extra
    headers = {"Authorization": f"Bearer {access_token}"}
    update_payload = {
        "amount": 130.75,
        "description": "Updated description"
    }
    put_expense_response = use_test_client.put("/api/v1/extra-expenses/1", json=update_payload, headers=headers)
    assert put_expense_response.status_code == 200

    response_json = put_expense_response.json()
    assert response_json["message"] == "Expense updated successfully"
    assert response_json["response"]["amount"] == 130.75
    assert response_json["response"]["description"] == "Updated description"

@pytest.mark.asyncio
async def test_delete_extra_expense(use_test_client):
    # Logando com o usuário
    login_payload = {"username": "user456@example.com", "password": "password456"}
    login_response = use_test_client.post("/api/v1/auth/login", data=login_payload)
    assert login_response.status_code == 200

    access_token = login_response.json()["access_token"]

    # Excluindo uma despesa extra
    headers = {"Authorization": f"Bearer {access_token}"}
    delete_expense_response = use_test_client.delete("/api/v1/extra-expenses/1", headers=headers)
    assert delete_expense_response.status_code == 200

    response_json = delete_expense_response.json()
    assert response_json["message"] == "Expense deleted successfully"

