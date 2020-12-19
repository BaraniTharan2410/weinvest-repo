"""
@package utils

CheckPoint class implementation
It provides functionality to assert the result

"""

import logging
from traceback import print_stack
from base.seleniumwebdriver import SeleniumDriver
import utils.customlogger as cl

class TestStatus(SeleniumDriver):

    log = cl.consoleLogger(logging.DEBUG)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.list = []

    def setResult(self,result,resultmessage):
        try:
            if result is not None:
                if result:
                    self.list.append('PASS')
                    self.log.info("VERIFICATION SUCCESSFUL"+resultmessage)
                else:
                    self.list.append('FAIL')
                    self.log.error("VERIFICATION FAILED" + resultmessage)
                    self.takeScreenshot(resultmessage)
            else:
                self.list.append('FAIL')
                self.log.error("VERIFICATION FAILED" + resultmessage)
                self.takeScreenshot(resultmessage)
        except:
            self.list.append('FAIL')
            self.log.error("Exception occured")
            self.takeScreenshot(resultmessage)
            print_stack()
    def mark(self,result,resultmessage):
        """
        mark the result of verification point in the testcase
        :param result: get result of the test
        :param message: get message to displayed
        :return: None
        """
        self.setResult(result,resultmessage)
    def markfinal(self,testname,result,resultmessage):
        """
          mark the final result of verification point in the testcase
          this should be called atleast once on testcase
          this should be final test status of the testcase
          :param result: get result of the test
          :param resultMessage: get message to displayed
          :return: None
          """
        self.setResult(result, resultmessage)
        if "FAIL" in self.list:
            self.log.error(testname+" ##### TEST FAILED")
            self.list.clear()
            assert True == False
        else:
            self.log.info(testname + " ##### TEST PASSED")
            self.list.clear()
            assert True == True

