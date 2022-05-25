import requests
import pytest
import logging as logger


@pytest.mark.smoke
def test_get_user_with_id_1_check_status_code_equals_200():
    logger.info(f'Checking Response code')
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200


@pytest.mark.smoke
def test_get_user_with_id_1_check_content_type_equals_json():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


@pytest.mark.smoke
def test_get_user_first_name():
    response = requests.get("https://reqres.in/api/users?page=2")
    resp = response.json()
    print(resp)
    assert resp['data'][1]['first_name'] == "Lindsay"


@pytest.mark.regression
def test_get_user_check_name():
    response = requests.get("https://reqres.in/api/users?page=2")
    resp = response.json()
    assert resp['data'][0]["first_name"] == "Michael"


@pytest.mark.highpriority
def test_get_user_email_address():
    response = requests.get("https://reqres.in/api/users/2")
    resp = response.json()
    assert (resp['data']['email']).endswith("@reqres.in")
    assert len(resp) == 2


def test_post_register_user():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post("https://reqres.in/api/register", json=payload)
    resp = response.json()
    assert response.status_code == 200, "Successfully Registered"


def test_post_check_status_code_validate_employee():
    details = {
        "company": "Payfare",
        "Domain": "Payments Gateway",
        "Employee": "Ravi",
        "Designation": "Test Engineer",
        "mail": "vkumar@payfare.com",
        "Tool": "python"

    }
    response = requests.post("https://reqres.in/api/users", json=details)
    assert response.status_code == 201
    resp = response.json()
    assert (resp['Employee']) == "Ravi"


def test_put_modify_data():
    Data = {
        "name": "Payfare",
        "salary": "Monthly wages",
        "Transaction": "online",
        "id": "2507"
    }

    response = requests.put("https://reqres.in/api/users/2", data=Data)
    assert response.status_code == 200
    resp = response.json()
    assert resp['id'] == '2507'


def test_delete_data():
    response = requests.delete("https://reqres.in/api/users?page=2")
    assert response.status_code == 204, "Data doesn't Deleted "

# @pytest.mark.parametrize("userid, expected_name", test_user)
# def test_get_data_for_user_check_name(userid, expected_name):
#     response = requests.get(f"https://reqres.in/api/users?page=2{userid}")
#     resp = response.json()
#     assert resp['data'][0]["first_name"] == expected_name
