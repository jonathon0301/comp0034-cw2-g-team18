import random
import time
from selenium.webdriver.common.by import By


def test_index_html(driver):
    """
    GIVEN the app is not running
    WHEN the app is called to run
    THEN the index page will show text "Please Log In!"
    """
    driver.get("http://127.0.0.1:9000/")
    time.sleep(5)
    h1_element = driver.find_element(By.XPATH, "/html/body/div/h1[2]")
    h1_text = h1_element.text
    assert h1_text.casefold() == "Please Log In!".casefold()


def test_main_function(driver, login):
    """
    GIVEN the app is running
    WHEN the user successfully logged in
    THEN text "Industry" will be shown on the page
    WHEN the user clicks on "Industry"
    THEN text "Education" will be shown on the page
    WHEN the user clicks on "Education"
    THEN text "Average" will be shown on the page
    """
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
    """
    GIVEN the app is running, user successfully logged in, and user is on the data table page
    WHEN the user clicks on "Home" on the navigation bar
    THEN the app returns to the index_second page
    """
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/ul/li[1]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[1]/a').click()
    time.sleep(2)
    assert (
            "Industry" in driver.find_element(By.XPATH, '/html/body/div/ul/li[1]/a').text
    )


def test_unmatch_login(driver):
    """
    GIVEN the user is trying to log in
    WHEN the password and username are not matched as in the database
    THEN the flash message will show "Wrong Username or Password!"
    """
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
    """
    GIVEN the user is logged in
    WHEN the user clicks on Logout on the Navigation Bar
    THEN the user will be logged out to the index page
    """
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a').click()
    time.sleep(2)
    assert (
            "Please Log In!" in driver.find_element(By.XPATH, '/html/body/div/h1[2]').text
    )


def test_login_to_register(driver):
    """
    GIVEN the app is running and is on log in page
    WHEN the user clicks on Register button
    THEN it directs to the register page
    """
    driver.get('http://127.0.0.1:9000/')
    driver.implicitly_wait(15)
    login_link = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')
    login_link.click()
    register_button = driver.find_element(By.XPATH, '/html/body/form/div[4]/a')
    register_button.click()
    assert (
            "register" in driver.find_element(By.XPATH, '/html/body/form/div[1]/h5').text
    )


def test_edge_case(driver, login):
    """
    GIVEN the user is logged in
    WHEN the user tries to look at data of companies which has Not Provided as Employer Size
    THEN it will raise ValueError
    """
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/ul/li[3]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/ul/li[5]/a').click()
    time.sleep(2)
    assert ValueError


def test_register(driver):
    """
    GIVEN the user is not logged in
    WHEN the user registers with a valid username and matched password
    THEN the app directs to the log in page
    """
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


def test_register_reset(driver):
    """
    GIVEN the user is not logged in
    WHEN the user clicks reset during registration
    THEN all inputs will be deleted
    """
    driver.get('http://127.0.0.1:9000/')
    time.sleep(2)
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a').click()
    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys('admin{}'.format(random.randint(0, 1000)))
    driver.find_element(By.XPATH, '/html/body/form/div[5]/button[1]').click()
    assert (
            driver.find_element(By.XPATH, '//*[@id="id_username"]').get_attribute("value") == ""
    )


def test_unmatch_register(driver):
    """
    GIVEN the user is not logged in
    WHEN the user tries to register with unmatched password
    THEN the flash message will warn "Unmatched!"
    """
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
    """
    GIVEN the user is not logged in
    WHEN the user wants to register with an existing username
    THEN the flash message will show "Username Exists!"
    """
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
    """
    GIVEN the user is logged in
    WHEN the user clicks on Gender Pay Gap Data Set button on the navigation bar
    THEN it will present full dataset prepared by the developer
    """
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a').click()
    time.sleep(2)
    assert (
            "DiffMeanHourlyPercent" in driver.find_element(By.XPATH, '/html/body/div/div/table/thead/tr/th[1]').text
    )
    assert (
            "DiffMedianHourlyPercent" in driver.find_element(By.XPATH, '/html/body/div/div/table/thead/tr/th[2]').text
    )
