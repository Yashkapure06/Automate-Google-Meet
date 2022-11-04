import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def join_meet():

    opt = Options()

    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")

    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })

    driver = webdriver.Chrome(
        chrome_options=opt, executable_path='chromedriver.exe')

    driver.get('https://accounts.google.com/')

    username = driver.find_element_by_id('identifierId')
    username.click()
    username.send_keys('Your Email Id')

    next = driver.find_element_by_xpath(
        '//*[@id="identifierNext"]/div/button/span')
    next.click()
    time.sleep(5)
    password = driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input')
    password.click()
    password.send_keys('Your Password')

    next = driver.find_element_by_xpath(
        '//*[@id="passwordNext"]/div/button/span')
    next.click()
    time.sleep(5)

    driver.get('https://meet.google.com/ihh-bqcp-zjs')

    time.sleep(5)

    camera = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[12]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[5]/div[2]/div/div[1]/span'
        )
    camera.click()

    time.sleep(5)

    mic = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[12]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[5]/div[1]/div/div/div[1]/span/span/div/div[1]')
    
    
    mic.click()

    time.sleep(5)

    join = driver.find_element(by=By.XPATH, value='//*[@id="yDmH0d"]/c-wiz/div/div/div[12]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button')
    
    
    join.click()
    input()
    
join_meet()