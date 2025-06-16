from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import ElementClickInterceptedException
from bs4 import BeautifulSoup
from time import sleep
import requests


form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdx3TqDOy3v8YdzgXjRNmmiRGwKj1mEuPNpZUAbhJLk9gfZuA/viewform?usp=header"
zillow = "YOUR_ZILLOW_PROPERTY_URL"

response = requests.get(zillow)

soup = BeautifulSoup(response.text,"html.parser")

# gathering all data

links = [link.get("href") for link in soup.select(".search-container .StyledPropertyCardPhotoBody a")]
prices = [price.getText().split('+')[0].split('/')[0] for price in soup.select(".search-container .PropertyCardWrapper__StyledPriceLine")]
addresses = [address.getText().replace("|","").strip() for address in soup.select(".search-container .StyledPropertyCardDataWrapper a address")]


# entering all data in form

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)

driver.get(form_url)

for i in range(len(links)):
    sleep(1)
    field = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field.send_keys(addresses[i],Keys.TAB,prices[i],Keys.TAB,links[i],Keys.TAB,Keys.ENTER)
    sleep(1)
    driver.find_element(By.XPATH,'//a[contains(text(),"Submit another response")]').click()
    print(i)