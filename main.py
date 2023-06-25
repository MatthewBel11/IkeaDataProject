from selenium import webdriver #Allows us to open a web browser
from selenium.webdriver.common.by import By
import os
import pandas as pd


rows_list = []


# driver.implicitly.wait(30) is better than time.sleep(30) because it only takes the amount of time needed
# to find the element rather than the full 30 seconds making it faster for programs.
# Don't need to repeat this everytime we try to get something as it sets it for all things in future,
# Will only need repeated if wanting to chane the time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


os.environ['PATH'] += r"\SeleniumDrivers"

driver = webdriver.Chrome(options=options)

driver.get('https://www.amazon.co.uk/s?k=banana&sprefix=Banana%2Caps%2C102&ref=nb_sb_ss_ts-doa-p_3_6')

elem_list = driver.find_element(By.CSS_SELECTOR,'div.s-main-slot.s-result-list.s-search-results.sg-row')

items = elem_list.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

for item in items:
    title = item.find_element(By.TAG_NAME, 'h2').text
    price = "No Price Available"
    rating = "No Rating Found"

    try:
        rating = item.find_element(By.CLASS_NAME, 'a-icon-alt').get_attribute('innerHTML')

    except:
        pass


    try:
        price = item.find_element(By.CLASS_NAME, 'a-price').text.replace('\n', '.')

    except:
        pass

    tempList = [title, price, rating]
    rows_list.append(tempList)

df = pd.DataFrame(rows_list, columns=['Product Title', 'Product Price', 'Product Rating'])
df.to_csv('Banana.csv', index_label=False)

driver.close() #Not sure what this does?

#driver.quit() #Quits the webdriver window, useful so you don't have x100 windows when testing lel



