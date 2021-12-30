from selenium import webdriver
import os
from termcolor import colored, cprint
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import webdriver_manager
from webdriver_manager.firefox import GeckoDriverManager

ROOT_DIR = os.path.abspath('../../')
driver = None


class AllDrivers:

    def __init__(self):
        cprint(ROOT_DIR, 'green')
        # driver = webdriver.Chrome(executable_path=ROOT_DIR + '/executables/chromedriver.exe')
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return driver

    def closeDriver(self,driver):
        driver.quit()

#    driv = getDriver()
#    driv.get('https://www.google.com')
#    closeDriver(driv)
