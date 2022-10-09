from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from utilities.configReader import readConfig


class BasePage:

    def __init__(self, driver):
        self.driver=driver

    def click(self, locator):
        self.driver.find_element(By.XPATH,readConfig('locators', locator)).click()

    def send_keys(self, locator, value):
        self.driver.find_element(By.XPATH,readConfig('locators', locator)).send_keys(value)

    def clear(self, locator):
        self.driver.find_element(By.XPATH,readConfig('locators', locator)).clear()

    def mouseover(self,locator):
        elem=self.driver.find_element(By.XPATH,readConfig('locators', locator))
        action=ActionChains(self.driver)
        action.move_to_element(elem).perform()

    def rightClick(self,locator):
        elem = self.driver.find_element(By.XPATH, readConfig('locators', locator))
        action = ActionChains(self.driver)
        action.context_click(elem).perform()

    def dropdown(self, locator,value):
        elem = self.driver.find_element(By.XPATH, readConfig('locators', locator))
        select=Select(elem)
        select.select_by_value(value)

    def waiting(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, readConfig('locators', locator))))

    def waiting_visible(self, locator,text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, readConfig('locators', locator)),text))

    def text_extraction(self, locator):
        return self.driver.find_element(By.XPATH, readConfig('locators', locator)).text

    def drag(self, locSlider,locSlideLine, percX, percY):
        mainSlider=self.driver.find_element(By.XPATH, readConfig('locators', locSlideLine))
        size=mainSlider.size
        w,h=size['width'], size['height']
        elem = self.driver.find_element(By.XPATH, readConfig('locators', locSlider))
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(elem, w*percX, h*percY).perform()

    def elems(self,locator):
        return self.driver.find_elements(By.XPATH, readConfig('locators', locator))

    def scrolldown(self,yaxis):
        self.driver.execute_script(f"window.scrollTo(0, {yaxis})")

    def attributes(self,locator,attribute):
        return self.driver.find_element(By.XPATH, readConfig('locators', locator)).get_attribute(attribute)

    def key_ent(self):
        self.driver.send_keys(Keys.ENTER)

    def click2(self,locator):
        self.driver.execute_script("arguments[0].click();", readConfig('locators',locator))



