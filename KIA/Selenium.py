from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.kia.gov.kw/")
driver.maximize_window()
tittle = driver.title

about = driver.find_element(By.LINK_TEXT, "About")
driver.wait(10)
about.click()

# print(tittle)
