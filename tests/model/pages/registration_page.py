from pathlib import Path

from selene import browser, have

import tests
from tests.data.users import User


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def register(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('[name="gender"]').element_by(have.value(user.gender)).element('..').click()
        browser.element('#userNumber').type(user.mobile)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.date_of_birth.month)
        browser.element('.react-datepicker__year-select').type(user.date_of_birth.year)
        (browser
         .element(f'.react-datepicker__day--0{user.date_of_birth.day}:not(.react-datepicker__day--outside-month)')
         .click())
        for subject in user.subjects:
            browser.element('#subjectsInput').type(subject).press_enter()
        for hobby in user.hobbies:
            browser.all('label[for^="hobbies-checkbox"]').element_by(have.exact_text(hobby)).click()
        (browser.element('#uploadPicture')
         .type(str(Path(tests.__file__).parent.joinpath('resources').joinpath(user.picture).absolute())))
        browser.element('#currentAddress').type(user.address)
        browser.element('#state').click()
        browser.all('[id^="react-select-3-option"]').element_by(have.exact_text(user.state)).click()
        browser.element('#city').click()
        browser.all('[id^="react-select-4-option"]').element_by(have.exact_text(user.city)).click()
        browser.element('#submit').click()

    def should_have_registered(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.mobile,
                f'{user.date_of_birth.day} {user.date_of_birth.month},{user.date_of_birth.year}',
                ', '.join(user.subjects),
                ', '.join(user.hobbies),
                user.picture,
                user.address,
                f'{user.state} {user.city}'
            ))

