import os
import allure
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from armobile_web.models.pages.authorization_page import AuthorizationPage
from utils import attach

DEFAULT_BROWSER_VERSION = "128.0"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0'
    )
    parser.addoption(
        '--local',
        action='store_true',
        help='Run tests locally instead of Selenoid'
    )

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    is_local = request.config.getoption('--local')

    options = Options()

    if is_local:
        # Локальный запуск
        driver = webdriver.Chrome(options=options)
    else:
        # Запуск через Selenoid
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)
        login = os.getenv('LOGIN_SELENOID')
        password = os.getenv('PASSWORD_SELENOID')
        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            options=options
        )

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)

    if not is_local:
        attach.add_video(browser)  # Видео только для Selenoid

    browser.quit()

@pytest.fixture
@allure.step("Авторизуемся под владельцем перед тестом")
def authorization_admin(setup_browser):
    authorization_page = AuthorizationPage(browser)

    authorization_page.open_authorization_form(os.getenv("BASE_URL"))
    authorization_page.fill_login(os.getenv("EMAIL_ADMIN"))
    authorization_page.fill_password(os.getenv("PASSWORD_ADMIN"))
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()

@pytest.fixture
@allure.step("Авторизуемся под администратором перед тестом")
def authorization_expert(setup_browser):
    authorization_page = AuthorizationPage(browser)

    authorization_page.open_authorization_form(os.getenv("BASE_URL"))
    authorization_page.fill_login(os.getenv("EMAIL_EXPERT"))
    authorization_page.fill_password(os.getenv("PASSWORD_ADMIN"))
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()

@pytest.fixture
@allure.step("Авторизуемся под инспектором перед тестом")
def authorization_master(setup_browser):
    authorization_page = AuthorizationPage(browser)

    authorization_page.open_authorization_form(os.getenv("BASE_URL"))
    authorization_page.fill_login(os.getenv("EMAIL_MASTER"))
    authorization_page.fill_password(os.getenv("PASSWORD_ADMIN"))
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()

@pytest.fixture
@allure.step("Авторизуемся под подрядчиком перед тестом")
def authorization_subcontractor(setup_browser):
    authorization_page = AuthorizationPage(browser)

    authorization_page.open_authorization_form(os.getenv("BASE_URL"))
    authorization_page.fill_login(os.getenv("EMAIL_SUBCONTRACTOR"))
    authorization_page.fill_password(os.getenv("PASSWORD_ADMIN"))
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()

@pytest.fixture
@allure.step("Авторизуемся под наблюдателем перед тестом")
def authorization_observer(setup_browser):
    authorization_page = AuthorizationPage(browser)

    authorization_page.open_authorization_form(os.getenv("BASE_URL"))
    authorization_page.fill_login(os.getenv("EMAIL_OBSERVER"))
    authorization_page.fill_password(os.getenv("PASSWORD_ADMIN"))
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()

@pytest.fixture
@allure.step("Авторизуемся под супервизором перед тестом")
def authorization_supervisor(setup_browser):
    authorization_page = AuthorizationPage(browser)

    authorization_page.open_authorization_form(os.getenv("BASE_URL"))
    authorization_page.fill_login(os.getenv("EMAIL_SUPERVISOR"))
    authorization_page.fill_password(os.getenv("PASSWORD_ADMIN"))
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()