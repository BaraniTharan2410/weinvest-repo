import unittest
from pages.exploreportfolio.explore_portfolio import ExplorePortfolio
from utils.teststatus import TestStatus
import pytest

@pytest.mark.usefixtures("oneTimesetUp", "setUp")
class RebalanceTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimesetUp):
        self.ep = ExplorePortfolio(self.driver)
        self.ts = TestStatus(self.driver)
    '''
    Test A
    1. Navigate to https://sfo-demo.herokuapp.com/model-portfolio
    2. Select “All Weather Strategy” by clicking on “Explore Investment Ideas”
    3. In next screen click on button “Customize Portfolio” to make changes to portfolio
    4. Click on “Customize” button to enable edit controls
    5. Change slider of “ SPDR S&P 500 ETF TRUST SPY US EQUITY ” to 50%
    6. Click on “Rebalance” button
    7. Click on “Invest” button
    8. On next page” verify that “SPDR…” under “What your portfolio contain ?” to be 50%
    '''
    @pytest.mark.run(order=1)
    def test_rebalanceValidation(self):
        result= self.ep.checkPercenatgeAllocatedAfterCustomizeInvest()
        self.ts.markfinal('test_rebalanceValidation',result, "test Re-balance Validation FAILED")