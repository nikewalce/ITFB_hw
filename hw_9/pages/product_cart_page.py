from pages.base_page import BasePage
from pages.locators.product_cart_page_locators import CartProductLocators as Locator
import allure
from pathlib import Path

class ProductCartPage(BasePage):
    def click_select_available_options_dropdown_button(self):
        self.get_element(Locator.SELECT_AVAILABLE_OPTIONS_DROPDOWN_LIST, timeout=1).click()
        self.get_element(Locator.OPTION_RED, timeout=1).click()

    def qty_entry(self):
        qty = 2
        element = self.get_element(Locator.INPUT_QTY, timeout=1)
        element.clear()
        element.send_keys(qty)

    def click_add_to_cart_button(self):
        self.get_element(Locator.ADD_TO_CART_BUTTON, timeout=1).click()

    def click_shopping_cart(self):
        self.get_element(Locator.SHOPPING_CART_BUTTON, timeout=3).click()

    def click_radio_medium_checkbox(self):
        self.get_element(Locator.RADIO_MEDIUM_CHECKBOX, timeout=1).click()

    def click_checkbox3(self):
        self.click_with_scroll(Locator.CHECKBOX3, timeout=3)
        self.scroll_to_end(1)

    def click_checkbox4(self):
        self.get_element(Locator.CHECKBOX4, timeout=1).click()

    def enter_text_text(self):
        text = 'Текст'
        element = self.get_element(Locator.TEXT_INPUT, timeout=1)
        element.clear()
        element.send_keys(text)

    def click_select_available_options_dropdown(self):
        self.get_element(Locator.SELECT_AVAILABLE_OPTIONS_DROPDOWN, timeout=1).click()

    def click_yellow_available_options(self):
        self.get_element(Locator.YELLOW_AVAILABLE_OPTIONS, timeout=1).click()

    def enter_textarea_available_options(self):
        text = 'Текст'
        element = self.get_element(Locator.TEXTAREA_AVAILABLE_OPTIONS, timeout=1)
        element.clear()
        element.send_keys(text)

    def upload_file(self):
        self.get_element(Locator.BUTTON_UPLOAD_FILE, timeout=1).click()
        file_input = self.presence_of_element_located(Locator.INPUT_TYPE_FILE,timeout=5)
        # 3. Делаем input видимым через JS
        self.driver.execute_script("""
                arguments[0].style.display = 'block';
                arguments[0].style.visibility = 'visible';
                arguments[0].style.opacity = 1;
            """, file_input)
        file_input.send_keys('C:/Work/workPython/ITFB/ITFB_hw/hw_9/requirements.txt')
        self.allert()


    def enter_date_time(self):
        date_text = '2025-05-11'
        time_text = '14:25'
        date = self.get_element(Locator.DATE_INPUT, timeout=1)
        date.clear()
        date.send_keys(date_text)
        time = self.get_element(Locator.TIME_INPUT, timeout=1)
        time.clear()
        time.send_keys(time_text)
        dateandtime = self.get_element(Locator.DATEANDTIME_INPUT, timeout=1)
        dateandtime.clear()
        dateandtime.send_keys(f"{date_text} {time_text}")

    def click_cart_div(self):
        self.get_element(Locator.CART_DIV, timeout=3).click()

    def click_cart_checkout(self):
        self.get_element(Locator.CART_CHECKOUT, timeout=3).click()