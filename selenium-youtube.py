from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import time

# entrar a youtube y entrar al menu tendencias

browser = webdriver.Chrome()
browser.get("https://www.youtube.com/")
browser.maximize_window()
searchbutton = browser.find_element_by_css_selector("#search")
searchbutton.send_keys("Beyonce Dangerous")
startsearch = browser.find_element_by_css_selector("#search-icon-legacy > yt-icon")
startsearch.click()
time.sleep(5)
firstresult = browser.find_element_by_css_selector("#video-title > yt-formatted-string")
firstresult.click()

keyboard.press("f")
time.sleep(20)
keyboard.press("f")
time.sleep(0.5)
#searchbutton.send_keys(ctrl+a)
#seachbutton.send_keys(keyboard.press("BACKSPACE"))

searchbutton1 = browser.find_element_by_css_selector("#search")
#actionChains = ActionChains(browser)
#actionChains.double_click(searchbutton1).perform()
searchbutton1.click()
keyboard.press_and_release("CONTROL+a")

time.sleep(1)
keyboard.press("BACKSPACE")



time.sleep(3)
searchbutton1.send_keys("GIBUS IS THA BOSS!")


