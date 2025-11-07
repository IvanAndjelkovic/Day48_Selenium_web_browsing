from selenium import webdriver
from selenium.webdriver.common.by import By  



# Keep  Chrome browser open after  program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Create and  configure  the Chrome  webrdiver

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://en.wikipedia.org/wiki/Main_Page")

tag  =driver.find_element(By.XPATH,   value = '//*[@id="articlecount"]/ul/li[2]/a[1]')
# tag = driver.find_element(By.CSS_SELECTOR,  value =  "#articlecount  a")
number_of_articles  = tag.get_attribute("text")
print(number_of_articles)



driver.quit()