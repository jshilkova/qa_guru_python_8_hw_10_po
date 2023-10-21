from selene import browser, have


class LandingPage:
    def clickGroupCard(self, group):
        browser.element('.category-cards').all('.card').element_by(have.exact_text(group)).click()