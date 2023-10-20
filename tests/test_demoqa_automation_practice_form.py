from tests.model.pages.registration_page import RegistrationPage


def test_complete_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Iuliia')
    registration_page.fill_last_name('Shilkova')
    registration_page.fill_email('yulia.shilkova@gmail.com')
    registration_page.select_gender('Female')
    registration_page.fill_mobile('1234567890')
    registration_page.fill_date_of_birth('1988', 'July', '30')
    registration_page.fill_subjects('Arts')
    registration_page.select_hobbies('Sports')
    registration_page.upload_picture('images/a_nice_cat_image.jpeg')
    registration_page.type_current_address('My current address')
    registration_page.select_state('Haryana')
    registration_page.select_city('Panipat')
    registration_page.submit()
    registration_page.should_have_registered_user(
            'Iuliia Shilkova',
            'yulia.shilkova@gmail.com',
            'Female',
            '1234567890',
            '30 July,1988',
            'Arts',
            'Sports',
            'a_nice_cat_image.jpeg',
            'My current address',
            'Haryana Panipat')
