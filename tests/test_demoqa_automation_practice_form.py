from datetime import date
from demoqa_tests.data.users import User, Hobby
from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_complete_form():
    registration_page = RegistrationPage()
    registration_page.open()

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

    registration_page.register(julia)

    registration_page.should_have_registered(julia)
