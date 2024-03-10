from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize ChromeDriver
driver = webdriver.Chrome()

# maximizing the Chrome window
driver.maximize_window()


driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(1)

# Enter the Username
driver.find_element(By.NAME, 'username').send_keys('Admin')
time.sleep(1)

# Find and enter the Password
password = driver.find_element(By.NAME, 'password').send_keys('Invalid Password')
time.sleep(1)

# Click the Login button
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

driver.implicitly_wait(5)
# Find the invalid Credentials
errortext = driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
print("Error Message: " + errortext)
time.sleep(1)


# Close the browser
driver.quit()