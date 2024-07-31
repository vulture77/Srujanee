from selenium import webdriver
import pytest
import sys
sys.path.append("E:\\folder F\\git\\Srujanee")
from PageObjects.loginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGeneration
from time import sleep
import os

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from TestCases.test_base import Base
from selenium.webdriver.common.by import By

class Test_Login():

    # url = ReadConfig.getURL()
    url = "https://dev.srujanee.in/auth/login?path="
    logger = LogGeneration.logGen()

    username = "baralsibaprasad@gmail.com"
    password = "Rev@123"

    # os.environ['WDM_LOG'] = '0'
    # @classmethod
    # def setUp(self, setUp_brow):
    #     # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     self.driver = setUp_browser
    #     self.driver.get(self.url)

    def test_1_login(self, driver_init):
        # self.logger.info(" ******** ")
        # self.logger.info("*** test_1_login ***")
        # self.logger.info("*** Passed ***")
        self.driver = driver_init
        # self.driver.get(self.url)
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        sleep(2)
        # self.driver.save_screenshot(".\\Screenshots\\" + "test_1_login.png")
        # self.driver.close()

    def test_2_googleLogin(self, driver_init):
        # self.logger.info(" ******** ")
        # self.logger.info("*** test_1_login ***")
        # self.logger.info("*** Passed ***")
        self.driver = driver_init
        self.driver.get("https://dev.srujanee.in/write")
        self.lp = LoginPage(self.driver)
        # self.lp.googleLogin()
        sleep(5)

    def test_3_loginpass(self, driver_init):
    # #     self.logger.info("*** Verifying Login Test ***")
        self.driver = driver_init
        self.driver.get("https://dev.srujanee.in/userprofile?componentState=false")
        # self.lp = LoginPage(self.driver)
        # self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogIn()
    #     self.driver.save_screenshot(".\\Screenshots\\" + "test_2_login.png")
        sleep(5)
    #     print("Passed")
    #     self.driver.close()

