import time


from pages.basePage import BasePage
from pages.resultPage import ResultPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)



    def hotel_search(self,city,day,age,country):
        self.click("hotel_XPATH")
        self.click("city_field_XPATH")
        self.send_keys("city_input_XPATH", city)
        self.waiting_visible("city_option_XPATH", city)
        self.click("city_option_XPATH")
        self.click("check_in_date_XPATH")
        for i in self.elems("check_in_calendar_XPATH"):
            if i.text==day:
                self.click(i)
        self.click("co_date_XPATH")
        self.click("travellers_XPATH")
        self.click("rooms_add_btn_XPATH")
        self.click("adults_add_btn_XPATH")
        self.click("child_add_btn_XPATH")
        self.waiting("child_age_dropd_XPATH")
        self.dropdown("child_age_dropd_XPATH",age)
        self.dropdown("nationality_dropd_XPATH", country)
        self.click("search_btn_XPATH")

        return ResultPage(self.driver)


    def neg_travellers(self):
        self.click("travellers_XPATH")
        self.waiting("adults_minus_btn_XPATH")
        a=time.time()
        while time.time()<a+10:
            self.click("adults_minus_btn_XPATH")
        assert int(self.attributes("adult_value_XPATH","value"))>-1

    def lot_travellers(self):
        self.click("travellers_XPATH")
        self.waiting("adults_add_btn_XPATH")
        a = time.time()
        while time.time() < a + 10:
            self.click("adults_add_btn_XPATH")
        assert int(self.attributes("adult_value_XPATH", "value")) < 100

    def lot_kids(self):
        self.click("travellers_XPATH")
        self.waiting("child_add_btn_XPATH")
        a = time.time()
        while time.time() < a + 10:
            self.click("child_add_btn_XPATH")
        assert int(self.attributes("child_value_XPATH", "value")) == 12

    def neg_kids(self):
        self.click("travellers_XPATH")
        self.waiting("child_minus_btn_XPATH")
        a=time.time()
        while time.time()<a+10:
            self.click("child_minus_btn_XPATH")
        assert int(self.attributes("child_value_XPATH","value"))>-1

    def lot_rooms(self):
        self.click("travellers_XPATH")
        self.waiting("rooms_add_btn_XPATH")
        a = time.time()
        while time.time() < a + 10:
            self.click("rooms_add_btn_XPATH")
        assert int(self.attributes("room_value_XPATH", "value")) < 100

    def neg_rooms(self):
        self.click("travellers_XPATH")
        self.waiting("room_minus_btn_XPATH")
        a=time.time()
        while time.time()<a+10:
            self.click("room_minus_btn_XPATH")
        assert int(self.attributes("room_value_XPATH","value"))>0