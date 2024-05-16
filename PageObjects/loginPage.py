from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

class LoginPage:
    
    login_button = "//p[contains(text(),'Login')]"
    user_id = "email"
    password = "password"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.user_id).send_keys(username)

    def setPassword(self, psw):
        self.driver.find_element_by_id(self.password).send_keys(psw)

    def clickLogIn(self):
        self.driver.find_element(By.XPATH, self.login_button).click()
