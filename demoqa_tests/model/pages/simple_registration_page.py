from selene import browser, have
from demoqa_tests.data.users import SimpleUser


class SimpleRegistrationPage:
    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/text-box')

    def register(self, user: SimpleUser):
        self.full_name.type(user.full_name)
        self.email.type(user.email)
        self.current_address.type(user.current_address)
        self.permanent_address.type(user.permanent_address)
        self.submit_button.click()

    def should_have_registered(self, user: SimpleUser):
        browser.element('#output').element('#name').should(have.exact_text(f'Name:{user.full_name}'))
        browser.element('#output').element('#email').should(have.exact_text(f'Email:{user.email}'))
        browser.element('#output').element('#currentAddress').should(have.exact_text(f'Current Address :{user.current_address}'))
        browser.element('#output').element('#permanentAddress').should(have.exact_text(f'Permananet Address :{user.permanent_address}'))


