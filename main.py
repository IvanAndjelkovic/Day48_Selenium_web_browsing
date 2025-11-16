import time 
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Keep  Chrome browser open after  program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Create and  configure  the Chrome  webrdiver
global  driver

driver = webdriver.Chrome(options=chrome_options)

# driver.get
driver.get("https://ozh.github.io/cookieclicker/")

# Click the english button

wait = WebDriverWait(driver, 5)
eng_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]')))
eng_button.click()


number_of_minutes  = 2

time_check=  6
timeout =  60 * number_of_minutes
multiplier = 2

timeout_start  = time.time()

stop_flag = False



def stop():
    time.sleep(3)

    wait = WebDriverWait(driver, 5)
    cookies_per_second_element = wait.until(
                EC.presence_of_element_located((By.ID, "cookiesPerSecond"))
            )
    cookies_per_second_list=cookies_per_second_element.text
    # cookies_per_second = cookies_per_second_list[-1]


    print(f"cookies/second: {cookies_per_second_list}")



    time.sleep(3)
    driver.quit()
      
      


def click_cookie():
    while  not  stop_flag:
        global cookies_count

        wait = WebDriverWait(driver, 5)
        cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bigCookie"]')))
        cookie_button.click()
        #print actual  cookies
        actual_cookies = driver.find_element(By.ID, "cookies")
        cookies_count_full = actual_cookies.text
        cookies_count = int(cookies_count_full.split()[0].replace(",",""))
        
        # return cookies_count
        # print(f"Cookies: {cookies_count}")
        # Add a small sleep to prevent CPU overuse
        time.sleep(0.01)


def  pick_the_element():
    while  not  stop_flag:
        wait = WebDriverWait(driver, 5)

        store_items=driver.find_elements(By.CSS_SELECTOR ,value  = ".product.unlocked.enabled")
        if len(store_items)==0:
            pass


        else  :
            element_number  = len(store_items)-1
            price_element  = store_items[element_number].find_element(By.CLASS_NAME, value  = "price")
            price = int(price_element.text.replace(",",""))
            # print(price)
            print(stop_flag)

            if  price * multiplier < cookies_count:
                            store_items[element_number].click()
                    

            time.sleep(time_check)

   
        # if len(store_items)>0:
        #     if len(store_items)==1:

        #         price_element  = store_items[0].find_element(By.CLASS_NAME, value  = "price")
        #         price = int(price_element.text)
        #         print(price)
        #         if  price * multiplier < cookies_count:
        #             price_element.click()
                
        #     else:
        #         print(len(store_items))

    
        

    


def stopper():
    global stop_flag
    time.sleep(timeout)

    stop_flag = True
    stop()

 





threading.Thread(target=click_cookie).start()
threading.Thread(target=pick_the_element).start()
threading.Thread(target=stopper, daemon=True).start()










        






