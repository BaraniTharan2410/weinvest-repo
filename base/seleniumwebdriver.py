from selenium.webdriver import Chrome as driver
import os
import time
import logging
from selenium.webdriver.common.by import By
import re
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import keys_to_typing
from selenium.webdriver.support.select import Select
import utils.customlogger as cl
from selenium.webdriver.common.keys import Keys

class SeleniumDriver():

    log = cl.consoleLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def takeScreenshot(self, resultMessage):
        """
        Take screenshot for the current open webpage
        :param resultMessage: get the result message to add in filename
        :return: does not return
        """
        filename = resultMessage + '.' + str(round(time.time()*1000)) + ".png"
        screenshotDirectory = "../screenshot/"
        relativeFileName = screenshotDirectory + filename
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            else:
                self.driver.save_screenshot(destinationFile)
                self.log.info("screenshot saved to directory:: " + destinationFile)

        except:
            self.log.error("###Exception occur when saving screenshot")
            print_stack()

    def enterTextByXpath(self, xpath, data):
        """
        Enter the text in the web page using Xpath locator
        :param xpath: get xpath locator
        :param data: get data to input
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_xpath(xpath)
            element.send_keys(data)
            self.log.info("Entered text ::" + data + ":: using xpath locator: " + xpath)
        except:
            self.log.error("Cannot Entered text ::" + data + ":: using xpath locator: " + xpath)
            print_stack()

    def enterTextById(self, id, data):
        """
        Enter the text in the web page using id locator
        :param id: get id locator
        :param data: get data to input
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_id(id)
            element.send_keys(data)
            self.log.info("Entered text ::" + data + ":: using id locator: " + id)
        except:
            self.log.error("Cannot Entered text ::" + data + ":: using id locator: " + id)
            print_stack()

    def enterTextByName(self, name, data):
        """
        Enter the text in the web page using name locator
        :param name: get name locator
        :param data: get data to input
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_name(name)
            element.send_keys(data)
            self.log.info("Entered text ::" + data + ":: using name locator: " + name)
        except:
            self.log.error("Cannot Entered text ::" + data + ":: using name locator: " + name)
            print_stack()

    def enterTextByClassName(self, class_name, data):
        """
        Enter the text in the web page using className locator
        :param class_name: get className locator
        :param data: get data to input
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_class_name(class_name)
            element.send_keys(data)
            self.log.info("Entered text ::" + data + ":: using className locator: " + class_name)
        except:
            self.log.error("Cannot Entered text ::" + data + ":: using className locator: " + class_name)
            print_stack()

    def enterTextByTagName(self, tag_name, data):
        """
        Enter the text in the web page using tag name locator
        :param tag_name: get tag name locator
        :param data: get data to input
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_tag_name(tag_name)
            element.send_keys(data)
            self.log.info("Entered text ::" + data + ":: using tag name locator: " + tag_name)
        except:
            self.log.error("Cannot Entered text ::" + data + ":: using tag name locator: " + tag_name)
            print_stack()

    def enterTextByLinkText(self, link_text, data):
        """
        Enter the text in the web page using link text locator
        :param link_text: get link text locator
        :param data: get data to input
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_link_text(link_text)
            element.send_keys(data)
            self.log.info("Entered text ::" + data + ":: using link text locator: " + link_text)
        except:
            self.log.error("Cannot Entered text ::" + data + ":: using link text locator: " + link_text)
            print_stack()

    def enterTextByCssSelector(self, css_selector, data):
        """
        Enter the text in the web page using css selector locator
        :param css_selector: get css selector locator
        :param data: get data to input
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_css_selector(css_selector)
            element.send_keys(data)
            self.log.info("Entered text ::" + data + ":: using link text locator: " + css_selector)
        except:
            self.log.error("Cannot Entered text ::" + data + ":: using link text locator: " + css_selector)
            print_stack()

    def clearTextById(self, id):
        """
        Clear the text in the web page using id locator
        :param id: get id locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_id(id)
            element.clear()
            self.log.info("cleared text in id locator: " + id)
        except:
            self.log.error("Cannot clear text using id locator: " + id)
            print_stack()

    def clearTextByName(self, name):
        """
        Clear the text in the web page using name locator
        :param name: get name locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_name(name)
            element.clear()
            self.log.info("cleared text in name locator: " + name)
        except:
            self.log.error("Cannot clear text using name locator: " + name)
            print_stack()


    def clearTextByClassName(self, class_name):
        """
        Clear the text in the web page using className locator
        :param class_name: get className locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_class_name(class_name)
            element.clear()
            self.log.info("cleared text in class name locator: " + class_name)
        except:
            self.log.error("Cannot clear text using class name locator: " + class_name)
            print_stack()


    def clearTextByTagName(self, tag_name):
        """
        Clear the text in the web page using tag name locator
        :param tag_name: get tag name locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_tag_name(tag_name)
            element.clear()
            self.log.info("cleared text in tag_name locator: " + tag_name)
        except:
            self.log.error("Cannot clear text using tag name locator: " + tag_name)
            print_stack()

    def clearTextByLinkText(self, link_text):
        """
        Clear the text in the web page using link text locator
        :param link_text: get link text locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_link_text(link_text)
            element.clear()
            self.log.info("cleared text in link text locator: " + link_text)
        except:
            self.log.error("Cannot clear text using link text locator: " + link_text)
            print_stack()

    def clearTextByCssSelector(self, css_selector):
        """
        Clear the text in the web page using css selector locator
        :param css_selector: get css selector locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_css_selector(css_selector)
            element.clear()
            self.log.info("cleared text in css locator: " + css_selector)
        except:
            self.log.error("Cannot clear text using css selector locator: " + css_selector)
            print_stack()

    def setWindowSize(self,height,width):
        # Resize browser window to 375 x 667
        try:
            self.driver.set_window_size(height, width)
            self.log.info("resized to :"+str(height)+"x"+str(width))
        except:
            self.log.error("Cannot resize")
            print_stack()
    def getTextByXpath(self, xpath):
        """
        get the text in the web page using xpath locator
        :param xpath: get xpath locator
        :return: text
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            ele = self.driver.find_element_by_xpath(xpath)
            ele.location_once_scrolled_into_view
            self.driver.execute_script("window.scrollBy(0,200);")
            txt = ele.text
            text = txt.strip()
            self.log.info("Get text in xpath locator: " + xpath)
        except:
            self.log.error("Cannot get text using xpath locator: " + xpath)
            print_stack()
        return text

    def getTextById(self, id):
        """
        get the text in the web page using id locator
        :param id: get text of id locator
        :return: text
        """
        try:
            element = self.driver.find_element_by_id(id)
            text = element.text
            text = text.strip
            self.log.info("get text in id locator: " + id)
        except:
            self.log.error("Cannot get text using id locator: " + id)
            print_stack()
        return text

    def getTextByName(self, name):
        """
        get the text in the web page using name locator
        :param name: get text of name locator
        :return: text
        """
        try:
            element = self.driver.find_element_by_name(name)
            text = element.text
            text = text.strip
            self.log.info("get text in name locator: " + name)
        except:
            self.log.error("Cannot get text using name locator: " + name)
            print_stack()
        return text

    def getTextByClassName(self, class_name):
        """
        get the text in the web page using className locator
        :param class_name: get text of className locator
        :return: text
        """
        try:
            element = driver.find_element_by_class_name(class_name)
            text = element.text
            text = text.strip
            self.log.info("get text in class name locator: " + class_name)
        except:
            self.log.error("Cannot get text using class name locator: " + class_name)
            print_stack()
        return text

    def getTextByTagName(self, tag_name):
        """
        get the text in the web page using tag name locator
        :param tag_name: get text of tag name locator
        :return: text
        """
        try:
            element = driver.find_element_by_tag_name(tag_name)
            text = element.text
            text = text.strip
            self.log.info("get text in tag name locator: " + tag_name)
        except:
            self.log.error("Cannot get text using tag name locator: " + tag_name)
            print_stack()
        return text

    def getTextByLinkText(self, link_text):
        """
        get the text in the web page using link text locator
        :param link_text: get text of link text locator
        :param data: get data to input
        :return: text
        """
        try:
            element = driver.find_element_by_link_text(link_text)
            text = element.text
            text = text.strip
            self.log.info("get text in link text locator: " + link_text)
        except:
            self.log.error("Cannot get text using link text locator: " + link_text)
            print_stack()
        return text

    def getTextByCssSelector(self, css_selector):
        """
        get the text in the web page using css selector locator
        :param css_selector: get text of css selector locator
        :return: text
        """
        try:
            element = driver.find_element_by_css_selector(css_selector)
            text = element.text
            text = text.strip
            self.log.info("get text in css locator: " + css_selector)
        except:
            self.log.error("Cannot get text using css selector locator: " + css_selector)
            print_stack()
        return text

    def webScroll(self, direction = "up"):
        """
        Scroll up and scroll down in the web page
        :param direction: direction to scroll
        :return: does not return
        """
        try:
            direction = direction.lower()
            if direction == "up":
                #Scroll Up
                driver.execute_script("window.scrollBy(0, -1000);")
                self.log.info("web scroll successful in direction:  " + direction)
            elif direction == "down":
                #Scroll Down
                driver.execute_script("window.scrollBy(0, 1000);")
                self.log.info("web scroll successful in direction: " + direction)
        except:
            self.log.error("web scroll unsuccessful in direction: " + direction)
            print_stack()

    def getTittle(self):
        """
        Get the current web page title
        :return: does not return
        """
        try:
            tittle = self.driver.title
            self.log.info("Title of the webpage : "+tittle)
        except:
            self.log.error("Title of Web page cannot be fetched")
            print_stack()
        return tittle

    def isElementDisplayedByXpath(self, xpath):
        """
        check the given element is displayed
        :param xpath: get xpath locator
        :return: boolean
        """
        try:
            element = self.driver.find_element_by_xpath(xpath)
            if element.is_displayed():
                self.log.info("Displayed check successful for xpath locator: "+ xpath)
                return True
            else:
                return False
        except:
            self.log.error("Displayed check unsuccessful for xpath locator: " + xpath)
            print_stack()
            return False

    def isElementSelectedByXpath(self, xpath):
        """
        check the given element is selected
        :param xpath: get xpath locator
        :return: boolean
        """
        selected = False
        try:
            element = self.driver.find_element_by_xpath(xpath)
            if element.is_selected():
                self.log.info("Selected check successful for xpath locator: "+ xpath)
                return True
            else:
                return False
        except:
            self.log.error("Selected check unsuccessful for xpath locator: " + xpath)
            print_stack()
            return False

    def isElementEnabledByXpath(self, xpath):
        """
        check the given element is enabled
        :param xpath: get xpath locator
        :return: boolean
        """
        try:
            element = self.driver.find_element_by_xpath(xpath)
            attrValue = element.get_attribute("disabled")
            if attrValue is not None:
                #check enabled condition for element with disabled attribute
                enabled = element.is_enabled()
                self.log.info("Enabled check successful for xpath locator: "+ xpath)
            else:
                #check enabled condition for element without disabled attribute
                #getting value of class attribute to check enabled
                value = element.get_attribute("class")
                #if disabled word is not in class attribute,then it is enabled
                enabled = not ("disabled" in value)
                if enabled:
                    self.log.info("Enabled check successful for xpath locator: " + xpath)
                    return True
                else:
                    self.log.error("Enabled check unsuccessful for xpath locator: " + xpath)
                    return False
        except:
            self.log.error("Enabled check unsuccessful for xpath locator: " + xpath)
            print_stack()
            return False

    def isElementPresentByXpath(self, xpath):
        """
        check the given element is present
        :param xpath: get xpath locator
        :return: boolean
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_elements_by_xpath(xpath)
            element.location_once_scrolled_into_view
            if element.is_displayed():
                self.log.info("Element Present check successful for xpath locator: " + xpath)
                return True
            else:
                self.log.error("Element Present check unsuccessful for xpath locator: " + xpath)
                return False
        except:
            self.log.error("Element Present check unsuccessful for xpath locator: " + xpath)
            print_stack()
            return False

    def getAttributeValueByXpath(self, xpath, attr):
        """
        check the given element is enabled
        :param xpath: get xpath locator
        :param attr: get attribute value of locator
        :return: attribute Value
        """
        enabled = False
        try:
            element = self.driver.find_element_by_xpath(xpath)
            attrValue = element.get_attribute(attr)
            self.log.info(attr +" :: attribute value for locator: "+ xpath + " is " + attrValue)
        except:
            self.log.error(attr +" :: attribute value for locator: "+ xpath + " cant be fetched")
            print_stack()
        return attrValue

    def waitForElementByXpath(self, xpath, timeout= 10, pollfrequency= 0.5):
        """
        wait until the element is found by xpath locator
        :param xpath: get xpath locator
        :return: element
        """
        element = None
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            self.log.info("waiting for maximum :: " + str(timeout) + ":: secs for element to be found")
            wait = WebDriverWait(self.driver,time_out= timeout, poll_frequency= pollfrequency, ignored_exceptions= [ElementNotVisibleException,
                                                                                                        ElementNotSelectableException,
                                                                                                        NoSuchElementException])
            element = wait.until(EC.element_to_be_clickable(ele))
            self.log.info("Element appeared on web page using xpath locator" + xpath)
        except:
            self.log.error("Element not appeared on web page using xpath locator" + xpath)
            print_stack()
        return element

    def waitForElementById(self, id, timeout= 10, pollfrequency= 0.5):
        """
        wait until the element is found by id locator
        :param id: get id locator
        :return: element
        """
        element = None
        try:
            ele = self.driver.find_element_by_id(id)
            self.log.info("waiting for maximum :: " + str(timeout) + ":: secs for element to be found")
            wait = WebDriverWait(self.driver,time_out= timeout, poll_frequency= pollfrequency, ignored_exceptions= [ElementNotVisibleException,
                                                                                                        ElementNotSelectableException,
                                                                                                        NoSuchElementException])
            element = wait.until(EC.element_to_be_clickable(ele))
            self.log.info("Element appeared on web page using id locator" + id)
        except:
            self.log.error("Element not appeared on web page using id locator" + id)
            print_stack()
        return element

    def waitForElementByName(self, name, timeout= 10, pollfrequency= 0.5):
        """
        wait until the element is found by name locator
        :param name: get name locator
        :return: element
        """
        element = None
        try:
            ele = self.driver.find_element_by_name(name)
            self.log.info("waiting for maximum :: " + str(timeout) + ":: secs for element to be found")
            wait = WebDriverWait(self.driver,time_out= timeout, poll_frequency= pollfrequency, ignored_exceptions= [ElementNotVisibleException,
                                                                                                        ElementNotSelectableException,
                                                                                                        NoSuchElementException])
            element = wait.until(EC.element_to_be_clickable(ele))
            self.log.info("Element appeared on web page using name locator" + name)
        except:
            self.log.error("Element not appeared on web page using name locator" + name)
            print_stack()
        return element

    def waitForElementByClassName(self, class_name, timeout= 10, pollfrequency= 0.5):
        """
        wait until the element is found by ClassName locator
        :param class_name: get ClassName locator
        :return: element
        """
        element = None
        try:
            ele = self.driver.find_element_by_class_name(class_name)
            self.log.info("waiting for maximum :: " + str(timeout) + ":: secs for element to be found")
            wait = WebDriverWait(self.driver,time_out= timeout, poll_frequency= pollfrequency, ignored_exceptions= [ElementNotVisibleException,
                                                                                                        ElementNotSelectableException,
                                                                                                        NoSuchElementException])
            element = wait.until(EC.element_to_be_clickable(ele))
            self.log.info("Element appeared on web page using ClassName locator" + class_name)
        except:
            self.log.error("Element not appeared on web page using ClassName locator" + class_name)
            print_stack()
        return element

    def waitForElementByTagName(self, tag_name, timeout= 10, pollfrequency= 0.5):
        """
        wait until the element is found by TagName locator
        :param tag_name: get tag name locator
        :return: element
        """
        element = None
        try:
            ele = self.driver.find_element_by_tag_name(tag_name)
            self.log.info("waiting for maximum :: " + str(timeout) + ":: secs for element to be found")
            wait = WebDriverWait(self.driver,time_out= timeout, poll_frequency= pollfrequency, ignored_exceptions= [ElementNotVisibleException,
                                                                                                        ElementNotSelectableException,
                                                                                                        NoSuchElementException])
            element = wait.until(EC.element_to_be_clickable(ele))
            self.log.info("Element appeared on web page using tag name locator" + tag_name)
        except:
            self.log.error("Element not appeared on web page using tag name locator" + tag_name)
            print_stack()
        return element

    def waitForElementByLinkText(self, link_text, timeout= 10, pollfrequency= 0.5):
        """
        wait until the element is found by link text locator
        :param link_text: get link text locator
        :return: element
        """
        element = None
        try:
            ele = self.driver.find_element_by_link_text(link_text)
            self.log.info("waiting for maximum :: " + str(timeout) + ":: secs for element to be found")
            wait = WebDriverWait(self.driver,time_out= timeout, poll_frequency= pollfrequency, ignored_exceptions= [ElementNotVisibleException,
                                                                                                        ElementNotSelectableException,
                                                                                                        NoSuchElementException])
            element = wait.until(EC.element_to_be_clickable(ele))
            self.log.info("Element appeared on web page using link text locator" + link_text)
        except:
            self.log.error("Element not appeared on web page using link text locator" + link_text)
            print_stack()
        return element

    def waitForElementByCssSelector(self, css_selector, timeout= 10, pollfrequency= 0.5):
        """
        wait until the element is found by CssSelector locator
        :param css_selector: get Css Selector locator
        :return: element
        """
        element = None
        try:
            ele = self.driver.find_element_by_css_selector(css_selector)
            self.log.info("waiting for maximum :: " + str(timeout) + ":: secs for element to be found")
            wait = WebDriverWait(self.driver,time_out= timeout, poll_frequency= pollfrequency, ignored_exceptions= [ElementNotVisibleException,
                                                                                                        ElementNotSelectableException,
                                                                                                        NoSuchElementException])
            element = wait.until(EC.element_to_be_clickable(ele))
            self.log.info("Element appeared on web page using Css Selector locator" + css_selector)
        except:
            self.log.error("Element not appeared on web page using Css Selector locator" + css_selector)
            print_stack()
        return element

    def waitForElementClickableByXpath(self, xpath, timeout= 10, pollfrequency= 0.5):
        """
        wait until the element is found by xpath locator
        :param xpath: get xpath locator
        :return: element
        """
        element = None
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            self.log.info("waiting for maximum :: " + str(timeout) + ":: secs for element to be clicked")
            wait = WebDriverWait(self.driver,time_out= timeout, poll_frequency= pollfrequency, ignored_exceptions= [ElementNotVisibleException,
                                                                                                        ElementNotSelectableException,
                                                                                                        NoSuchElementException])
            element = wait.until(EC.element_to_be_clickable(ele))
            element.click()
            self.log.info("Element appeared on web page using locator" + xpath)
        except:
            self.log.error("Element not appeared on web page using locator" + xpath)
            print_stack()

        return element

    def doubleClickByXpath(self, xpath):
        """
        double Click using Xpath locator
        :param xpath: get xpath locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_xpath(xpath)
            actions = ActionChains(self.driver)
            actions.double_click(element).perform()
            self.log.info("Double clicked by xpath locator: " + xpath)
        except:
            self.log.error("Cannot double click by xpath locator: " + xpath)
            print_stack()

    def clickByXpath(self, xpath):
        """
        Click using Xpath locator
        :param xpath: get xpath locator
        :return: does not return
        """
        try:
            WebDriverWait(self.driver, 20,poll_frequency= 1).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element_by_xpath(xpath)
            element.click()
            self.log.info("clicked by xpath locator: " + xpath)
        except:
            self.log.error("Cannot be clicked by xpath locator: " + xpath)
            print_stack()

    def clickById(self, id):
        """
        Click using Id locator
        :param id: get Id locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_id(id)
            element.click()
            self.log.info("clicked by id locator: " + id)
        except:
            self.log.error("Cannot be clicked by id locator: " + id)
            print_stack()

    def clickByName(self, name):
        """
        Click using name locator
        :param name: get name locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_name(name)
            element.click()
            self.log.info("clicked by name locator: " + name)
        except:
            self.log.error("Cannot be clicked by name locator: " + name)
            print_stack()

    def clickByClassName(self, class_name):
        """
        Click using class name locator
        :param class_name: get class name locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_class_name(class_name)
            element.click()
            self.log.info("clicked by class name locator: " + class_name)
        except:
            self.log.error("Cannot be clicked using class name locator: " + class_name)
            print_stack()

    def clickByTagName(self, tag_name):
        """
        click using tag name locator
        :param tag_name: get tag name locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_tag_name(tag_name)
            element.click()
            self.log.info("clicked by tag name locator: " + tag_name)
        except:
            self.log.error("Cannot be clicked by using tag name locator: " + tag_name)
            print_stack()

    def clickByLinkText(self, link_text):
        """
        click using link text locator
        :param link_text: get link text locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_link_text(link_text)
            element.click()
            self.log.info("clicked by link text locator: " + link_text)
        except:
            self.log.error("Cannot be clicked by link text locator: " + link_text)
            print_stack()

    def clickByCssSelector(self, css_selector):
        """
        click using css selector locator
        :param css_selector: get css selector locator
        :return: does not return
        """
        try:
            element = driver.find_element_by_css_selector(css_selector)
            element.click()
            self.log.info("clicked by css locator: " + css_selector)
        except:
            self.log.error("Cannot be clicked by css selector locator: " + css_selector)
            print_stack()

    def switchToFrameByIndexBasedOnXpath(self, xpath):
        """
        switching to the frame based on index based on given xpath locator
        :param xpath: get xpath locator
        :return: does not return
        """
        try:
            iframeList  = driver.find_elements_by_xpath("//iframe")
            for i in range(len(iframeList)):
                self.driver.switch_to.frame(iframeList[i])
                result = self.isElementPresentByXpath(xpath)
                if result:
                    self.log.info("Switched to Frame " + iframeList[i])
                    break
                self.switchToDefaultFrame()
                self.log.info("Switched to default Frame")
        except:
            self.log.info("Iframe not found for xpath locator :" + xpath)
            print_stack()

    def switchToDefaultFrame(self):
        """
        switch to default frame
        :return: doenot return
        """
        try:
            self.driver.switch_to.default_content()
            self.log.info("Switched to default Frame")
        except:
            self.log.error("Cannot Switched to default Frame")
            print_stack()

    def switchToFrameByXpath(self, xpath):
        """
        Switching to frame using xpath locator
        :param xpath: get xpath locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            self.driver.switch_to.frame(ele)
            self.log.info("Switched to Frame by xpath locator: " + xpath)
        except:
            self.log.error("Cannot Switched to Frame by xpath locator: " + xpath)
            print_stack()

    def switchToFrameById(self, id):
        """
        Switching to frame using id locator
        :param id: get id locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_id(id)
            self.driver.switch_to.frame(ele)
            self.log.info("Switched to Frame by id locator: " + id)
        except:
            self.log.error("Cannot Switched to Frame by id locator: " + id)
            print_stack()

    def switchToFrameByName(self, name):
        """
        Switching to frame using name locator
        :param id: get name locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_name(name)
            self.driver.switch_to.frame(ele)
            self.log.info("Switched to Frame by name locator: " + name)
        except:
            self.log.error("Cannot Switched to Frame by name locator: " + name)
            print_stack()

    def switchToFrameOnlyByIndex(self, index):
        """
        Switching to frame using given frame index
        :param index: get frame index
        :return: does not return
        """
        try:
            self.driver.switch_to.frame(index)
            self.log.info("Switched to Frame by Index: " + str(index))
        except:
            self.log.error("Cannot Switched to Frame by Index: " + str(index))
            print_stack()

    def dragAndDropById(self, fromId, toId):
        """
        Drag and drop element from source to target using id locator
        :param fromID: get source of id locator
        :param toID: get target of id locator
        :return: does not return
        """
        try:
            src = self.driver.find_element_by_id(fromId)
            target = self.driver.find_element_by_id(toId)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(src, target).perform()
            self.log.info("Drag and Drop succcesful using FROM ID locator: " + fromId + " and TO ID locator :" + toId)
        except:
            self.log.error("Drag and Drop unsucccesful using FROM ID locator: " + fromId +" and TO ID locator :" + toId)

    def dragAndDropByName(self, fromName, toName):
        """
        Drag and drop element from source to target using name locator
        :param fromName: get source of name locator
        :param toName: get target of name locator
        :return: does not return
        """
        try:
            src = self.driver.find_element_by_name(fromName)
            target = self.driver.find_element_by_name(toName)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(src, target).perform()
            self.log.info("Drag and Drop succcesful using FROM name locator: " + fromName + " and TO name locator :" + toName)
        except:
            self.log.error("Drag and Drop unsucccesful using FROM name locator: " + fromName +" and TO name locator :" + toName)

    def dragAndDropByXpath(self, fromXpath, toXpath):
        """
        Drag and drop element from source to target using xpath locator
        :param fromXpath: get source of xpath locator
        :param toXpath: get target of xpath locator
        :return: does not return
        """
        try:
            src = self.driver.find_element_by_xpath(fromXpath)
            target = self.driver.find_element_by_xpath(toXpath)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(src, target).perform()
            self.log.info("Drag and Drop succcesful using FROM xpath locator: " + fromXpath + " and TO xpath locator :" + toXpath)
        except:
            self.log.error("Drag and Drop unsucccesful using FROM xpath locator: " + fromXpath +" and TO xpath locator :" + toXpath)

    def clearTextByXpath(self, xpath):
        """
        Clear the text in the web page using Xpath locator
        :param xpath: get xpath locator
        :return: does not return
        """
        try:
            element = self.driver.find_element_by_xpath(xpath)
            element.clear()
            self.log.info("cleared text in xpath locator: " + xpath)
        except:
            self.log.error("Cannot clear text using xpath locator: " + xpath)
            print_stack()

    def dragAndDropByClassName(self, fromClassName, toClassName):
        """
        Drag and drop element from source to target using ClassName locator
        :param fromClassName: get source of ClassName locator
        :param toClassName: get target of ClassName locator
        :return: does not return
        """
        try:
            src = self.driver.find_element_by_class_name(fromClassName)
            target = self.driver.find_element_by_class_name(toClassName)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(src, target).perform()
            self.log.info("Drag and Drop succcesful using FROM ClassName locator: " + fromClassName + " and TO ClassName locator :" + toClassName)
        except:
            self.log.error("Drag and Drop unsucccesful using FROM ClassName locator: " + fromClassName +" and TO ClassName locator :" + toClassName)


    def dragAndDropByTagName(self, fromTagName, toTagName):
        """
        Drag and drop element from source to target using TagName locator
        :param fromTagName: get source of TagName locator
        :param toTagName: get target of TagName locator
        :return: does not return
        """
        try:
            src = self.driver.find_element_by_tag_name(fromTagName)
            target = self.driver.find_element_by_tag_name(toTagName)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(src, target).perform()
            self.log.info("Drag and Drop succcesful using FROM TagName locator: " + fromTagName + " and TO TagName locator :" + toTagName)
        except:
            self.log.error("Drag and Drop unsucccesful using FROM TagName locator: " + fromTagName + " and TO TagName locator :" + toTagName)

    def dragAndDropByLinkText(self, fromLinkText, toLinkText):
        """
        Drag and drop element from source to target using Link text locator
        :param fromLinkText: get source of Link text locator
        :param toLinktext: get target of Link text locator
        :return: does not return
        """
        try:
            src = self.driver.find_element_by_link_text(fromLinkText)
            target = self.driver.find_element_by_link_text(toLinkText)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(src, target).perform()
            self.log.info("Drag and Drop succcesful using FROM Link text locator: " + fromLinkText + " and TO Link text locator :" + toLinkText)
        except:
            self.log.error("Drag and Drop unsucccesful using FROM Link text locator: " + fromLinkText + " and TO Link text locator :" + toLinkText)

    def dragAndDropByCssSelector(self, fromCssSelector, toCssSelector):
        """
        Drag and drop element from source to target using CssSelector locator
        :param fromCssSelector: get source of CssSelector locator
        :param toCssSelector: get target of CssSelector locator
        :return: does not return
        """
        try:
            src = self.driver.find_element_by_link_text(fromCssSelector)
            target = self.driver.find_element_by_link_text(toCssSelector)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(src, target).perform()
            self.log.info("Drag and Drop succcesful using FROM CssSelector locator: " + fromCssSelector + " and TO CssSelector locator :" + toCssSelector)
        except:
            self.log.error("Drag and Drop unsucccesful using FROM CssSelector locator: " + fromCssSelector + " and TO CssSelector locator :" + toCssSelector)

    def javascriptExecutor(self, statement):
        """
        Execute the given javascript line
        :param statement: get javascript statement
        :return: does not return
        """
        try:
            self.driver.execute_script(statement)
            self.log.info("JavaScript statement is executed :" + statement)
        except:
            self.log.error("JavaScript statement is not executed :" + statement)
            print_stack()

    def implicitwait(self, sec):
        """
        :param sec: get number of seconds for implicit wait
        :return: does not return
        """
        try:
            self.driver.implicitly_wait(sec)
            self.log.info("waited for :" + str(sec) + " seconds")
        except:
            self.log.info("not waited for :" + str(sec) + " seconds")
            print_stack()

    def threadSleep(self, sec):
        """
        explicit wait for given number of seconds
        :param sec: get number of seconds for explicit wait
        :return: does not return
        """
        try:
            time.sleep(sec)
            self.log.info("waited for :" + str(sec) + " seconds")
        except:
            self.log.info("not waited for :" + str(sec) + " seconds")
            print_stack()

    def fileUploadById(self, id, filePath):
        """
        upload the file from the given file path
        :param id: get the id locator
        :param filePath: get file path to upload
        :return: does not return
        """
        try:
            self.driver.find_element_by_id(id).send_keys(filePath)
            self.log.info("File uploaded sucessfully using id locator :" + id + " from the filepath: "+ filePath)
        except:
            self.log.error("File upload unsucessful using id locator :" + id + " from the filepath: " + filePath)
            print_stack()

    def fileUploadByName(self, name, filePath):
        """
        upload the file from the given file path
        :param name: get the name locator
        :param filePath: get file path to upload
        :return: does not return
        """
        try:
            self.driver.find_element_by_name(name).send_keys(filePath)
            self.log.info("File uploaded sucessfully using name locator :" + name + " from the filepath: "+ filePath)
        except:
            self.log.error("File upload unsucessful using name locator :" + name + " from the filepath: " + filePath)
            print_stack()

    def fileUploadByXpath(self, xpath, filePath):
        """
        upload the file from the given file path
        :param name: get the xpath locator
        :param filePath: get file path to upload
        :return: does not return
        """
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(filePath)
            self.log.info("File uploaded sucessfully using xpath locator :" + xpath + " from the filepath: "+ filePath)
        except:
            self.log.error("File upload unsucessful using xpath locator :" + xpath + " from the filepath: " + filePath)
            print_stack()

    def fileUploadByClassName(self, className, filePath):
        """
        upload the file from the given file path
        :param name: get the className locator
        :param filePath: get file path to upload
        :return: does not return
        """
        try:
            self.driver.find_element_by_class_name(className).send_keys(filePath)
            self.log.info("File uploaded sucessfully using xpath locator :" + className + " from the filepath: "+ filePath)
        except:
            self.log.error("File upload unsucessful using xpath locator :" + className + " from the filepath: " + filePath)
            print_stack()

    def fileUploadByTagName(self, tagName, filePath):
        """
        upload the file from the given file path
        :param name: get the tagName locator
        :param filePath: get file path to upload
        :return: does not return
        """
        try:
            self.driver.find_element_by_tag_name(tagName).send_keys(filePath)
            self.log.info("File uploaded sucessfully using xpath locator :" + tagName + " from the filepath: "+ filePath)
        except:
            self.log.error("File upload unsucessful using xpath locator :" + tagName + " from the filepath: " + filePath)
            print_stack()

    def fileUploadByLinkText(self, linkText, filePath):
        """
        upload the file from the given file path
        :param name: get the LinkText locator
        :param filePath: get file path to upload
        :return: does not return
        """
        try:
            self.driver.find_element_by_link_text(linkText).send_keys(filePath)
            self.log.info("File uploaded sucessfully using LinkText locator :" + linkText + " from the filepath: "+ filePath)
        except:
            self.log.error("File upload unsucessful using LinkText locator :" + linkText + " from the filepath: " + filePath)
            print_stack()

    def fileUploadByCssSelector(self, cssSelector, filePath):
        """
        upload the file from the given file path
        :param name: get the cssSelector locator
        :param filePath: get file path to upload
        :return: does not return
        """
        try:
            self.driver.find_element_by_css_selector(cssSelector).send_keys(filePath)
            self.log.info("File uploaded sucessfully using cssSelector locator :" + cssSelector + " from the filepath: "+ filePath)
        except:
            self.log.error("File upload unsucessful using cssSelector locator :" + cssSelector + " from the filepath: " + filePath)
            print_stack()

    def tabOperationById(self, id):
        """
        perform Tab operation using id locator
        :param id: get id locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_id(id)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.TAB).perform()
            self.log.info("Tab operation is performed using id locator"+ id)
        except:
            self.log.error("Tab operation is unsuccessful using id locator"+ id)
            print_stack()

    def tabOperationByName(self, name):
        """
        perform Tab operation using name locator
        :param name: get name locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_name(name)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.TAB).perform()
            self.log.info("Tab operation is performed using name locator"+ name)
        except:
            self.log.error("Tab operation is unsuccessful using name locator"+ name)
            print_stack()

    def tabOperationByXpath(self, xpath):
        """
        perform Tab operation using xpath locator
        :param xpath: get xpath locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.TAB).perform()
            self.log.info("Tab operation is performed using xpath locator"+ xpath)
        except:
            self.log.error("Tab operation is unsuccessful using xpath locator"+ xpath)
            print_stack()

    def tabOperationByClassName(self, className):
        """
        perform Tab operation using className locator
        :param className: get className locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_class_name(className)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.TAB).perform()
            self.log.info("Tab operation is performed using ClassName locator" + className)
        except:
            self.log.error("Tab operation is unsuccessful using ClassName locator" + className)
            print_stack()

    def tabOperationByTagName(self, tagName):
        """
        perform Tab operation using tagName locator
        :param tagName: get TagName locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_tag_name(tagName)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.TAB).perform()
            self.log.info("Tab operation is performed using TagName locator" + tagName)
        except:
            self.log.error("Tab operation is unsuccessful using TagName locator" + tagName)
            print_stack()

    def tabOperationByLinkText(self, linktext):
        """
        perform Tab operation using linktext locator
        :param linktext: get linktext locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_tag_name(linktext)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.TAB).perform()
            self.log.info("Tab operation is performed using linktext locator" + linktext)
        except:
            self.log.error("Tab operation is unsuccessful using linktext locator" + linktext)
            print_stack()

    def tabOperationByCssSelector(self, cssSelector):
        """
        perform Tab operation using cssSelector locator
        :param cssSelector: get cssSelector locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_tag_name(cssSelector)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.TAB).perform()
            self.log.info("Tab operation is performed using cssSelector locator" + cssSelector)
        except:
            self.log.error("Tab operation is unsuccessful using cssSelector locator" + cssSelector)
            print_stack()

    def enterOperationById(self, id):
        """
        perform enter operation using id locator
        :param id: get id locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_id(id)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
            self.log.info("ENTER operation is performed using id locator" + id)
        except:
            self.log.error("ENTER operation is unsuccessful using id locator" + id)
            print_stack()

    def enterOperationByName(self, name):
        """
        perform enter operation using name locator
        :param name: get name locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_name(name)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
            self.log.info("ENTER operation is performed using name locator" + name)
        except:
            self.log.error("ENTER operation is unsuccessful using name locator" + name)
            print_stack()

    def enterOperationByXpath(self, xpath):
        """
        perform enter operation using xpath locator
        :param xpath: get xpath locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
            self.log.info("ENTER operation is performed using xpath locator" + xpath)
        except:
            self.log.error("ENTER operation is unsuccessful using xpath locator" + xpath)
            print_stack()

    def enterOperationByClassName(self, className):
        """
        perform ENTER operation using className locator
        :param className: get className locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_class_name(className)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
            self.log.info("ENTER operation is performed using ClassName locator" + className)
        except:
            self.log.error("ENTER operation is unsuccessful using ClassName locator" + className)
            print_stack()

    def enterOperationByTagName(self, tagName):
        """
        perform ENTER operation using tagName locator
        :param tagName: get TagName locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_tag_name(tagName)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
            self.log.info("ENTER operation is performed using TagName locator" + tagName)
        except:
            self.log.error("ENTER operation is unsuccessful using TagName locator" + tagName)
            print_stack()

    def enterOperationByLinkText(self, linktext):
        """
        perform ENTER operation using linktext locator
        :param linktext: get linktext locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_tag_name(linktext)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
            self.log.info("ENTER operation is performed using linktext locator" + linktext)
        except:
            self.log.error("ENTER operation is unsuccessful using linktext locator" + linktext)
            print_stack()

    def enterOperationByCssSelector(self, cssSelector):
        """
        perform ENTER operation using cssSelector locator
        :param cssSelector: get cssSelector locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_tag_name(cssSelector)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
            self.log.info("ENTER operation is performed using cssSelector locator" + cssSelector)
        except:
            self.log.error("ENTER operation is unsuccessful using cssSelector locator" + cssSelector)
            print_stack()

    def refreshpage(self):
        """
        refresh the current web page
        :return: does not return
        """
        try:
            self.driver.refresh()
            self.log.info("WebPage Refreshed")
        except:
            self.log.error("WebPage Refresh failed")
            print_stack()

    def goforwardpage(self):
        """
        go forward from current webpage
        :return: does not return
        """
        try:
            self.driver.forward()
            self.log.info("WebPage Forwarded")
        except:
            self.log.error("WebPage Forward failed")
            print_stack()

    def gobackpage(self):
        """
        go back from current webpage
        :return: does not return
        """
        try:
            self.driver.back()
            self.log.info("Go to Back WebPage")
        except:
            self.log.error("Go to Back WebPage failed")
            print_stack()

    def closeAllBrowsers(self):
        """
        Close the browser window
        :return: does not return
        """
        try:
            self.driver.quit()
            self.log.info("Browser is closed")
        except:
             self.log.error("Browser Close Failed")
             print_stack()

    def closeWindow(self):
        def closeAllBrowsers(self):
            """
            Close the current browser window
            :return: does not return
            """
            try:
                self.driver.close()
                self.log.info("Closed the current window in Browser")
            except:
                self.log.error("Current window Close is Failed")
                print_stack()

    def acceptAlert(self):
        """
        accept the alert
        :return: does not return
        """
        try:
            self.driver.switch_to.alert.accept()
            self.log.info("Accept the Alert")
        except:
            self.log.error("Accepting the Alert Failed")
            print_stack()

    def dismissAlert(self):
        """
        dismiss the alert
        :return: does not return
        """
        try:
            self.driver.switch_to.alert.dismiss()
            self.log.info("Dismiss the Alert")
        except:
            self.log.error("Dismissing the Alert Failed")
            print_stack()

    def getAlertText(self):
        """
         get the text from alert
         :return: does not return
         """
        try:
            text = self.driver.switch_to.alert.text
            self.log.info("Text in Alert is " + text)
        except:
            self.log.error("Getting Text from Alert Failed" + text)
            print_stack()
        return text

    def mouseOverByXpath(self, xpath):
        """
        perform mouse hover using xpath locator
        :param xpath: get xpath locator
        :return: doesnot return
        """
        try:
            actions = ActionChains(self.driver)
            ele = self.driver.find_element_by_xpath(xpath)
            actions.move_to_element(ele).perform()
            self.log.info("Mouse Hover is performed using xpath locator" + xpath)
        except:
            self.log.error("Mouse Hover failed using xpath locator" + xpath)
            print_stack()

    def mouseOverById(self, id):
        """
        perform mouse hover using id locator
        :param id: get id locator
        :return: doesnot return
        """
        try:
            actions = ActionChains(self.driver)
            ele = self.driver.find_element_by_id(id)
            actions.move_to_element(ele).perform()
            self.log.info("Mouse Hover is performed using id locator" + id)
        except:
            self.log.error("Mouse Hover failed using id locator" + id)
            print_stack()

    def mouseOverByname(self, name):
        """
        perform mouse hover using name locator
        :param name: get name locator
        :return: doesnot return
        """
        try:
            actions = ActionChains(self.driver)
            ele = self.driver.find_element_by_name(name)
            actions.move_to_element(ele).perform()
            self.log.info("Mouse Hover is performed using name locator" + name)
        except:
            self.log.error("Mouse Hover failed using name locator" + name)
            print_stack()

    def mouseOverByClassname(self, classname):
        """
        perform mouse hover using classname locator
        :param classname: get classname locator
        :return: doesnot return
        """
        try:
            actions = ActionChains(self.driver)
            ele = self.driver.find_element_by_class_name(classname)
            actions.move_to_element(ele).perform()
            self.log.info("Mouse Hover is performed using name locator" + classname)
        except:
            self.log.error("Mouse Hover failed using name locator" + classname)
            print_stack()

    def selectValueByXpath(self, xpath, value):
        """
         select value using xpath locator
         :param xpath: get xpath locator
         :param value: get value to select
         :return: doesnot return
         """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            sel = Select(ele)
            sel.select_by_value(value)
            self.log.info("Selected value: " + value + " using xpath locator" + xpath)
        except:
            self.log.error("Select value Failed: " + value + " using xpath locator" + xpath)
            print_stack()

    def selectValueByid(self, id, value):
        """
         select value using id locator
         :param id: get id locator
         :param value: get value to select
         :return: doesnot return
         """
        try:
            ele = self.driver.find_element_by_id(id)
            sel = Select(ele)
            sel.select_by_value(value)
            self.log.info("Selected value: " + value + " using id locator" + id)
        except:
            self.log.error("Select value Failed: " + value + " using id locator" + id)
            print_stack()

    def selectValueByName(self , name, value):
        """
         select value using name locator
         :param name: get name locator
         :param value: get value to select
         :return: doesnot return
         """
        try:
            ele = self.driver.find_element_by_name(name)
            sel = Select(ele)
            sel.select_by_value(value)
            self.log.info("Selected value: " + value + " using name locator" + name)
        except:
            self.log.error("Select value Failed: " + value + " using name locator" + name)
            print_stack()

    def selectValueByClassName(self , classname, value):
        """
         select value using classname locator
         :param classname: get classname locator
         :param value: get value to select
         :return: doesnot return
         """
        try:
            ele = self.driver.find_element_by_class_name(classname)
            sel = Select(ele)
            sel.select_by_value(value)
            self.log.info("Selected value: " + value + " using class name locator" + classname)
        except:
            self.log.error("Select value Failed: " + value + " using class name locator" + classname)
            print_stack()

    def selectVisibileTextByXpath(self, xpath, value):
        """
         select visible using xpath locator
         :param xpath: get xpath locator
         :param value: get value to select
         :return: doesnot return
         """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            sel = Select(ele)
            sel.select_by_visible_text(value)
            self.log.info("Selected visible text: " + value + " using xpath locator" + xpath)
        except:
            self.log.error("Select visible text Failed: " + value + " using xpath locator" + xpath)
            print_stack()

    def selectVisibileTextById(self, id, value):
        """
         select visible using id locator
         :param id: get id locator
         :param value: get value to select
         :return: doesnot return
         """
        try:
            ele = self.driver.find_element_by_id(id)
            sel = Select(ele)
            sel.select_by_visible_text(value)
            self.log.info("Selected visible text: " + value + " using id locator" + id)
        except:
            self.log.error("Select visible text Failed: " + value + " using id locator" + id)
            print_stack()

    def selectVisibileTextByName(self, name, value):
        """
         select visible using name locator
         :param name: get name locator
         :param value: get value to select
         :return: doesnot return
         """
        try:
            ele = self.driver.find_element_by_name(name)
            sel = Select(ele)
            sel.select_by_visible_text(value)
            self.log.info("Selected visible text: " + value + " using name locator" + name)
        except:
            self.log.error("Select visible text Failed: " + value + " using name locator" + name)
            print_stack()

    def selectVisibileTextByClassName(self, classname, value):
        """
         select visible using classname locator
         :param classname: get classname locator
         :param value: get value to select
         :return: doesnot return
         """
        try:
            ele = self.driver.find_element_by_class_name(classname)
            sel = Select(ele)
            sel.select_by_visible_text(value)
            self.log.info("Selected visible text: " + value + " using classname locator" + classname)
        except:
            self.log.error("Select visible text Failed: " + value + " using classname locator" + classname)
            print_stack()

    def selectIndexByXpath(self, xpath, index):
        """
         select value by index using xpath locator
         :param xpath: get xpath locator
         :param index: get value to select
         :return: doesnot return
         """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            sel = Select(ele)
            sel.select_by_index(index)
            self.log.info("Selected visible text: " + index + " using name locator" + xpath)
        except:
            self.log.error("Select visible text Failed: " + index + " using name locator" + xpath)
            print_stack()

    def selectIndexById(self, id, index):
        """
         select value by index using id locator
         :param id: get id locator
         :param index: get value to select
         :return: does not return
         """
        try:
            ele = self.driver.find_element_by_id(id)
            sel = Select(ele)
            sel.select_by_index(index)
            self.log.info("Selected visible text: " + index + " using id locator" + id)
        except:
            self.log.error("Select visible text Failed: " + index + " using id locator" + id)
            print_stack()

    def selectIndexByName(self, name, index):
        """
         select value by index using name locator
         :param name: get name locator
         :param index: get value to select
         :return: does not return
         """
        try:
            ele = self.driver.find_element_by_name(name)
            sel = Select(ele)
            sel.select_by_index(index)
            self.log.info("Selected visible text: " + index + " using name locator" + name)
        except:
            self.log.error("Select visible text Failed: " + index + " using name locator" + name)
            print_stack()

    def selectIndexByClassName(self, classname, index):
        """
         select value by index using ClassName locator
         :param classname: get ClassName locator
         :param index: get value to select
         :return: doe snot return
         """
        try:
            ele = self.driver.find_element_by_class_name(classname)
            sel = Select(ele)
            sel.select_by_index(index)
            self.log.info("Selected visible text: " + index + " using classname locator" + classname)
        except:
            self.log.error("Select visible text Failed: " + index + " using classname locator" + classname)
            print_stack()

    def switchToNewWindow(self):
        """
        Switch to new window
        :return: does not return
        """
        try:
            #get window session id of current opened window
            phandle = self.driver.current_window_handle
            # get window session id of all the opened windows
            handles = self.driver.window_handles
            for handle in handles:
                if handle not in phandle:
                    self.driver.switch_to.window(handle)
                    self.log.info("Switched to new window:" + handle)
                    break
        except:
            self.log.error("Switch to new window failed")
            print_stack()

    def switchToMainWindow(self):
        """
         Switch to Main window
         :return: does not return
         """
        try:
            #get window session id of current opened window
            phandle = self.driver.current_window_handle
            self.driver.switch_to.window(phandle)
            self.log.info("Switched to Main window:" + phandle)
        except:
            self.log.error("Switch to Main window failed")
            print_stack()

    def verifyTextById(self, id, expectedText):
        """
        verify the text using id locator
        :param id: get id locator
        :param expectedText: get the text to verify
        :return: does not return
        """
        try:
            actualText= self.driver.find_element_by_id(id).text
            if actualText in expectedText:
                self.log.info("Actal Text: "+ actualText +" matched using id locator: " + id + " with Entered Text: " + expectedText)
        except:
            self.log.error("Actal Text: "+ actualText +" doesnot match using id locator: " + id + "  Entered Text: " + expectedText)
            print_stack()

    def verifyTextByName(self, name, expectedText):
        """
        verify the text using name locator
        :param name: get name locator
        :param expectedText: get the text to verify
        :return: does not return
        """
        try:
            actualText= self.driver.find_element_by_name(name).text
            if actualText in expectedText:
                self.log.info("Actal Text: "+ actualText +" matched using name locator: " + name + " with Entered Text: " + expectedText)
        except:
            self.log.error("Actal Text: "+ actualText +" doesnot match using name locator: " + name + " with Entered Text:: " + expectedText)
            print_stack()

    def verifyTextByXpath(self, xpath, expectedText):
        """
        verify the text using xpath locator
        :param xpath: get xpath locator
        :param expectedText: get the text to verify
        :return: does not return
        """
        try:
            actualText= self.driver.find_element_by_xpath(xpath).text
            if actualText in expectedText:
                self.log.info("Actal Text: "+ actualText +" matched using xpath locator: " + xpath + " with Entered Text: " + expectedText)
        except:
            self.log.error("Actal Text: "+ actualText +" doesnot match using xpath locator: " + xpath + " with Entered Text:: " + expectedText)
            print_stack()

    def verifyTextByClassName(self, classname, expectedText):
        """
        verify the text using classname locator
        :param classname: get classname locator
        :param expectedText: get the text to verify
        :return: does not return
        """
        try:
            actualText = self.driver.find_element_by_class_name(classname).text
            if actualText in expectedText:
                self.log.info("Actal Text: " + actualText + " matched using classname locator: " + classname + " with Entered Text: " + expectedText)
        except:
            self.log.error("Actal Text: " + actualText + " doesnot match using classname locator: " + classname + " with Entered Text:: " + expectedText)
            print_stack()

    def verifyTextByTagName(self, tagname, expectedText):
        """
        verify the text using tagname locator
        :param tagname: get tagname locator
        :param expectedText: get the text to verify
        :return: does not return
        """
        try:
            actualText = self.driver.find_element_by_tag_name(tagname).text
            if actualText in expectedText:
                self.log.info("Actal Text: " + actualText + " matched using tagname locator: " + tagname + " with Entered Text: " + expectedText)
        except:
            self.log.error("Actal Text: " + actualText + " doesnot match using tagname locator: " + tagname + " with Entered Text:: " + expectedText)
            print_stack()

    def verifyTextByLinkText(self, linkText, expectedText):
        """
        verify the text using linkText locator
        :param linkText: get linkText locator
        :param expectedText: get the text to verify
        :return: does not return
        """
        try:
            actualText = self.driver.find_element_by_link_text(linkText).text
            if actualText in expectedText:
                self.log.info("Actal Text: " + actualText + " matched using linkText locator: " + linkText + " with Entered Text: " + expectedText)
        except:
            self.log.error("Actal Text: " + actualText + " doesnot match using linkText locator: " + linkText + " with Entered Text:: " + expectedText)
            print_stack()

    def verifyTextByCssSelector(self, cssSelector, expectedText):
        """
        verify the text using cssSelector locator
        :param cssSelector: get cssSelector locator
        :param expectedText: get the text to verify
        :return: does not return
        """
        try:
            actualText = self.driver.find_element_by_css_selector(cssSelector).text
            if actualText in expectedText:
                self.log.info("Actal Text: " + actualText + " matched using cssSelector locator: " + cssSelector + " with Entered Text: " + expectedText)
        except:
            self.log.error("Actal Text: " + actualText + " doesnot match using cssSelector locator: " + cssSelector + " with Entered Text:: " + expectedText)
            print_stack()

    def scrollToElementById(self, id):
        """
        scroll down to element by id locator
        :param id: get id locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_id(id)
            self.driver.execute_script("window.scrollBy(argument[0].scrollintoview(true);", ele)
            self.driver.execute_script("window.scrollBy(0,150);")
            self.log.info("scrolled down to the element by id locator: "+ id)
        except:
            self.log.error("Cannot scrolled down to the element by id locator: "+ id)
            print_stack()

    def scrollToElementByName(self, name):
        """
        scroll down to element by name locator
        :param name: get name locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_name(name)
            self.driver.execute_script("window.scrollBy(argument[0].scrollintoview(true);", ele)
            self.driver.execute_script("window.scrollBy(0,150);")
            self.log.info("scrolled down to the element by name locator: "+ name)
        except:
            self.log.error("Cannot scrolled down to the element by name locator: "+ name)
            print_stack()

    def scrollToElementByXpath(self, xpath):
        """
        scroll down to element by xpath locator
        :param name: get xpath locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script("window.scrollBy(argument[0].scrollintoview(true);", ele)
            self.driver.execute_script("window.scrollBy(0,150);")
            self.log.info("scrolled down to the element by xpath locator: "+ xpath)
        except:
            self.log.error("Cannot scrolled down to the element by xpath locator: "+ xpath)
            print_stack()

    def scrollToElementByClassName(self, className):
        """
        scroll down to element by className locator
        :param className: get className locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_class_name(className)
            self.driver.execute_script("window.scrollBy(argument[0].scrollintoview(true));", ele)
            self.driver.execute_script("window.scrollBy(0,150);")
            self.log.info("scrolled down to the element by className locator: " + className)
        except:
            self.log.error("Cannot scrolled down to the element by className locator: " + className)
            print_stack()

    def scrollToElementByTagName(self, tagName):
        """
        scroll down to element by tagName locator
        :param tagName: get tagName locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_tag_name(tagName)
            self.driver.execute_script("window.scrollBy(argument[0].scrollintoview(true);", ele)
            self.driver.execute_script("window.scrollBy(0,150);")
            self.log.info("scrolled down to the element by tagName locator: " + tagName)
        except:
            self.log.error("Cannot scrolled down to the element by tagName locator: " + tagName)
            print_stack()

    def scrollToElementByCssSelector(self, cssSelector):
        """
        scroll down to element by cssSelector locator
        :param cssSelector: get cssSelector locator
        :return: does not return
        """
        try:
            ele = self.driver.find_element_by_css_selector(cssSelector)
            self.driver.execute_script("window.scrollBy(argument[0].scrollintoview(true);", ele)
            self.driver.execute_script("window.scrollBy(0,150);")
            self.log.info("scrolled down to the element by cssSelector locator: " + cssSelector)
        except:
            self.log.error("Cannot scrolled down to the element by cssSelector locator: " + cssSelector)
            print_stack()

    def slidingVerticallyById(self, id):
        """
          sliding vertically using id locator
          :param id: get id locator
          :return: does not return
          """
        try:
            ele = self.driver.find_element_by_id(id)
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(ele, 100, 0).perform()
            self.log.info("Sliding vertically by id locator: " + id)
        except:
            self.log.error("Sliding vertically Failed by id locator: " + id)
            print_stack()

    def slidingVerticallyByXpathWithRange(self, slider_xpath,slider_range_percent_xpath,slider_range_percent):
        """
          sliding vertically using xpath locator for mentioned range
          :param slider_xpath: get xpath locator
          :param slider_range_percent_xpath: get xpath of percentage
          :param slider_range_percent: get percentage range to slode
          :return: does not return
          """
        try:
            actions = ActionChains(self.driver)
            slider = self.driver.find_element_by_xpath(slider_xpath)
            slider.location_once_scrolled_into_view
            self.driver.execute_script("window.scrollBy(0,200);")
            for i in range(0, 100):
                actions.click_and_hold(slider).move_by_offset(i, 0).release().perform()
                slider_range = self.driver.find_element_by_xpath(slider_range_percent_xpath).text
                arr = list(re.split("%", slider_range))
                if arr[0] == slider_range_percent:
                    self.log.info("PASS::slider changed to %"+str(slider_range_percent))
                    break
        except:
            self.log.error("Sliding vertically Failed by xpath locator: " + slider_xpath)
            print_stack()

    def slidingVerticallyByXpath(self, xpath):
        """
          sliding vertically using xpath locator
          :param xpath: get xpath locator
          :return: does not return
          """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(ele, 100, 0).perform()
            self.log.info("Sliding vertically by xpath locator: " + xpath)
        except:
            self.log.error("Sliding vertically Failed by xpath locator: " + xpath)
            print_stack()

    def slidingVerticallyByClassName(self, classname):
        """
          sliding vertically using classname locator
          :param classname: get classname locator
          :return: does not return
          """
        try:
            ele = self.driver.find_element_by_class_name(classname)
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(ele, 100, 0).perform()
            self.log.info("Sliding vertically by classname locator: " + classname)
        except:
            self.log.error("Sliding vertically Failed by classname locator: " + classname)
            print_stack()

    def slidingVerticallyByName(self, name):
        """
          sliding vertically using name locator
          :param name: get name locator
          :return: does not return
          """
        try:
            ele = self.driver.find_element_by_xpath(name)
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(ele, 100, 0).perform()
            self.log.info("Sliding vertically by name locator: " + name)
        except:
            self.log.error("Sliding vertically Failed by name locator: " + name)
            print_stack()