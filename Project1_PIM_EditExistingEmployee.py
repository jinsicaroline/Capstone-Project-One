from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize ChromeDriver
driver = webdriver.Chrome()

# maximizing the Chrome window
driver.maximize_window()

# Navigate to the OrangeHRM login page
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(1)

# Find and enter the Username
driver.find_element(By.NAME, 'username').send_keys('Admin')
time.sleep(1)

# Find and enter the Password
driver.find_element(By.NAME, 'password').send_keys('admin123')
time.sleep(1)

# Click the Login button
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

driver.implicitly_wait(10)

if "dashboard/index" in driver.current_url:
    driver.find_element(By.LINK_TEXT, 'PIM').click()

driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...'][1]").send_keys('Jhon Mark')
# time.sleep(1)
# name.send_keys('Test1')
time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-pencil-fill']").click()
time.sleep(1)

# Replace the Lastname field with the generated word
firstName = driver.find_element(By.NAME, 'firstName')
firstName.click()
time.sleep(1)
firstName.send_keys(Keys.CONTROL + "a")
firstName.send_keys(Keys.DELETE)
time.sleep(1)
firstName.send_keys('JhonMarks')
time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

# Close the browser
driver.quit()