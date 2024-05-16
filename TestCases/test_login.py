from selenium import webdriver
import pytest
import sys
sys.path.append("E:\\folder F\\git\\Srujanee")
from PageObjects.loginPage import LoginPage
# from PageObjects.loginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGeneration
from time import sleep
import os


class Test_Login:

    url = ReadConfig.getURL()
    # url = "https://dev.srujanee.in/auth/login?path="
    logger = LogGeneration.logGen()

    username = "sivaprasad.baral@reverieinc.com"
    password = "Rev@123"

    os.environ['WDM_LOG'] = '0'

    def test_1_login(self, setUp):
        # self.logger.info(" ******** ")
        self.logger.info("*** test_1_login ***")
        self.logger.info("*** Passed ***")
        self.driver = setUp
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        sleep(5)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_1_login.png")
        self.driver.close()

    def test_2_login(self, setUp):
        self.logger.info("*** Verifying Login Test ***")
        self.driver = setUp
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_2_login.png")
        sleep(10)
        print("Passed")
        self.driver.close()

