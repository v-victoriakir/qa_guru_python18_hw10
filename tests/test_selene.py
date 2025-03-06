from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com/')
    browser.driver.fullscreen_window()
    s('.search-input').click()
    s('#query-builder-test').send_keys('okken/pytest-check').press_enter()
    s(by.link_text("okken/pytest-check")).click()
    s("#issues-tab").click()
    s(by.link_text('raises match argument')).should(be.visible)
