from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    comfort_button = (By.XPATH, '//div[@class="tcard"]//div[contains(text(), "Comfort")]')
    taxi_button = (By.XPATH, '//button[contains(text(), "Pedir taxi")]')
    phone_number_field = (By.ID, 'phone_number')
    next_button = (By.XPATH, '//button[text()="Siguiente"]')
    phone_code_field = (By.ID, 'code')
    confirm_button = (By.XPATH, '//button[text()="Confirmar"]')
    payment_method_button = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card_button = (By.CSS_SELECTOR, '.pp-button .pp-text')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.CSS_SELECTOR, '#code')
    link_button = (By.CSS_SELECTOR, '.pp-buttons button:last-child')
    message_for_driver_field = (By.ID, 'comment')
    blanket_and_tissues_toggle = (By.CSS_SELECTOR, '.toggle.round')
    ice_cream_toggle = (By.CSS_SELECTOR,
                        '#requirements > div > div.tcard-body.card-body > div:nth-child(2) > div.slider.round')
    ice_cream_plus_button = (By.CSS_SELECTOR,
                             'div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button')
    order_button = (By.CSS_SELECTOR, '.order-button')
    search_for_driver_modal = (By.CSS_SELECTOR, '.order-body')
    driver_info_modal = (By.CSS_SELECTOR, '.order-finished')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field)).send_keys(from_address)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value(self.from_field, from_address))

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.to_field)).send_keys(to_address)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value(self.to_field, to_address))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.comfort_button))

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_attribute('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_attribute('value')

    def click_taxi_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.taxi_button))
        self.driver.find_element(*self.taxi_button).click()

    def click_comfort_button(self):
        card = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.comfort_button))
        self.driver.execute_script("arguments[0].scrollIntoView();", card)
        card.click()

    def get_comfort_tariff(self):
        return self.driver.find_element(*self.comfort_button).text

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_phone_code(self, phone_code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*self.phone_code_field))
        self.driver.find_element(*self.phone_code_field).send_keys(phone_code)

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    def add_credit_card(self, card_number, card_code):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.payment_method_button)).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_card_button)).click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.card_number_field)).send_keys(card_number)

        self.driver.find_element(*self.card_code_field).send_keys(card_code)
        self.driver.find_elemetn(*self.card_code_field).send_keys(Keys.TAB)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.link_button))
        self.driver.find_element(*self.link_button).click()

    def set_message_for_driver(self, message):
        self.driver.find_element(*self.message_for_driver_field).send_keys(message)

    def click_blanket_and_tissues_toggle(self):
        self.driver.find_element(*self.blanket_and_tissues_toggle).click()

    def add_two_ice_cream(self):
        self.driver.find_element(*self.ice_cream_toggle).click()
        self.driver.find_element(*self.ice_cream_plus_button).click()
        self.driver.find_element(*self.ice_cream_plus_button).click()

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def wait_for_search_for_driver_modal(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(*self.search_for_driver_modal))

    def wait_for_driver_info_modal(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(*self.driver_info_modal))
        return self.driver.find_element(*self.driver_info_modal)
