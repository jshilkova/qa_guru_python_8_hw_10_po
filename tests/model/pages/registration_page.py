from pathlib import Path

from selene import browser, have

import tests


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def select_gender(self, value):
        browser.all('[name="gender"]').element_by(have.value(value)).element('..').click()
        return self

    def fill_mobile(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        (browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click())
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def select_hobbies(self, value):
        browser.all('label[for^="hobbies-checkbox"]').element_by(have.exact_text(value)).click()
        return self

    def upload_picture(self, value):
        (browser.element('#uploadPicture')
         .type(str(Path(tests.__file__).parent.joinpath(value).absolute())))
        return self

    def type_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value):
        browser.element('#state').click()
        browser.all('[id^="react-select-3-option"]').element_by(have.exact_text(value)).click()
        return self

    def select_city(self, value):
        browser.element('#city').click()
        browser.all('[id^="react-select-4-option"]').element_by(have.exact_text(value)).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_registered_user(self, full_name, email, gender, mobile, birthday, subjects, hobbies, picture,
                                    address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile,
                birthday,
                subjects,
                hobbies,
                picture,
                address,
                state_and_city
            ))


