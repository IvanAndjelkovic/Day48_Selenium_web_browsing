from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Keep  Chrome browser open after  program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Create and  configure  the Chrome  webrdiver

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://en.wikipedia.org/wiki/Main_Page")


#  Find  element  by  Link Text

all_portals  = driver.find_element(By.LINK_TEXT,  value  =  "Content portals")
# all_portals.click()

# tag  =driver.find_element(By.XPATH,   value = '//*[@id="articlecount"]/ul/li[2]/a[1]')
# # tag = driver.find_element(By.CSS_SELECTOR,  value =  "#articlecount  a")
# number_of_articles  = tag.get_attribute("text")
# print(number_of_articles)


# Wait for the search input field to be present
# search= driver.find_element(By.ID, "searchInput")
# search.send_keys("Python")
# text  = search_box.get_attribute("text")
# print(text)

try:
    # Wait up to 10 seconds for element to be clickable
    wait = WebDriverWait(driver, 10)
    search = wait.until(
        EC.element_to_be_clickable((By.ID, "searchInput"))
    )
    
    # Interact with the element
    search.click()  # Focus the element first
    search.clear()  # Clear any existing text
    search.send_keys("Python")
    search.send_keys(Keys.RETURN)
    
except Exception as e:
    print(f"An error occurred: {e}")



# # Click or focus the search box (optional)
# search_box.click()

# # search = driver.find_element(By.XPATH, value = '//*[@id="searchform"]/div/div/div[1]/input')

# # Sending Keyboard input  to Selenium
# # search.send_keys("Python")
# search_box.send_keys("Python")


# # Send Enter key to submit the search
# search_box.send_keys(Keys.ENTER)

 # driver.quit()