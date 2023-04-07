import pytest
from basepage import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = BasePage(
        driver=webdriver.Chrome(
            service=Service(executable_path=ChromeDriverManager(
                url="https://chromedriver.storage.googleapis.com"
            ).install())
        ))
    # webdriver.Chrome(executable_path='/gender_app/test/chromedriver_mac_arm64/chromedriver'))
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get('http://127.0.0.1:9000/')
    driver.implicitly_wait(15)
    login_link = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')
    login_link.click()
    username_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
    username_input.send_keys('admin')
    password_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')
    password_input.send_keys('111')
    login_button = driver.find_element(By.XPATH, '/html/body/form/div[4]/button')
    login_button.click()
