from PIL import ImageGrab
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import shutil


def del_file(filepath):
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(driver.title)
if os.path.exists('img/pic1'):
    del_file('img/')

num = 3
for i in range(1, num, 1):
    box = (982, 296, 1741, 660)
    im = ImageGrab.grab(box)
    images_name = 'pic' + str(i)
    im.save('img/' + images_name, 'tiff')
    # im.show()
    ele = driver.find_element_by_id("radio_moveNextDiv").click()
    size = driver.find_element_by_id("radio_moveNextDiv").size
    print(size)
    time.sleep(0.5)
