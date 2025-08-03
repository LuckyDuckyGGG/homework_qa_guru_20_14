import os
import random
import time

from faker import Faker
from selene.support.shared import browser

from armobile_web.models.pages.admin_panel_page import AdminPanelProjectPage
from conftest import setup_browser
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("BASE_URL")
fake = Faker('ru_RU')

def test_create_project_admin(authorization_admin, setup_browser):
    create_project = AdminPanelProjectPage(browser)
    project_name = f"Проект{random.randint(1, 9999)}"

    create_project.click_project_create()
    create_project.fill_project_name(project_name)
    create_project.fill_project_city(fake.city_name())
    create_project.submit_create_project()
    create_project.should_table_have_project_name(project_name)

def test_create_project_expert(authorization_expert, setup_browser):
    create_project = AdminPanelProjectPage(browser)

    create_project.should_button_create_disabled()

def test_create_project_master(authorization_master, setup_browser):
    create_project = AdminPanelProjectPage(browser)

    create_project.should_button_create_disabled()

def test_create_project_subcontractor(authorization_subcontractor, setup_browser):
    create_project = AdminPanelProjectPage(browser)

    create_project.should_button_create_disabled()

def test_create_project_observer(authorization_observer, setup_browser):
    create_project = AdminPanelProjectPage(browser)

    create_project.should_button_create_disabled()

def test_create_project_supervisor(authorization_supervisor, setup_browser):
    create_project = AdminPanelProjectPage(browser)

    time.sleep(2)
    create_project.open_project_tab(url)
    create_project.should_button_create_disabled()