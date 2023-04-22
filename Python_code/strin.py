from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.common.by import By


s = time.time()
driver = webdriver.Chrome(executable_path ="chromedriver_win32\chromedriver.exe")

# Navigate to Google
driver.get("https://www.google.com/")
# driver.get("https://www.google.com/search?q=site%3Ayoutube.com+openinapp.co")
time.sleep(2)

driver.find_element(By.CLASS_NAME,'gLFyf').send_keys('site:youtube.com openinapp.co')
driver.find_elements(By.NAME,'btnK')[1].click()
time.sleep(2)


# for the next button
lst=[]
cnt =0
try:
    while 1:
        cnt+=1
        print("Working On Page No: ", cnt)
        link = driver.find_elements(By.TAG_NAME, "a")
        # https://www.youtube.com/c/OpeninApp
        for i in link:
            temp = i.get_attribute('href')

            temp= str(temp)[:23]
        #     print(temp)
            if temp == "https://www.youtube.com":
        #         
                x = i.get_attribute("href")
                if x not in lst:
                    lst.append(i.get_attribute("href"))
        #             print(i.get_attribute("href"))

        #     if 'youtube' in temp:
        #         print(i.get_attribute("href"))
        #         lst.append(i.get_attribute("href"))


        driver.find_element(By.ID,"pnnext").click()
        
except:
    print("done")
print(len(lst))


print(len(lst))
print(type(lst[0]))
for i in lst:
    print(lst)

e = time.time()

print("time taken ",e-s)