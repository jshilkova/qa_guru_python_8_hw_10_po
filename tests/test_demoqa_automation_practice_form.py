import os
from datetime import datetime
from pathlib import Path

from selene import browser, have, be, command

import tests
from tests.data.users import User, DateOfBirth
from tests.model.pages.registration_page import RegistrationPage


def test_complete_form():
    registration_page = RegistrationPage()
    registration_page.open()

    julia = User(
        'Iuliia',
        'Shilkova',
        'yulia.shilkova@gmail.com',
        'Female',
        '1234567890',
        DateOfBirth('30', 'July', '1988'),
        ['Arts'],
        ['Sports'],
        'a_nice_cat_image.jpeg',
        'My current address',
        'Haryana',
        'Panipat'
    )

    registration_page.register(julia)

    registration_page.should_have_registered(julia)
