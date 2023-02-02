# from selenium import webdriver

# chrome_driver_path = R"C:/Users/Mr.Nachos/Desktop/Courses/...Udemy/100 Days of Python/ChromeDriver/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://secure-retreat-92358.herokuapp.com/")

# input_area = driver.find_element_by_css_selector("input.form-control:nth-child(3)")
# input_area.send_keys("Lythras")

# input_area = driver.find_element_by_css_selector("input.form-control:nth-child(4)")
# input_area.send_keys("Crowley")

# input_area = driver.find_element_by_css_selector("input.form-control:nth-child(5)")
# input_area.send_keys("xpaceranger@gmail.com")

# sign_up_button = driver.find_element_by_css_selector(".btn")
# sign_up_button.click()

# driver.quit

import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

num = '12,445,683'

print(locale.atoi(num))