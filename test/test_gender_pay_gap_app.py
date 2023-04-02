import random
import time
from selenium.webdriver.common.by import By


def test_index_html(driver):
    driver.get("http://127.0.0.1:9000/")
    time.sleep(5)
    h1_element = driver.find_element(By.XPATH, "/html/body/div/h1[2]")
    h1_text = h1_element.text
    assert h1_text.casefold() == "Please Log In!".casefold()


def test_data_query(driver, login):
    time.sleep(2)
    assert (
            "Industry" in driver.find_element(By.XPATH, '/html/body/div/ul/li[1]/a').text
    )
    driver.find_element(By.XPATH, '/html/body/div/ul/li[1]/a').click()
    time.sleep(2)
    assert (
            "Education" in driver.find_element(By.XPATH, '/html/body/div/ul/li[1]/a').text
    )
    driver.find_element(By.XPATH, '/html/body/div/ul/li[1]/a').click()
    time.sleep(2)
    assert (
            "Average" in driver.find_element(By.XPATH, '/html/body/div/table/thead/tr/th[2]').text
    )


def test_home(driver, login):
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/ul/li[1]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[1]/a').click()
    time.sleep(2)
    assert (
            "Industry" in driver.find_element(By.XPATH, '/html/body/div/ul/li[1]/a').text
    )


def test_unmatch_login(driver):
    driver.get('http://127.0.0.1:9000/')
    driver.implicitly_wait(15)
    login_link = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')
    login_link.click()
    username_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
    username_input.send_keys('admin')
    password_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')
    password_input.send_keys('123456')
    login_button = driver.find_element(By.XPATH, '/html/body/form/div[4]/button')
    login_button.click()
    time.sleep(2)
    assert "Wrong Username or Password!"


def test_logout(driver, login):
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a').click()
    time.sleep(2)
    assert (
            "Please Log In!" in driver.find_element(By.XPATH, '/html/body/div/h1[2]').text
    )


def test_edge_case(driver, login):
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/ul/li[3]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/ul/li[5]/a').click()
    time.sleep(2)
    assert ValueError


def test_register(driver):
    driver.get('http://127.0.0.1:9000/')
    time.sleep(2)
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a').click()
    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys('admin{}'.format(random.randint(0, 1000)))
    driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys('111')
    driver.find_element(By.XPATH, '//*[@id="id_confirm"]').send_keys('111')
    driver.find_element(By.XPATH, '/html/body/form/div[5]/button[2]').click()
    assert (
            "welcome login" in driver.find_element(By.XPATH, '/html/body/form/div[1]/h5/a').text
    )


def test_unmatch_register(driver):
    driver.get('http://127.0.0.1:9000/')
    time.sleep(2)
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a').click()
    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys('admin{}'.format(random.randint(0, 100)))
    driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys('111')
    driver.find_element(By.XPATH, '//*[@id="id_confirm"]').send_keys('222')
    driver.find_element(By.XPATH, '/html/body/form/div[5]/button[2]').click()
    assert "Unmatched!"


def test_exist_username(driver):
    driver.get('http://127.0.0.1:9000/')
    time.sleep(2)
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a').click()
    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys('admin')
    driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys('111')
    driver.find_element(By.XPATH, '//*[@id="id_confirm"]').send_keys('111')
    driver.find_element(By.XPATH, '/html/body/form/div[5]/button[2]').click()
    assert "Username Exists!"


def test_display_alldata(driver, login):
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a').click()
    time.sleep(2)
    assert (
            "DiffMeanHourlyPercent" in driver.find_element(By.XPATH, '/html/body/div/div/table/thead/tr/th[1]').text
    )
    assert (
            "DiffMedianHourlyPercent" in driver.find_element(By.XPATH, '/html/body/div/div/table/thead/tr/th[2]').text
    )
