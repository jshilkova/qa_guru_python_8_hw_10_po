from datetime import date

from demoqa_tests.application import app
from demoqa_tests.data.users import User, Hobby


def test_complete_form():
    app.registration_page.open()

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

    app.registration_page.register(julia)

    app.registration_page.should_have_registered(julia)