import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.configReader import readConfig

@pytest.fixture(scope='function')
def setUp(request):
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver = driver
    driver.get(readConfig("basic_info", "starting_URL"))
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()