import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " - Creating connection to the hub")
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
driver = webdriver.Remote(command_executor='http://test:test-password@ggr:4444/wd/hub', desired_capabilities=capabilities)
print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " - Print driver URL and session ID")
print(f'driver.command_executor._url: {driver.command_executor._url}')
print(f'driver.session_id: {driver.session_id}')
print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " - Open page on session")
driver.get("https://www.w3schools.com/html/")
print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " - Get element from page")
vartext = driver.find_element(By.CSS_SELECTOR, "h1").text
print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " - The element capture show: " + vartext)