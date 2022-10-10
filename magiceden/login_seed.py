from selenium import webdriver
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

def mint():

        options = Options()
        chrome_path = which("chromedriver")
        options.add_extension("Phantom.crx")
        options.add_argument("--disable-gpu")
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path=chrome_path, options=options)

        driver.get("https://magiceden.io/launchpad/thirsty_cactus_garden_party")
        driver.maximize_window()
        txt = open("login.txt", 'r')
        read_txt = txt.readlines()
        values = []
        for x in read_txt:
                values.append(x)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[@class='sc-bdfBQB fatHKg']")))
        recovery_phrase = driver.find_element(By.XPATH,"//button[@class='sc-bdfBQB fatHKg']").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Secret phrase']")))

        text_area = driver.find_element(By.XPATH,"//textarea[@placeholder='Secret phrase']").send_keys(values[0])
        import_btn = driver.find_element(By.XPATH,"//button[@class='sc-bdfBQB bzlPNH']").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
        password1 = driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(values[1])
        password2 = driver.find_element(By.XPATH,"//input[@placeholder='Confirm Password']").send_keys(values[1])
        check_box = driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Continue')]")))
        continue_ = driver.find_element(By.XPATH,"//button[contains(text(),'Continue')]")
        driver.execute_script ("arguments[0].click();",continue_)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Finish')]")))
        finish = driver.find_element(By.XPATH,"//button[contains(text(),'Finish')]")
        driver.execute_script ("arguments[0].click();",finish)