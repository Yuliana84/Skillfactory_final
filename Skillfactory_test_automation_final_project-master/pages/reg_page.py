from .base_page import BasePage
from .locators import BaseLocators, RegPageLocators, EmailConfirmPageLocators, UserAgreementPageLocators


class RegPage(BasePage):
    # RT013 метод проверки расположения полей ввода, кнопки "Зарегистрироваться", ссылки на пользовательское соглашение
    def location_of_input_fields_and_buttons_and_links(self):
        assert self.is_element_present(RegPageLocators.REG_FIRST_NAME_INPUT_PAGE_RIGHT), "element not found"
        assert self.is_element_present(RegPageLocators.REG_REGISTER_BUTTON_PAGE_RIGHT), "element not found"
        assert self.is_element_present(RegPageLocators.REG_USER_AGREEMENT_LINK_PAGE_RIGHT), "element not found"

    # RT014 метод проверки валидации текстового поля (ввод валидных данных)
    def text_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_not_element_present(RegPageLocators.REG_ERROR_FIRST_NAME_INPUT), "element found"


    # RT015 метод проверки ссылки в футере на страницу с пользовательским соглашением
    def link_fut_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(RegPageLocators.REG_PRIVACY_POLICY_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # RT016 метод проверки валидации текстового поля (ввод невалидных данных)
    def text_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_FIRST_NAME_INPUT), "element not found"

