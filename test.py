from pages import page_register
from pages import page_login
from pages import page_home
import urllib.request
import json

register = page_register
login = page_login
home = page_home
url = "https://jsonplaceholder.typicode.com/posts"
data_to_send = {
    "userId": 12,
    "title": "recomendations",
    "body": "motorcycle"
}

def test_api_get():
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    data = response.read()
    data = json.loads(data.decode('utf-8'))

    for item in data:
        if not isinstance(item["userId"], int):
            print(f"userId is not of type int: {item['userId']}")
            assert False
        if not isinstance(item["id"], int):
            print(f"id is not of type int: {item['id']}")
            assert False
        if not isinstance(item["title"], str):
            print(f"title is not of type string: {item['title']}")
            assert False
        if not isinstance(item["body"], str):
            print(f"body is not of type string: {item['body']}")

def test_api_post():
    data = json.dumps(data_to_send).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST', headers={'Content-Type': 'application/json'})
    response = urllib.request.urlopen(req)
    response_data = response.read()
    response_data = json.loads(response_data.decode('utf-8'))
    if response_data["userId"] == 12 and response_data["title"] == "recomendations" and response_data["body"] == "motorcycle":
        assert True
    else:
        print(f"repsponse incorrect = {response_data}")
        assert False


def test_001_register_success_and_login(driver):
    register.register_submit(driver, "test", "test@gmail.com", "password", "password", "Registration Successful")
    login.do_login(driver, "test@gmail.com", "password")
    home.assert_login(driver, "test", "test@gmail.com", "password")

def test_002_register_existing_email(driver):
    register.register_submit(driver, "test", "test@gmail.com", "password", "password", "Registration Successful")
    register.register_submit(driver, "test", "test@gmail.com", "password", "password", "Email Already Exists")

def test_003_register_empty_field(driver):
    register.register_empty_all_field(driver)

def test_004_register_incorrect_email_format(driver):
    register.register_incorrect_input(driver, "test", "email", "password", "password", "Enter Valid Email", "email")

def test_005_register_incorrect_email_format_with_special_character(driver):
    register.register_incorrect_input(driver, "test", "email##@mail.com", "password", "password", "Enter Valid Email", "email")

def test_006_register_missmatch_password(driver):
    register.register_incorrect_input(driver, "test", "test@gmail.com", "password", "incorrectpassword", "Password Does Not Matches", "password")

def test_007_register_empty_name(driver):
    register.register_incorrect_input(driver, "", "test@gmail.com", "password", "password", "Enter Full Name", "name_empty")

def test_008_register_empty_email(driver):
    register.register_incorrect_input(driver, "test", "", "password", "password", "Enter Valid Email", "email")

def test_009_register_empty_password(driver):
    register.register_incorrect_input(driver, "test", "test@gmail.com", "", "", "Enter Password", "password_empty")

def test_010_login_invalid_email_password(driver):
    login.login_invalid(driver, "test@gmail.com", "password", "Wrong Email or Password", "incorrect email password")

def test_011_login_empty_email(driver):
    login.login_invalid(driver, "", "password", "Enter Valid Email", "email")

def test_011_login_empty_password(driver):
    login.login_invalid(driver, "test@gmail.com", "", "Enter Valid Email", "email")

def test_011_login_empty_field(driver):
    login.login_invalid(driver, "", "", "Enter Valid Email", "email")



