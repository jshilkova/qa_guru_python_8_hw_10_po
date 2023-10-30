from datetime import date

import allure

from demoqa_tests.application import app
from demoqa_tests.data.users import User, Hobby


@allure.feature("Registration")
@allure.story("Complete registration form")
@allure.title("Test extended registration form")
def test_complete_form():
    julia = User(
        'Iuliia',
        'Shilkova',
        'yulia.shilkova@gmail.com',
        'Female',
        '1234567890',
        date(1988, 7, 30),
        ['Arts'],
        [Hobby.sports.value],
        'a_nice_cat_image.jpeg',
        'My current address',
        'Haryana',
        'Panipat'
    )

    with allure.step("Open registration form"):
        app.complete_registration.open()

    with allure.step("Register the user"):
        app.complete_registration.register(julia)

    with allure.step("Check registered user"):
        app.complete_registration.should_have_registered(julia)
