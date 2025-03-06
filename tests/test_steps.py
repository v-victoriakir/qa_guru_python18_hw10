import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 'v-victoriakir')
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Проверка наличия конкретного Issue")
    allure.dynamic.link('https://github.com/', 'Testing')
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')
        browser.driver.fullscreen_window()
    with allure.step('Ищем репозиторий'):
        s('.search-input').click()
        s('#query-builder-test').send_keys('okken/pytest-check').press_enter()
    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text("okken/pytest-check")).click()
    with allure.step('Открываем tab issues'):
        s("#issues-tab").click()
    with allure.step('Проверяем наличие issue с текстом raises match argument'):
        s(by.link_text('raises match argument')).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'v-victoriakir')
@allure.feature("Задачи в репозитории")
@allure.story("Проверка наличия Issue")
@allure.link('https://github.com/', 'Testing')
def test_decorator_labels():
    open_main_page()
    search_for_repository('okken/pytest-check')
    go_to_repository('okken/pytest-check')
    open_issues_tab()
    should_see_issue_with_text('raises match argument')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')
    browser.driver.fullscreen_window()


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.search-input').click()
    s('#query-builder-test').send_keys(repo).press_enter()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем tab issues')
def open_issues_tab():
    s("#issues-tab").click()


@allure.step('Проверяем наличие issue с текстом {value}')
def should_see_issue_with_text(value):
    s(by.link_text(value)).should(be.visible)
