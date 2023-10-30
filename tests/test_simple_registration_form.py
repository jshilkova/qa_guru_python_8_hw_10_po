import allure

from demoqa_tests.application import app
from demoqa_tests.data.users import SimpleUser


@allure.feature("Registration")
@allure.story("Simple registration form")
@allure.title("Test simple registration form")
def test_simple_registration_form():
    julia = SimpleUser(
        'Iuliia Shilkova',
        'yulia.shilkova@gmail.com',
        'My current address',
        'My permanent address'
    )

    with allure.step("Open simple form"):
        app.open()
        app.landing_page.clickGroupCard('Elements')
        app.left_panel.open_simple_registration_page('Elements', 'Text Box')

    with allure.step("Register a user"):
        app.simple_registration.register(julia)

    with allure.step("Check registered user"):
        app.simple_registration.should_have_registered(julia)
