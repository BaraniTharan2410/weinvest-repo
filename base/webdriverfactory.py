from selenium import webdriver
"""
create a webdriver instance and return web driver based on the browser config
##Note##
Executable path for the webdriver should pointed to the environment variables in your system default
 """
class WebDriverFactory():
    def __init__(self, browser):
        self.browser= browser
    def getDriverInstance(self):
        baseurl = "https://sfo-demo.herokuapp.com/model-portfolio"
        if self.browser == "chrome":
            chrome_opt = webdriver.ChromeOptions(executable_path="./drivers/chromedriver.exe")
            chrome_opt.add_argument("--disable-gpu")
            driver = webdriver.Chrome(options= chrome_opt)
            # set maximum size based on system resolution usage
            driver.set_window_size(1366,768)
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
        elif self.browser == "ie":
            driver = webdriver.Ie(executable_path="./drivers/IEDriverServer.exe")
        #maximize window
        driver.maximize_window()
        driver.implicitly_wait(8)
        # navigate browser window to the mentioned base url
        driver.get(baseurl)
        return driver