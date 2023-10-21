from demoqa_tests.application import app
from demoqa_tests.data.users import SimpleUser


def test_simple_registration_form():
    app.open()
    app.landing_page.clickGroupCard('Elements')
    app.left_panel.open_simple_registration_page('Elements', 'Text Box')

    julia = SimpleUser(
        'Iuliia Shilkova',
        'yulia.shilkova@gmail.com',
        'My current address',
        'My permanent address'
    )

    app.simple_registration.register(julia)

    app.simple_registration.should_have_registered(julia)
