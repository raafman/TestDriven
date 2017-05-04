import os
from selenium import webdriver

chromedriver = './chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver;

browser = webdriver.Chrome(chromedriver)
browser.get('http://localhost:8000')

assert 'Django' in browser.title