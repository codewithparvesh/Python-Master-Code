# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_class_name("gsc-input")

# create action chain object
action = ActionChains(driver)

# click the item
action.click(on_element = element)

# send keys
action.send_keys("Arrays")

# perform the operation
action.perform()
