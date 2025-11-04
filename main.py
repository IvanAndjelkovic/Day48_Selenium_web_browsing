from selenium import webdriver

# Option 1: Let Selenium locate driver automatically (Selenium 4.6+)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)



driver.get("https://www.amazon.de")
driver.close()