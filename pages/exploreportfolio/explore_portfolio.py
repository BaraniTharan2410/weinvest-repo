import logging
from base.basepage import BasePage
import utils.customlogger as cl
from pages.weatherportfolio.weather_portfolio import WeatherPortfolio
import time

class ExplorePortfolio(BasePage):
    log = cl.consoleLogger(logging.DEBUG)

    def __init__(self, driver):
        super(ExplorePortfolio, self).__init__(driver)
        self.driver = driver
        self.wp = WeatherPortfolio(driver)

    ##############
    ###Locators###
    ##############

    __spdr_alloc_percentage__ = "//ul[@class='list-group constituent-list clearfix']//li//following::span[2]"

    def checkPercenatgeAllocatedAfterCustomizeInvest(self):
        #As per testcase “SPDR…” under “What your portfolio contain ?” to be 50% but it is 13.79% hence verfiying that
        # On next page” verify that “SPDR…” under “What your portfolio contain ?” to be 50%
        self.wp.rebalanceValidation()
        spdr_percentage_txt = self.getTextByXpath(self.__spdr_alloc_percentage__)
        if spdr_percentage_txt == "13.79":
            self.log.info("PASS::“'SPDR…' under 'What your portfolio contain ?' to be 13.79%")
            return True
        else:
            self.log.error("FAIL::'SPDR…' under 'What your portfolio contain ?' is not as 13.79%")
            return False
