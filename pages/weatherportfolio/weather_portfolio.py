import logging
from pages.modelportfolio.modelportfolio_page import ModelPortfolio
from base.basepage import BasePage
import utils.customlogger as cl

class WeatherPortfolio(BasePage):
    log = cl.consoleLogger(logging.DEBUG)

    def __init__(self, driver):
        super(WeatherPortfolio, self).__init__(driver)
        self.driver = driver
        self.mp = ModelPortfolio(driver)

    ##############
    ###Locators###
    ##############
    __customize_Portfolio_button__ = "//*[contains(text(),'Customize Portfolio') and @href = 'explore_portfolio/1']"
    __customize_button_edit_control__= "//*[contains(text(),'Customise')]"
    __slider__= "//*[@class='col-md-9']//child::input[1]"
    __slider_range_percent__ = "//*[@class='col-md-9']//parent::div/div"
    __rebalance_button__ = "//*[contains(text(),'Rebalance')]"
    __invest_button__ = "//*[contains(text(),'Invest Now')]"
    __reset_button__ = "//*[contains(text(),'Reset')]"
    __add_stock_button__ = "//*[contains(text(),'+ Add Stock')]"
    __BT_Group_plc__add_stock_button__= "//*[@id='modal-1']//child::div//a[contains(text(),'BT Group plc')]//following::button[1]"
    __Done_button__ = "//*[contains(text(),'Done')]"
    __bT_Group_plc_portfolio__ = "//*[@class='row constituent-row vertical-align']//a[contains(text(),'BT Group plc')]"
    __BT_Group_plc_dialog__ = "//*[@id='modal-1']//child::div//a[contains(text(),'BT Group plc')]"

    def clickCustomizePortfolioButton(self):
        # In next screen click on button “Customize Portfolio” to make changes to portfolio
        self.clickByXpath(self.__customize_Portfolio_button__)

    def clickCustomizeButtonToEditControl(self):
       #Click on “Customize” button to enable edit controls
       self.clickByXpath(self.__customize_button_edit_control__)

    def changeSliderButton(self, sliderPercent):
        #Change slider of “ SPDR S&P 500 ETF TRUST SPY US EQUITY ” to 50%
        self.slidingVerticallyByXpathWithRange(slider_xpath= self.__slider__,slider_range_percent_xpath= self.__slider_range_percent__,slider_range_percent= sliderPercent)

    def clickRebalanceButton(self):
        # Click on “Rebalance” button
        self.clickByXpath(self.__rebalance_button__)

    def clickInvestButton(self):
        # Click on “Invest” button
        self.clickByXpath(self.__invest_button__)

    def rebalanceValidation(self):
        self.mp.clickExploreInvestmentIdeasButton()
        self.clickCustomizePortfolioButton()
        self.clickCustomizeButtonToEditControl()
        self.changeSliderButton(sliderPercent="50")
        self.clickRebalanceButton()
        self.clickInvestButton()

    def verifyResetText(self):
       #Ensure the text change to “Reset”
        reset_text = self.getTextByXpath(self.__reset_button__)
        if reset_text == 'Reset':
            self.log.info("PASS::Reset Text is present after clicking 'Customize' button ")
            return True
        else:
            self.log.error("FAIL::Reset Text is not present after clicking 'Customize' button")
            return False

    def clickAddStock(self):
        # Click on “+Add Stock”
        self.clickByXpath(self.__add_stock_button__)

    def clickAddStockInDialog(self):
        # Click “Add Stock” in “BT Group plc” row.
        self.webScroll("down")
        self.clickByXpath(self.__BT_Group_plc__add_stock_button__)

    def clickDoneInDialog(self):
        # Click on “Done”
        self.driver.find_element_by_xpath(self.__Done_button__).click()

    def addStockAndValidateInPortfolio(self):
        self.mp.clickExploreInvestmentIdeasButton()
        self.clickCustomizePortfolioButton()
        self.clickCustomizeButtonToEditControl()
        self.verifyResetText()
        self.clickAddStock()
        self.clickAddStockInDialog()
        self.clickDoneInDialog()
        # Check whether “BT Group plc” is added to the portfolio
        bT_Group_plc_portfolio = self.isElementPresentByXpath(self.__bT_Group_plc_portfolio__)
        if bT_Group_plc_portfolio:
            self.log.info("PASS::'BT Group plc' is added to the portfolio")
            return True
        else:
            self.log.error("FAIL::'BT Group plc' is not added to the portfolio")
            return False