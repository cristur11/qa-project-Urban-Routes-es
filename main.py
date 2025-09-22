import data
from selenium import webdriver
from helpers import retrieve_phone_code
from pages import UrbanRoutesPage
from selenium.webdriver.chrome.options import Options



class TestUrbanRoutes:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        # Se pasa el objeto `options` al constructor de Chrome
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.urban_routes_url)
        cls.page = UrbanRoutesPage(cls.driver)

    def setup_method(self):
        self.driver.get(data.urban_routes_url)

    def test_1_set_address(self):
        self.page.set_from(data.address_from)
        self.page.set_to(data.address_to)
        assert self.page.get_from() == data.address_from
        assert self.page.get_to() == data.address_to

    def test_2_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_comfort_button()
        assert 'Comfort' == routes_page.get_comfort_tariff()

    def test_3_phone_number(self):
        self.page.set_from(data.address_from)
        self.page.set_to(data.address_to)
        self.page.click_comfort_button()
        self.page.set_phone_number(data.phone_number)
        self.page.click_next_button()
        phone_code = retrieve_phone_code(self.driver)
        self.page.set_phone_code(phone_code)
        self.page.click_confirm_button()
        assert not self.page.driver.find_elements(*self.page.phone_code_field)

    def test_4_card_number(self):
        self.page.set_from(data.address_from)
        self.page.set_to(data.address_to)
        self.page.click_comfort_button()
        self.page.set_phone_number(data.phone_number)
        self.page.click_next_button()
        phone_code = retrieve_phone_code(self.driver)
        self.page.set_phone_code(phone_code)
        self.page.click_confirm_button()
        self.page.add_credit_card(data.card_number, data.card_code)
        assert not self.page.driver.find_elements(*self.page.add_card_button)

    def test_5_message_for_driver(self):
        self.page.set_from(data.address_from)
        self.page.set_to(data.address_to)
        self.page.click_comfort_button()
        self.page.set_message_for_driver(data.message_for_driver)
        assert self.page.driver.find_element(*self.page.message_for_driver_field).get_attribute(
            'value') == data.message_for_driver

    def test_6_blanket_and_tissues_option(self):
        self.page.set_from(data.address_from)
        self.page.set_to(data.address_to)
        self.page.click_comfort_button()
        self.page.click_blanket_and_tissues_toggle()
        assert "checked" in self.page.driver.find_element(*self.page.blanket_and_tissues_toggle).get_attribute("class")

    def test_7_add_two_ice_cream(self):
        self.page.set_from(data.address_from)
        self.page.set_to(data.address_to)
        self.page.click_comfort_button()
        self.page.add_two_ice_cream()
        assert self.page.driver.find_element(*self.page.ice_cream_plus_button).is_displayed()

    def test_8_complete_taxi_order_process(self):
        self.page.set_from(data.address_from)
        self.page.set_to(data.address_to)
        self.page.click_comfort_button()
        self.page.set_phone_number(data.phone_number)
        self.page.click_next_button()
        phone_code = retrieve_phone_code(self.driver)
        self.page.set_phone_code(phone_code)
        self.page.click_confirm_button()
        self.page.add_credit_card(data.card_number, data.card_code)
        self.page.click_order_button()
        self.page.wait_for_search_for_driver_modal()
        assert self.page.driver.find_element(*self.page.search_for_driver_modal).is_displayed()

    def test_9_driver_info_modal(self):
        self.page.set_from(data.address_from)
        self.page.set_to(data.address_to)
        self.page.click_comfort_button()
        self.page.set_phone_number(data.phone_number)
        self.page.click_next_button()
        phone_code = retrieve_phone_code(self.driver)
        self.page.set_phone_code(phone_code)
        self.page.click_confirm_button()
        self.page.add_credit_card(data.card_number, data.card_code)
        self.page.click_order_button()
        driver_modal_element = self.page.wait_for_driver_info_modal()
        assert driver_modal_element.is_displayed()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
