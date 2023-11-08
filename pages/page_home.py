import time
from appium.webdriver.common.appiumby import By

# text_name = By.ID, "com.loginmodule.learning:id/textViewName"
text_email = By.ID, "com.loginmodule.learning:id/textViewEmail"
text_password = By.ID, "com.loginmodule.learning:id/textViewPassword"
text_name = By.XPATH, "//android.widget.LinearLayout[1]/android.widget.TextView[@resource-id='com.loginmodule.learning:id/textViewName']"


def assert_login(driver, name, email, password):
    time.sleep(3)
    actual_name = driver.find_element(*text_name).text
    actual_email = driver.find_element(*text_email).text
    actual_password = driver.find_element(*text_password).text
    if actual_email == email and actual_password == password and actual_name == name:
        assert True
    else:
        print(f"actual email == {actual_email} expected email == {email}\n"
              f"actual name == {actual_password} expected email == {password}\n"
              f"actual name == {actual_name} expected email == {name}\n")
        assert False


