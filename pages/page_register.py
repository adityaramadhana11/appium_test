import time
from appium.webdriver.common.appiumby import By

field_register_name = By.ID, "com.loginmodule.learning:id/textInputEditTextName"
field_register_email = By.ID, "com.loginmodule.learning:id/textInputEditTextEmail"
field_register_password = By.ID, "com.loginmodule.learning:id/textInputEditTextPassword"
field_register_confirm_password = By.ID, "com.loginmodule.learning:id/textInputEditTextConfirmPassword"
button_register = By.ID, "com.loginmodule.learning:id/appCompatButtonRegister"
button_register_page = By.ID, "com.loginmodule.learning:id/textViewLinkRegister"
popup_register = By.ID , "com.loginmodule.learning:id/snackbar_text"
alert_name = By.XPATH, "//android.widget.TextView[text(), 'Enter Full Name']"
alert_email = By.XPATH, "//android.widget.TextView[text(), 'Enter Valid Email']"
alert_password = By.XPATH, "//android.widget.TextView[text(), 'Enter Password']"
alert_password_not_match = By.XPATH, "//android.widget.TextView[text(), 'Password Does Not Matches']"


# alert_name = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.support.v7.widget.LinearLayoutCompat/TextInputLayout[1]/android.widget.LinearLayout/android.widget.TextView"

def do_register(driver, name, email, password, confirm_password):
    driver.find_element(*button_register_page).click()
    time.sleep(1.5)
    driver.find_element(*field_register_name).send_keys(name)
    driver.find_element(*field_register_email).send_keys(email)
    driver.find_element(*field_register_password).send_keys(password)
    driver.find_element(*field_register_confirm_password).send_keys(confirm_password)
    driver.find_element(*button_register).click()
    time.sleep(1.5)

def register_submit(driver, name, email, password, confirm_password, expected_popup):
    do_register(driver, name, email, password, confirm_password)
    popup = driver.find_element(*popup_register).text
    if popup == expected_popup:
        assert True
    else:
        print(f"expected = {expected_popup} \npopup = {popup}")
        assert False
    driver.back()

def register_empty_all_field(driver):
    driver.find_element(*button_register_page).click()
    time.sleep(1.5)
    driver.find_element(*button_register).click()
    time.sleep(3)
    alert_name_error = driver.find_element(*alert_name).text
    if alert_name_error == "Enter Full Name":
        assert True
    else:
        print(f"allert = {alert_name_error}")
        assert False

def register_incorrect_input(driver, name, email, password, confirm_password, expected_popup , incorecct_input):
    do_register(driver, name, email, password, confirm_password)
    popup = None
    if incorecct_input == "email":
        popup = driver.find_element(*alert_email).text
    elif incorecct_input == "password":
        popup = driver.find_element(*alert_password_not_match).text
    elif incorecct_input == "name_empty":
        popup = driver.find_element(*alert_name).text
    elif incorecct_input == "password_empty":
        popup = driver.find_element(*alert_password).text

    if popup == expected_popup:
        assert True
    else:
        print(f"expected = {expected_popup} \npopup = {popup}")
        assert False
    driver.back()