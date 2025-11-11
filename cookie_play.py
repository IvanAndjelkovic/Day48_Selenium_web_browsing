import time 
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

# driver.get
driver.get("https://ozh.github.io/cookieclicker/")

# Click the english button

wait = WebDriverWait(driver, 5)
eng_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]')))
eng_button.click()



timeout =  60*5
time_check=  5



def click_cookie(driver):
    wait = WebDriverWait(driver, 5)
    cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bigCookie"]')))
    cookie_button.click()
    #print actual  cookies
    actual_cookies = driver.find_element(By.ID, "cookies")
    cookies_count_full = actual_cookies.text
    cookies_count = cookies_count_full.split()[0]
    # return cookies_count
    print(f"Cookies: {cookies_count}")






timeout_start  = time.time()

while time.time()<timeout_start + timeout:
    click_cookie(driver)




    store_items=driver.find_elements(By.CSS_SELECTOR ,value  = ".product.unlocked.enabled")
    if len(store_items)>0:
        if len(store_items)==1:
            print(store_items[0].get_attribute("text"))
        else:
            print(len(store_items))
        
    
    else:
        pass
 





        






