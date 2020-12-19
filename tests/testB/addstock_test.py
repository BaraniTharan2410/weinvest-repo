import unittest
from pages.weatherportfolio.weather_portfolio import WeatherPortfolio
from utils.teststatus import TestStatus
import pytest

@pytest.mark.usefixtures("oneTimesetUp", "setUp")
class AddStockTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimesetUp):
        self.wp = WeatherPortfolio(self.driver)
        self.ts = TestStatus(self.driver)
    """
    Test B
    1. Navigate to https://sfo-demo.herokuapp.com/model-portfolio
    2. Select “All Weather Strategy” by clicking on “Explore Investment Ideas”
    3. In next screen click on button “Customize Portfolio” to make changes to portfolio
    4. Click on “Customize” button to enable edit controls
    5. Click on “Customise” button and ensure the text change to “Reset”
    6. Click on “+Add Stock”
    7. Click “Add Stock” in “BT Group plc” row.
    8. Click on “Done”
    9. Check whether “BT Group plc” is added to the portfolio
    """
    @pytest.mark.run(order=1)
    def test_addStockValidation(self):
        result= self.wp.addStockAndValidateInPortfolio()
        self.ts.markfinal('test_addStockValidation',result, "test add stock Validation FAILED")