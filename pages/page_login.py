import time
from appium.webdriver.common.appiumby import By

login_button = By.ID, "com.loginmodule.learning:id/appCompatButtonLogin"
field_username = By.ID, "com.loginmodule.learning:id/textInputEditTextEmail"
field_password = By.ID, "com.loginmodule.learning:id/textInputEditTextPassword"
popup_login = By.ID , "com.loginmodule.learning:id/snackbar_text"
alert_email = By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[text(), 'Enter Valid Email']"


def do_login(driver, username, password):
    driver.find_element(*field_username).send_keys(username)
    driver.find_element(*field_password).send_keys(password)
    driver.find_element(*login_button).click()
    time.sleep(1.5)


def login_invalid(driver, username, password, expected_popup, incorrect_input):
    do_login(driver, username, password)
    popup = None
    if incorrect_input == "email":
        popup = driver.find_element(*alert_email).text
    if incorrect_input == "incorrect email password":
        popup = driver.find_element(*popup_login).text

    if popup == expected_popup:
        assert True
    else:
        print(f"expected = {expected_popup} \npopup = {popup}")
        assert False

