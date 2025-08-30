from conftest import driver
from locators.home_page_locators import HomePageLocators
from pages.order_page import OrderPage
from utils.urls import Urls
import allure


class TestHeaderLogo:
    @allure.title('Клик на лого Самоката в шапке возвращает на главную страницу')
    def test_redirect_samokat_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_header_order_btn()
        order_page.click_samokat_logo()
        order_page.wait_navigating_url(Urls.HOME_PAGE)
        current_url = order_page.get_current_url()
        assert current_url == Urls.HOME_PAGE


    @allure.title('Проверка перенаправления на Dzen.ru при клике на Яндекс в лого шапки')
    def test_redirect_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_header_order_btn()
        order_page.click_yandex_logo()
        order_page.tab_switch()
        order_page.wait_navigating_url(Urls.ZEN_HOME_PAGE)
        current_url = order_page.get_current_url()
        assert current_url == Urls.ZEN_HOME_PAGE
