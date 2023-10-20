from tests.model.pages.registration_page import RegistrationPage


def test_complete_form():
    registration_page = RegistrationPage()
    registration_page.open()

    (registration_page
     .fill_first_name('Iuliia')
     .fill_last_name('Shilkova')
     .fill_email('yulia.shilkova@gmail.com')
     .select_gender('Female')
     .fill_mobile('1234567890')
     .fill_date_of_birth('1988', 'July', '30')
     .fill_subjects('Arts')
     .select_hobbies('Sports')
     .upload_picture('images/a_nice_cat_image.jpeg')
     .type_current_address('My current address')
     .select_state('Haryana')
     .select_city('Panipat')
     .submit())

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
