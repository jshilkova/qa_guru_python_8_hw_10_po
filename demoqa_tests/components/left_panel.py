from selene import browser, have, be


class LeftPanel:
    def open(self, group, item):
        menu_item = browser.element('.menu-list').all('[id^="item"]').element_by(have.exact_text(item))
        if not menu_item.matching(be.existing):
            browser.element('.left-pannel').all('.header-text').element_by(have.exact_text(group)).click()
        menu_item.click()

    def open_simple_registration_page(self, group, item):
        self.open(group, item)
