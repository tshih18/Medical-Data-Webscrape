from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

browser = webdriver.Firefox(executable_path="/Users/theodoreshih/Downloads/geckodriver")
browser.get("ftp://vhpmale:vis!male@vhnet.nlm.nih.gov/Male/")
delay = 10

PNG_format_link = browser.find_element_by_link_text("PNG_format")
PNG_format_link.click()

# Waits for page to load to find the link and clicks it
while 1:
    try:
        abdomen_link = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, "thighs")))
        abdomen_link.click()
        break
    except:
        continue


time.sleep(15)
for i in range(0, 613):
    a = str(2309 + i)
    pics = browser.find_element_by_link_text("a_vm"+a+".png")
    action_chains = ActionChains(browser)
    action_chains.move_to_element(pics).context_click(pics).perform()
    time.sleep(2)
    pyautogui.typewrite(['down','down','down','down','down','enter'])
    pyautogui.PAUSE = 2
    time.sleep(2)
    pyautogui.typewrite(['enter'])
    #pyautogui.PAUSE = 2
    #time.sleep(2)
    pyautogui.scroll(-1)
    #time.sleep(2)
