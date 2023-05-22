from settings import valid_phone, valid_email, sql_injection
from .base_page import BasePage
from .locators import AuthPageLocators, ChangePassPageLocators, UserAgreementPageLocators, \
    RejectedRequestPageLocators, BaseLocators


class ChangePassPage(BasePage):
    # RT009 метод проверки типа восстановления пароля по умолчанию
    def default_password_recovery_type(self):
        assert self.is_element_present(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT_PLACEHOLDER_TELEPHONE), \
            "element not found"

    # RT010 метод проверки на валидацию поля ввода номера телефона /почты /логина /лицевого счета (ввод валидного номера)
    def phone_field_validation_valid_data(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_PHONE).click()
        phone = valid_phone()
        self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT).send_keys(phone)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT_VALUE)
        value = element.get_attribute("value")
        assert ("7"+str(phone)) == value, "phone do not match"

    # RT011 метод проверки на валидацию поля ввода номера телефона /почты /логина /лицевого счета (ввод валидного email)
    def email_field_validation_valid_data(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_MAIL).click()
        username_input = self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT)
        email = valid_email()
        username_input.send_keys(email)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT_VALUE)
        value = element.get_attribute("value")
        assert email == value, "email do not match"

    # RT012 метод проверки восстановления пароля с незаполненными полями
    def password_recovery_with_blank_fields(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_PHONE).click()
        self.find_element(ChangePassPageLocators.CHANGE_PASS_CONTINUE_BUTTON).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassPageLocators.CHANGE_PASS_ERROR_ENTER_PHONE_NUMBER), \
            "element not found"

