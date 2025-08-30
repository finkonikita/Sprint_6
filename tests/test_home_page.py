from conftest import driver
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from utils.urls import Urls
import allure



class TestHeaderLogo:
    @allure.title('Клик на лого Самоката в шапке возвращает на главную страницу')
    def test_redirect_samokat_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_samokat_logo()
        home_page.wait_navigating_url(Urls.HOME_PAGE)
        current_url= home_page.get_current_url()
        assert current_url == Urls.HOME_PAGE


    @allure.title('Проверка редиректа на Dzen.ru при клике на Яндекс в лого шапки')
    def test_redirect_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_yandex_logo()
        home_page.tab_switch()
        home_page.wait_navigating_url(Urls.ZEN_HOME_PAGE)
        current_url = home_page.get_current_url()
        assert current_url == Urls.ZEN_HOME_PAGE
