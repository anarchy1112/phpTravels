
import pytest

from pages.formPage import FormPage
from  utilities.get_data import data_getter
from pages.homePage import HomePage
from tests.baseTest import BaseTest

#kosristio function chaining, ako ne ide obrisato fill_form metodu i pozvati objekat form pagea
#is_displayed napravi metod u base pageui funkcijukoja bi radila iteraciju

class TestHotelBooking(BaseTest):

    @pytest.mark.parametrize("city, day, age, country,firstname,lastname,Email,Phone,Address,countr,nationality,trav1title,trav1firstname,trav1lastname,trav2title,trav2firstname,trav2lastname,trav3title,trav3firstname,trav3lastname,childfname,childlname", data_getter('Sheet1'))
    def test_hotel_book(self,city,day,age,country,firstname,lastname,Email,Phone,Address,countr,nationality,trav1title,trav1firstname,trav1lastname,trav2title,trav2firstname,trav2lastname,trav3title,trav3firstname,trav3lastname,childfname,childlname):
        page=HomePage(self.driver)
        page.hotel_search(city,day,age,country).filter_and_choose().book_room()
        page2=FormPage(self.driver)
        page2.fill_form(firstname,lastname,Email,Phone,Address,countr,nationality,trav1title,trav1firstname,trav1lastname,trav2title,trav2firstname,trav2lastname,trav3title,trav3firstname,trav3lastname,childfname,childlname)

