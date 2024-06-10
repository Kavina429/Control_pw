from selenium.webdriver.common.by import By

# локаторы логина
locator_field_username = (By.XPATH, '//*[@id="username"]')
locator_field_user_password = (By.XPATH, '//*[@id="password"]')
locator_button_login = (By.XPATH, '//*[@id="login"]/button/i')
locator_flash = (By.XPATH, '//*[@id="flash"]')
locator_button_logout = (By.XPATH, '//*[@id="content"]/div/a/i')
