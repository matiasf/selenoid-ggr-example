import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " - Creating connection to the hub")
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
driver = webdriver.Remote(command_executor='http://test:test-password@localhost:4446/wd/hub', desired_capabilities=capabilities)
print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " - Close created session")
driver.close()
driver.quit()
print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " - Hack session")
driver.session_id = 'COPY_SESSION_RECONECT_HERE'
print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " - Open page on session")
print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " - Get element from page")
vartext = driver.find_element(By.CSS_SELECTOR, "h1").text
print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " - The element capture show: " + vartext)