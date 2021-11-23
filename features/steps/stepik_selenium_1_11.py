import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/")
basic_auth = driver.find_element(By.XPATH,"//li/a[text() = 'Basic Auth']")
basic_auth.click()
time.sleep(5)
driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')
# Напишем текст ответа в найденное поле

time.sleep(5)


# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.close()
driver.quit()