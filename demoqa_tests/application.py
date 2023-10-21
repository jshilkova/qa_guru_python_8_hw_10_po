from selene import browser

from demoqa_tests.components.left_panel import LeftPanel
from demoqa_tests.model.pages.landing_page import LandingPage
from demoqa_tests.model.pages.simple_registration_page import SimpleRegistrationPage


class Application:
    def __init__(self):
        self.simple_registration = SimpleRegistrationPage()
        self.left_panel = LeftPanel()
        self.landing_page = LandingPage()

    def open(self):
        browser.open('/')
        return self


app = Application()