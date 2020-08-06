import time
import webbrowser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def check_exists_by_id(iden,web_driver):
    try:
        web_driver.find_element_by_id(iden)
    except NoSuchElementException:
        return False;
    return True;

url = "http://www.limudnaim.co.il/node/11313/update-modified" # desired webpage
user_name = "or.ba402@gmail.com" # desired username/email
password = "password" #desired password

while True:
        driver = webdriver.Chrome()
        driver.get(url)
        if check_exists_by_id('edit-name',driver):
                sbox = driver.find_element_by_id('edit-name')
                sbox.send_keys(user_name)
                sbox = driver.find_element_by_id('edit-pass')
                sbox.send_keys(password)
                submit = driver.find_element_by_id('edit-submit')
                submit.click()
        time.sleep(10805) #in seconds - how much time between profile update
        driver.quit();

