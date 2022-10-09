import time

from pages.basePage import BasePage

from pages.hotelPage import HotelPage


class ResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)



    def filter_and_choose(self):
        self.waiting("slide_to_XPATH")
        self.drag("slide_to_XPATH","slider_XPATH", -0.2,0)
        self.waiting("slide_from_XPATH")
        self.drag("slide_from_XPATH", "slider_XPATH", 0.3,0)
        time.sleep(3)
        self.click("hotel_detail_btn_XPATH")
        return HotelPage(self.driver)
