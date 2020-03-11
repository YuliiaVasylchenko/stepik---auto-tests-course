from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
browser.find_element_by_xpath("//button[text()='Book']").click()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    answer = browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_xpath("//button[text()='Submit']").click()


finally:
    time.sleep(10)
    browser.quit()
