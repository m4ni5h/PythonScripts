from selenium import webdriver
import time

d = webdriver.Chrome()
d.get('https://financials.morningstar.com/ratios/r.html?t=INE154A01025&culture=en&platform=sal')
time.sleep(2)
d.find_element_by_css_selector('.large_button').click()
time.sleep(2)
d.quit()