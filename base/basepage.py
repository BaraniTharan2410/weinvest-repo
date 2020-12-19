from base.seleniumwebdriver import SeleniumDriver
from traceback import print_stack
import utils.customlogger as cl
import logging

class BasePage(SeleniumDriver):
    log = cl.consoleLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        super(BasePage,self).__init__(driver)

    def getTittle(self):
        """
        Get the current web page title
        :return: tittle
        """
        try:
            tittle = self.driver.title
            self.log.info("Title of the webpage : "+tittle)
        except:
            self.log.error("Title of Web page cannot be fetched")
            print_stack()
        return tittle

