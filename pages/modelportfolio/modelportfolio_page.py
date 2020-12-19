import logging
from base.basepage import BasePage
import utils.customlogger as cl
import re

class ModelPortfolio(BasePage):

    log = cl.consoleLogger(logging.DEBUG)

    def __init__(self, driver):
        super(ModelPortfolio,self).__init__(driver)
        self.driver = driver

    ##############
    ###Locators###
    ##############
    __explore_Investment_Ideas_button__ = "//*[contains(text(),'Explore Investment Ideas') and @href = 'weather_portfolio']"
    __recommendations__ = "//*[@href='#selected-model-portfolios']"
    __other_portfolio__ = "//*[@href='#remaining-model-portfolios']"
    __Recommended_min__  = "//*[contains(text(),'Recommended')]"
    __others_min__ = "//*[contains(text(),'Others')]"

    def clickExploreInvestmentIdeasButton(self):
        # Select “All Weather Strategy” by clicking on “Explore Investment Ideas”
        self.clickByXpath(self.__explore_Investment_Ideas_button__)

    # check tabs with text “X Portfolio recommendations based on your preferences”
    def verifyRecommendationTab(self):
        recommendations = self.getTextByXpath(self.__recommendations__)
        recommendations_num = re.findall(r'(\d+) Portfolio recommendations based on your preferences', recommendations)
        if re.match(r'[0-9]+ Portfolio recommendations based on your preferences', recommendations):
            self.log.info("PASS::tabs with text 'X Portfolio recommendations based on your preferences'")
        else:
            self.log.error("FAIL::tabs with text 'X Portfolio recommendations based on your preferences'")
        return recommendations_num

    # check tabs with text “Y other portfolio choices available”
    def verifyOtherPortfolioTab(self):
        other_portfolio = self.getTextByXpath(self.__other_portfolio__)
        other_portfolionum = re.findall(r'(\d+) other portfolio choices available', other_portfolio)
        if re.match(r'[0-9]+ other portfolio choices available', other_portfolio):
            self.log.info("PASS::tabs with text 'Y other portfolio choices available'")
        else:
            self.log.error("FAIL::tabs with text 'Y other portfolio choices available'")
        return other_portfolionum

    def ResizeWindow(self, height, width):
        # Resize browser window to 375 x 667
        self.setWindowSize(height,width)

    # check tabs with text “Recommended (X)”
    def verifyRecommendedTabMinResolution(self):
        Recommended_min = self.getTextByXpath(self.__Recommended_min__)
        Recommended_minnum = re.findall(r'Recommended \((\d+)\)', Recommended_min)
        if re.match(r'Recommended \(+[0-9]+\)', Recommended_min):
            self.log.info("PASS::tabs with text 'Recommended (X)'")
        else:
            self.log.error("FAIL::tabs with text 'Recommended (X)'")
        return Recommended_minnum

    # check tabs with text “Others (Y)“
    def verifyOtherTabMinResolution(self):
        others_min = self.getTextByXpath(self.__others_min__)
        others_minnum = re.findall(r'Others \((\d+)\)', others_min)
        if re.match(r'Others \(+[0-9]+\)', others_min):
            self.log.info("PASS::tabs with text 'Others (Y)'")
        else:
            self.log.error("FAIL::tabs with text 'Others (Y)'")
        return others_minnum

    def tabVerificaion(self,height=375, width= 667):
        recommendations_num = self.verifyRecommendationTab()
        other_portfolionum= self.verifyOtherPortfolioTab()
        self.ResizeWindow(height, width)
        Recommended_minnum = self.verifyRecommendedTabMinResolution()
        others_minnum= self.verifyOtherTabMinResolution()
        # Check X, Y are same as in normal resolution and standard resolution
        if recommendations_num == Recommended_minnum and other_portfolionum == others_minnum:
            self.log.info("PASS::x and y numbers are same")
            return True
        else:
            self.log.error("FAIL::x and y numbers are not same")
            return False