import pytest
from basepage import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = BasePage(
        driver=webdriver.Chrome(executable_path='/comp0034-cw2-g-team18/gender_app/test/chromedriver_mac_arm64'
                                                '/chromedriver'))
    yield driver
    driver.quit()
