from selenium import webdriver
from selenium.webdriver.common.by import By  

# Option 1: Let Selenium locate driver automatically (Selenium 4.6+)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)




driver.get("https://www.amazon.de/Lenovo-Tablet-Display-MediaTek-Android/dp/B0DF2G9HK7/ref=zg_bs_g_429874031_d_sccl_1/262-0067990-5553324?th=1")

price_eur = driver.find_element(By.CLASS_NAME,value="a-price-whole")
price_cent = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
print(f"The price is {price_eur.text}.{price_cent.text}")
driver.quit()