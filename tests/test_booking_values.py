from pages.homePage import HomePage
from tests.baseTest import BaseTest


class TestBookingValues(BaseTest):

    def test_neg_adults(self):
        page = HomePage(self.driver)
        page.neg_travellers()

    def test_100_adults(self):
        page = HomePage(self.driver)
        page.lot_travellers()

    def test_12_kids(self):
        page = HomePage(self.driver)
        page.lot_kids()

    def test_neg_kids(self):
        page = HomePage(self.driver)
        page.neg_kids()

    def test_10_rooms(self):
        page = HomePage(self.driver)
        page.lot_rooms()

    def test_under1_room(self):
        page = HomePage(self.driver)
        page.neg_rooms()