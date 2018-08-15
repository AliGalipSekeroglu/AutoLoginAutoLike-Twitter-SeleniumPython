from selenium import webdriver
import time
import twitterInfo

browser = webdriver.Firefox()

url="https://twitter.com"
browser.get(url)

time.sleep(2)

username=browser.find_element_by_xpath ("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password=browser.find_element_by_xpath ("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

username.send_keys(twitterInfo.username) 
password.send_keys(twitterInfo.password)
time.sleep(3)

log_in_button = browser.find_element_by_xpath ("//*[@id='page-container']/div/div[1]/form/div[2]/button")
log_in_button.click()

time.sleep(5)

searchArea = browser.find_element_by_xpath ("//*[@id='search-query']")
searchButton=browser.find_element_by_xpath ("//*[@id='global-nav-search']/span/button")

searchArea.send_keys("#Android") #Search the hashtag that you want to search for.
searchButton.click()

time.sleep(5)

"""In order to make an infinite scrool through Javascript"""
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

elements = browser.find_elements_by_css_selector(".ProfileTweet-actionButton.js-actionButton.js-actionFavorite")
#If we want to find only an element,we must write browser.find_element_by_css_selector but if not,we must write browser.find_elements_by_css_selector

for element in elements:
	try:
		element.click()
		time.sleep(2)
	except Exception:
		print("Something is wrong...")

browser.close()
