import os
from datetime import datetime
from pathlib import Path

from selene import browser, have, be, command

import tests


def test_complete_form():
    browser.open('/automation-practice-form')
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#firstName').should(be.blank).type('Iuliia')
    browser.element('#lastName').should(be.blank).type('Shilkova')
    browser.element('#userEmail').should(be.blank).type('yulia.shilkova@gmail.com')

    browser.all('[name="gender"]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('July')
    browser.element('.react-datepicker__year-select').type('1988')
    (browser.element(f'.react-datepicker__day--0{30}:not(.react-datepicker__day--outside-month)').click())

    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.all('label[for^="hobbies-checkbox"]').element_by(have.exact_text('Sports')).click()
    (browser.element('#uploadPicture')
     .type(str(Path(tests.__file__).parent.joinpath('images/a_nice_cat_image.jpeg').absolute())))

    browser.element('#currentAddress').type('My current address')

    browser.element('#state').click()
    browser.all('[id^="react-select-3-option"]').element_by(have.exact_text("Haryana")).click()
    browser.element('#city').click()
    browser.all('[id^="react-select-4-option"]').element_by(have.exact_text("Panipat")).click()
    browser.element('#submit').click()

    browser.element('.modal-title').should(have.exact_text("Thanks for submitting the form"))
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Iuliia Shilkova',
            'yulia.shilkova@gmail.com',
            'Female',
            '1234567890',
            '30 July,1988',
            'Arts',
            'Sports',
            'a_nice_cat_image.jpeg',
            'My current address',
            'Haryana Panipat'
        ))
