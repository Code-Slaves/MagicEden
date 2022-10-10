import os
from shutil import which
from selenium import webdriver
from bs4 import BeautifulSoup as b 
import time 
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
import string
from selenium.webdriver.firefox.options import Options
import multiprocessing
import requests


user_agent = UserAgent()
options = webdriver.FirefoxOptions()
#options.add_argument("--disable-blink-features=AutomationControlled")
#options.headless = True
options.add_argument(f"user_agent={user_agent.ie}")
driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
actions = ActionChains(driver)
#Добавление расширения
driver.install_addon('phantom_app-22.9.19.xpi', temporary=True)
wait = WebDriverWait(driver, 60)

fl = open("seed.txt", 'r')
file = fl.read()
list = file.split(" ")
x = -1
y = 0


try:
	driver.get(url='https://magiceden.io/')
	driver.maximize_window()
	driver.switch_to.window(driver.window_handles[1])
	driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/div[2]/button[2]").click()
	wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/form/div/div[2]/div[1]/input")))
	while x != 11:
		x = x+1
		y = y+1
		wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/form/div/div[2]/div["+str(y)+"]/input"))).send_keys(list[x])
		
	wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/form/button")))
	wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/form/button"))).click()
	time.sleep(3)
	wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/form/button")))
	wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/form/button"))).click()
	pasword_ = "12345678"
	wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/form/div[1]/div[2]/input")))
	wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/form/div[1]/div[2]/input"))).send_keys(pasword_)
	wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/form/div[1]/div[2]/div/div/input"))).send_keys(pasword_)
	wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/form/div[2]/span"))).click()
	wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/form/button"))).click()
	

	driver.switch_to.window(driver.window_handles[0])

	def magiceden_connect():
		driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/header/nav/div[2]/div[2]/div/button[2]").click()
		time.sleep(1)
		wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[3]/div/div/div[2]/ul/li/button")))
		wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/div/div/div[2]/ul/li/button"))).click()
		time.sleep(1)
		driver.switch_to.window(driver.window_handles[2])
		time.sleep(1)
		wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div[2]/div/button[2]")))
		wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div/button[2]"))).click()
		driver.switch_to.window(driver.window_handles[0])

	magiceden_connect()

	def offer_collection():
		print("Input collection tag name:")
		collection_name =  "mno"   #str(input())
		search = "https://magiceden.io/marketplace/"+collection_name
		driver.maximize_window()
		driver.get(url=search)
		
		wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/input")))
		wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/input"))).click()

		wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]")))
		wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]"))).click()

		screen = driver.page_source
		soup = b(screen, "html.parser")
		urls_all_div = soup.find('div')

		a = ""

		for i in urls_all_div.find_all('a', href=True):
			a = a + "," + "https://magiceden.io/" + (i['href'])
		print(a)

	offer_collection()


except Exception as ex:
	print(ex)

finally:
	driver.quit()




