import time

from pages.basePage import BasePage


class FormPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def fill_form(self,firstname,lastname,Email,Phone,Address,countr,nationality,trav1title,trav1firstname,trav1lastname,trav2title,trav2firstname,trav2lastname,trav3title,trav3firstname,trav3lastname,childfname,childlname):
        self.send_keys('persinfo_firstname_XPATH', firstname)
        self.send_keys('persinfo_lastname_XPATH',lastname)
        self.send_keys('persinfo_Email_XPATH',Email )
        self.send_keys('persinfo_Phone_XPATH',Phone )
        self.send_keys('persinfo_Address_XPATH', Address)
        self.click('persinfo_country_XPATH')
        self.send_keys('country_text_XPATH', countr)
        self.key_ent()
        self.click('persinfo_nationality_XPATH')
        self.send_keys('nation_text_XPATH', nationality)
        self.key_ent()
        self.dropdown('traveler1_title_XPATH',trav1title)
        self.send_keys('traveler1_firstname_XPATH', trav1firstname)
        self.send_keys('traveler1_lastname_XPATH', trav1lastname)
        self.dropdown('traveler2_title_XPATH',trav2title)
        self.send_keys('traveler2_firstname_XPATH', trav2firstname)
        self.send_keys('traveler2_lastname_XPATH', trav2lastname)
        self.dropdown('traveler3_title_XPATH', trav3title)
        self.send_keys('traveler3_firstname_XPATH', trav3firstname)
        self.send_keys('traveler3_lastname_XPATH', trav3lastname)
        self.send_keys('child_firstname_XPATH', childfname)
        self.send_keys('child_lastname_XPATH', childlname)
        time.sleep(2)
        self.scrolldown(1500)
        self.click('pay_later_btn_XPATH')
        self.waiting('termsandcond_XPATH')
        self.click2('termsandcond_XPATH')
        #self.click('termsandcond_XPATH')
        self.click('confirm_booking_btn_XPATH')