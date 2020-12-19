import pytest
from base.webdriverfactory import WebDriverFactory

@pytest.fixture()
def setUp():
    # setup
    print("I am in setup will execute once before all the method")
    yield
    # tear down
    print("I am in setup will execute once after all the method")

@pytest.fixture(scope= "class")
def oneTimesetUp(request, browser):
    print("Running Onetime Setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    # close the browser
    driver.quit()
    print("Running tear down")

def pytest_addoption(parser):
    # Pass the value to commmand line arguments
    parser.addoption("--browser")
    parser.addoption("--os",help="type of os")

@pytest.fixture(scope= "session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope= "session")
def os(request):
    return request.config.getoption("--os")


