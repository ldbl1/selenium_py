from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome('C:/Driver/chromedriver.exe')
driver.get("https://www.instagram.com/")
driver.maximize_window()
XPusuario = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input'
XPcontrasena = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'
XPentrar = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div'

driver.find_element_by_xpath(XPusuario).send_keys('John')
driver.find_element_by_xpath(XPcontrasena).send_keys('1234')
driver.find_element_by_xpath(XPentrar).submit()
