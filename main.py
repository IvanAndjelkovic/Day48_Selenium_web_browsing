from selenium import webdriver
from selenium.webdriver.common.by import By  

# Option 1: Let Selenium locate driver automatically (Selenium 4.6+)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)




driver.get("https://www.python.org")

# price_eur = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# print(f"The price is {price_eur.text}.{price_cent.text}")

# search_bar =  driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID,value="submit")
# print(button.size)


# #CSS  Selector
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

#XPath


# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')


# print(bug_link.text)

# driver.find_elements(By.CLASS_NAME,value="example")

dates  = driver.find_elements(By.XPATH, value =  '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
for date in dates:
    date_show = date.find_element(By.CSS_SELECTOR, value =  '#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child(4) > time')
    print(date_show.datetime)




driver.quit()