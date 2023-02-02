from selenium import webdriver

chrome_driver_path = R"C:/Users/Mr.Nachos/Desktop/Courses/...Udemy/100 Days of Python/ChromeDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com.br/Monster-Manual-Wizards-RPG-Team/dp/0786965614/?_encoding=UTF8&pd_rd_w=aq02E&pf_rd_p=dd41083a-b62d-4da5-8d00-47e50153dbdf&pf_rd_r=NXS8M2Y4HWHN6FDVCQRT&pd_rd_r=bbd9f9ca-35ce-4ec3-a1a2-e80cfd68b1fc&pd_rd_wg=QxLlc&ref_=pd_gw_crs_wish")

price = driver.find_element_by_id("price")
print(price.text)
# Close only a tab
# driver.close()
driver.quit()