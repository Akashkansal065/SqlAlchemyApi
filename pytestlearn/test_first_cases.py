import pytest
from termcolor import colored, cprint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def suite():
    # print(module)
    global driver
    cprint('\nbefore suite', 'red')
    yield
    cprint('after suite', 'red')


@pytest.fixture(scope='function')
def beforeaftermeth():

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://magicbricks.com')
    driver.maximize_window()
    print('launch browser')
    yield
    driver.quit()
    print('close browser')


@pytest.mark.usefixtures("suite", "beforeaftermeth")
def test_one():
    #driver.find_element_by_id('keyword').click().send_keys('pappu')
    print("the beginning of an end")
    assert "pappu" == "rahul", 'Rahul gandhi is pappu'
    print('after pappu fail')
    assert "rahul" in "rahul is damroo", 'pappu antonio'


def test_two(suite, beforeaftermeth):
    print("the beginning of an end")
    driver.find_element_by_id('keyword').click().send_keys('pappu')


def test_otwo(suite, beforeaftermeth):
    print("the beginning of two")
    driver.find_element_by_id('keyword').click().send_keys('pappu')
