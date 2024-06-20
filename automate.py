import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui
import cv2
import pyocr
import pyocr.builders
from PIL import Image

import time

tools = pyocr.get_available_tools()
tool = tools[0]

options = Options()

options.add_argument("-start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

driver.get("https://sushida.net/play.html")
time.sleep(7)

location_start_button = pyautogui.locateOnScreen('./img/start.png', confidence=0.6)
point_start_button = pyautogui.center(location_start_button)
x_start_button, y_start_button = point_start_button
pyautogui.click(x_start_button, y_start_button)
time.sleep(2)

location_course_button = pyautogui.locateOnScreen('./img/course.png', confidence=0.8)
point_curse_button = pyautogui.center(location_course_button)
x_course_button, y_course_button = point_curse_button
pyautogui.click(x_course_button, y_course_button)
time.sleep(1)

pyautogui.press('Enter')
time.sleep(2)

count = 0
while True:
  if count > 100:
    break
  game_window = driver.find_element(By.XPATH, '//*[@id="#canvas"]')
  game_window.screenshot('./img/game_window.png')
  game_window_img = cv2.imread('./img/game_window.png', cv2.IMREAD_GRAYSCALE)
  # game_window_img = cv2.resize(game_window_img, (500, 500))

  ret2, img_otsu = cv2.threshold(game_window_img, 0, 255, cv2.THRESH_OTSU)
  string_img = img_otsu[230:260, 100:400]
  cv2.imwrite('./img/string_img.png', string_img)
  img_org = Image.open('./img/string_img.png')
  builder = pyocr.builders.TextBuilder(tesseract_layout=10)
  result = tool.image_to_string(img_org, lang="jpn", builder=builder)
  print(result)
  pyautogui.typewrite(result)
  time.sleep(1)
  count += 1

time.sleep(100)
