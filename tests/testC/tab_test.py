import unittest
from pages.modelportfolio.modelportfolio_page import ModelPortfolio
from utils.teststatus import TestStatus
import pytest

@pytest.mark.usefixtures("oneTimesetUp", "setUp")
class TabTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimesetUp):
        self.mp = ModelPortfolio(self.driver)
        self.ts = TestStatus(self.driver)
    '''
    Test C
    1. Navigate to https://sfo-demo.herokuapp.com/model-portfolio
    2. Check whether tabs with below texts are available (Where X, Y are are numbers)
        a. “X Portfolio recommendations based on your preferences”
        b. “Y other portfolio choices available”
    3. Resize browser window to 375 x 667
    4. Check whether tabs with below texts are available now (Where X, Y are are numbers)
        a. “Recommended (X)”
        b. “Others (Y)”
        c. Check X, Y are same as in step 2
    '''
    @pytest.mark.run(order=1)
    def test_tabTextValidation(self):
        result= self.mp.tabVerificaion(height=375, width= 667)
        self.ts.markfinal('test_rebalanceValidation',result, "test Re-balance Validation FAILED")