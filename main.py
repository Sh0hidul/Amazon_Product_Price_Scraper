# Import necessary librariesw
from selenium import webdriver
from selenium.webdriver.common.by import By

# Additional import
import undetected_chromedriver as web

# Chrome options to configure headless mode to bypass captcha
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--use_subprocess")

# chrome_options.add_experimental_option('detach',True)
# Create a webdriver instance for chrome
browser = webdriver.Chrome(options=chrome_options)

# Open the Amazon product page
browser.get("https://www.amazon.com/Soundcore-Cancelling-"
           "Headphones-Comfortable-Bluetooth/dp/B08HMWZBXC/ref="
           "sr_1_3?crid=PSV6LK1OLZWL&keywords=q30%2Bheadphones&qid"
           "=1706669340&sprefix=q30%2Caps%2C135&sr=8-3&ufe=app_do%3Aamzn1"
           ".fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc&th=1")

# save a screenshot of the page
browser.save_screenshot("screenshot.png")

#Extract the price of the page
price_whole = browser.find_element(By.CLASS_NAME,'a-price-whole').text
price_fraction = browser.find_element(By.CLASS_NAME,"a-price-fraction").text
price = price_whole + '.' + price_fraction

#Extract the product name
product_name_with_description = browser.find_element(By.XPATH,'//*[@id="productTitle"]').text
product_short_name = product_name_with_description.split(',')[0]

#Display the name and price
print(f"Product name is: {product_short_name} and price is: {price}")



# driver.close()
# driver.quit()
