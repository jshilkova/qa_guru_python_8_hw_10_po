import os
from datetime import datetime

from selene import browser, have, be


def test_complete_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Iuliia')
    browser.element('#lastName').should(be.blank).type('Shilkova')
    browser.element('#userEmail').should(be.blank).type('yulia.shilkova@gmail.com')

    browser.all('label[for^="gender-radio"]').element_by(have.exact_text('Female')).click()
    browser.element('#userNumber').should(be.blank).type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker').should(be.visible)
    browser.element('.react-datepicker__month-select').click().all('option').element_by(have.exact_text('July')).click()
    browser.element('.react-datepicker__year-select').click().all('option').element_by(have.exact_text('1988')).click()
    browser.element('[aria-label="Choose Saturday, July 30th, 1988"]').click()
    browser.element('#dateOfBirthInput').should(have.value('30 Jul 1988'))

    browser.element('#subjectsInput').type('a')
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text('Arts')).click()
    browser.element('#subjectsInput').type('b')
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text('Biology')).click()
    browser.all('.subjects-auto-complete__multi-value__label').should(have.exact_texts('Arts', 'Biology'))

    browser.all('label[for^="hobbies-checkbox"]').element_by(have.exact_text('Sports')).click()
    browser.all('label[for^="hobbies-checkbox"]').element_by(have.exact_text('Reading')).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('.pytest_cache/images/a_nice_cat_image.jpeg'))

    browser.element('#currentAddress').type('My current address is very long\n'
                                            'and should be written in several lines\n'
                                            'to test the form')

    browser.element('#state').click().all('[id^="react-select-3-option"]') \
        .element_by(have.exact_text("Haryana")).click()
    browser.element('#city').click().all('[id^="react-select-4-option"]').element_by(have.exact_text("Panipat")).click()
    browser.element('#submit').click()

    browser.element('.modal-title').should(have.exact_text("Thanks for submitting the form"))
    browser.element('//div[@class="modal-body"]//td[text()="Student Name"]/following-sibling::td') \
        .should(have.text("Iuliia Shilkova"))
    browser.element('//div[@class="modal-body"]//td[text()="Student Email"]/following-sibling::td') \
        .should(have.text("yulia.shilkova@gmail.com"))
    browser.element('//div[@class="modal-body"]//td[text()="Gender"]/following-sibling::td') \
        .should(have.text("Female"))
    browser.element('//div[@class="modal-body"]//td[text()="Mobile"]/following-sibling::td') \
        .should(have.text("1234567890"))
    browser.element('//div[@class="modal-body"]//td[text()="Date of Birth"]/following-sibling::td') \
        .should(have.text("30 July,1988"))
    browser.element('//div[@class="modal-body"]//td[text()="Subjects"]/following-sibling::td') \
        .should(have.text("Arts, Biology"))
    browser.element('//div[@class="modal-body"]//td[text()="Hobbies"]/following-sibling::td') \
        .should(have.text("Sports, Reading"))
    browser.element('//div[@class="modal-body"]//td[text()="Picture"]/following-sibling::td') \
        .should(have.text("a_nice_cat_image.jpeg"))
    browser.element('//div[@class="modal-body"]//td[text()="Address"]/following-sibling::td') \
        .should(have.text("My current address is very long and should be written in several lines to test the form"))
    browser.element('//div[@class="modal-body"]//td[text()="State and City"]/following-sibling::td') \
        .should(have.text("Haryana Panipat"))

    browser.element("#closeLargeModal").click()

    browser.element('.modal-dialog').should(be.not_.existing)
    browser.element('#firstName').should(be.blank)
    browser.element('#lastName').should(be.blank)
    browser.element('#userEmail').should(be.blank)
    browser.element('#userNumber').should(be.blank)
    browser.element('#dateOfBirthInput').should(have.value(datetime.today().strftime('%d %b %Y')))
    browser.element('.subjects-auto-complete__multi-value').should(be.not_.present)
    browser.element('#uploadPicture').should(be.blank)
    browser.element('#currentAddress').should(be.blank)
