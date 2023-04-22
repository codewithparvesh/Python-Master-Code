from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path ="D:\Coding\Pythob Library\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# these buttons and drop down manu all are locator

# driver.maximize.window() #maxmize the wndoe
# print(driver.title)
# print(driver.current_url)
driver.find_element(By.ID,'name').send_keys('parvesh')
# driver.find_element_by_id("name").send_keys("Parvesh")

# driver.find_element('id','name').send_keys("parves")
# driver.find_element('id','alertbtn').click()

#  where we can not use id and class or ther locator then we use the css selector or xpath selector




