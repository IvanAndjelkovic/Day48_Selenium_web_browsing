from selenium import webdriver

# Option 1: Let Selenium locate driver automatically (Selenium 4.6+)
driver = webdriver.Chrome()

# # Option 2: Specify path explicitly if needed
# driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

driver.get("https://www.amazon.com")
driver.close()