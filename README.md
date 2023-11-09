### Dependency
pytest, appium
### Run Code
main runner : test.py
```bash
pytest test.py
```
### Scenario
There is 13 scenario for mobile dan 2 for API  in test.py file: 

##### API: 
- test_api_get
- test_api_post

#### Mobile
- test_001_register_success_and_login
- test_002_register_existing_email
- test_003_register_empty_field
- test_004_register_incorrect_email_format
- test_005_register_incorrect_email_format_with_special_character
- test_006_register_missmatch_password
- test_007_register_empty_name
- test_008_register_empty_email
- test_009_register_empty_password
- test_010_login_invalid_email_password
- test_011_login_empty_email
- test_012_login_empty_password
- test_013_login_empty_field
