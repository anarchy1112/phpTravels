import time

from pages.basePage import BasePage


class HotelPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def book_room(self):
        time.sleep(2)
        self.click("notif_XPATH")
        time.sleep(1)
        self.scrolldown(500)
        self.waiting("book_room1_XPATH")
        time.sleep(1)
        self.click("book_room1_XPATH")