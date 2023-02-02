from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

## NOT FINISHED ##

WEBDRIVER_PATH = "C:/Users/Mr.Nachos/Desktop/Courses/...Udemy/100 Days of Python/webdriver/geckodriver.exe"
USERNAME = "username"
PASSWORD = "password"

class InstaFollower():
    def __init__(self, driver_path):
        options = Options()
        options.add_argument('-private')
        self.driver = webdriver.Firefox(executable_path=driver_path, options=options)
        self.driver.get("https://www.instagram.com/")

    def login(self):      
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

    def find_followers(self):
        pass

    def follow(self):
        pass

    def quit(self):
        self.driver.quit()

instaFoollower = InstaFollower(WEBDRIVER_PATH)

while True:
    try:
        instaFoollower.login()
    except:
        time.sleep(2)
    else:
        break


