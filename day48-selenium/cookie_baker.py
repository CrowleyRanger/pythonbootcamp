from selenium import webdriver
import time
import locale

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

upgrades_list = [
    "buyCursor",
    "buyGrandma",
    "buyFactory",
    "buyMine",
    "buyShipment",
    "buyAlchemy\ lab",
    "buyPortal",
    "buyTime\ machine"
]

chrome_driver_path = R"C:/Users/Mr.Nachos/Desktop/Courses/...Udemy/100 Days of Python/ChromeDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

clock_start = time.time()
buy_upgrade = 5 # seconds

cookie_button = driver.find_element_by_id("cookie")

while True:

    cookie_button.click()
    if time.time() > clock_start + buy_upgrade:

        for upgrade in reversed(upgrades_list):
            cookies = locale.atoi(driver.find_element_by_id("money").text)
            upgrade_price = locale.atoi(driver.find_element_by_css_selector(f"#{upgrade} > b:nth-child(1)").text.split()[-1])
            
            if upgrade_price < cookies:
                selected_upgrade = driver.find_element_by_id(upgrade)
                selected_upgrade.click()
                print(f"{cookies} cookies. Getting {upgrade[3:]} for {upgrade_price}.")
                break
            
        buy_upgrade += 5