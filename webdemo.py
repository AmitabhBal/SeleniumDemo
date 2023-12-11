import selenium
from time import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
runs=0
line=["first","second","third","fourth","fifth"]
username = "smartestbatmaninlondonn"
password = "abcdefg"
while runs<5:
	driver=webdriver.Chrome(r"C:\Users\balam\webdriver\chromedriver.exe")
	driver.get("https://www.instagram.com/")
	sleep(5)
	driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(username)
	sleep(1)
	driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(password)
	sleep(1)
	driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]").click()
	sleep(7)
	driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
	driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
	sleep(5)
	driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
	sleep(5)
	driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[5]").click()
	sleep(5)
	driver.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[1]/a").click()
	sleep(1)
	driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[4]/div/textarea").send_keys(Keys.ENTER+line[runs])
	sleep(5)
	driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[10]/div/div/button[1]").click()
	sleep(2)
	driver.quit()
	sleep(254)
	runs=runs+1
