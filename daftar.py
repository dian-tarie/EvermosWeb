from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Windows\System32\chromedriver.exe")
driver.get("https://evermos.com/registration")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div/form/div[1]/div[2]/div/div/div[2]/input").send_keys("0816590270")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div/form/div[2]/div[2]/input").send_keys("Dian Testing")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div/form/div[3]/div[2]/input").send_keys("Testing123")
time.sleep(3)

#area
inputElement =driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div/form/div[4]/div[2]/input")
inputElement.send_keys("\n")  #send enter for links, buttons
driver.find_element_by_xpath("//*[@id='__layout']/div/div[3]/div/div[3]/div/form/input").send_keys("Batujajar")
driver.implicitly_wait(10) # seconds
driver.find_element_by_xpath("//*[@id='__layout']/div/div[3]/div/div[3]/div/div[2]/a").click()
kecamatan=driver.find_element_by_xpath("//*[@id='__layout']/div/div[3]/div/div[3]/div/div[2]/a").is_selected()
#print(kecamatan)

#checkbox referral
inputElement = driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div/form/div[5]/div/div[1]/label/input")
inputElement.send_keys(Keys.SPACE) #for checkbox etc
time.sleep(3)
driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div/form/div[5]/div[3]/div/input").send_keys("COBARUMAHAN")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div/form/div[5]/div[3]/a").click()
time.sleep(3)

#checkbox syarat & ketentuan
inputElement = driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div/form/div[6]/div[1]/label/input")
inputElement.send_keys(Keys.SPACE) #for checkbox etc
time.sleep(3)
driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div/form/button").click()

#driver.close()
