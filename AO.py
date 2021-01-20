import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import winsound

print("PS5 Bot Copyright (C) 2021  Mahdi Zaini This program comes with ABSOLUTELY NO WARRANTY; for details check included license. This is free software, and you are welcome to redistribute it under certain conditions; check license for conditions.")

item = 'https://ao.com/product/p5hehwsny39500-sony-playstation-playstation-5-console-white-79528-291.aspx' # Variable for the item wanted
options = Options()
options.add_argument("user-data-dir=C:\\Users\\ps5\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(item)
while True:
    try:
        # Code with possible error - error being that there's no add to cart button
        driver.find_element_by_xpath('//*[@id="productInformation"]/div[5]/a').click() # Looks for the 'add to cart button' using xpath
    except:
        driver.get(item) # If the atc button cannot be found, refresh until it is found
    else:
        time.sleep(1)
        driver.get('https://checkout.ao.com/shoppingbasket.aspx#address') # Goes to checkout page after adding to cart
        break
winsound.Beep(899, 5000) # Makes a beep sound for 5 seconds to notify the user that the item is in stock and at checkout page
