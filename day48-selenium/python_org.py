from selenium import webdriver

chrome_driver_path = R"C:/Users/Mr.Nachos/Desktop/Courses/...Udemy/100 Days of Python/ChromeDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

driver.quit()

# Close only a tab
# driver.close()

# In 'python.org'
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
# .
# logo = driver.find_element_by_class_name("python logo")
# print(logo.size)
# .
# documentation_link = driver.find_elements_by_css_selector(".documentation-widget a")
# print(documentation_link.text)
# .
# bug_link = driver.find_element_by_xpath()
# print(bug_link.text)

