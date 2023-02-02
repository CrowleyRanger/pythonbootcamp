from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
WEBDRIVER_PATH = "C:/Users/Mr.Nachos/Desktop/Courses/...Udemy/100 Days of Python/webdriver/geckodriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        options = Options()
        options.add_argument('-private')
        self.driver = webdriver.Firefox(executable_path=driver_path, options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()

        time.sleep(55)
        while True:
            try:
                self.down = float(self.driver.find_element_by_class_name("upload-speed").text)
                self.up = float(self.driver.find_element_by_class_name("download-speed").text)
                print("Download speed:", self.down)
                print("Upload speed:", self.up)
            except:
                time.sleep(2)
            else:
                break
            
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")

bot = InternetSpeedTwitterBot(WEBDRIVER_PATH)
bot.get_internet_speed()
if PROMISED_DOWN > bot.down:
    bot.tweet_at_provider()