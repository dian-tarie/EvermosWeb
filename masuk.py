from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Windows\System32\chromedriver.exe")
driver.get("https://evermos.com/login")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/form/label[1]/span[2]/input").send_keys("621223334444")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/form/label[2]/span[2]/input").send_keys("password")
time.sleep(3)

#button masuk
inputElement=driver.find_element_by_xpath("//*[@id='__layout']/div/div[3]/button")
inputElement.send_keys("\n")  #send enter for links, buttons