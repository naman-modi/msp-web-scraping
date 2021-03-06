"""
Download BOT :

    This Script makes a google for a particular object
    and downloads all the images of that object from the
    image section in 'Downloaded_Image' Directory

    Use : Can be used to collect images to feed it to AL-ML model

    -- Kshitij Sangar & Naman Modi
"""


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import urllib.request

# Important variables...
search = 'cars'  # Object to search on the internet
Download_Directory = 'Downloaded_Image'
path = 'C:/Users\KSHITIJ R. SANGAR\Desktop\Kshitij Projects\Python projects\chromedriver_win32\chromedriver.exe'


# Setting up path the chrome driver.
driver = webdriver.Chrome(path)

# Getting google home page
driver.get('https://www.google.com')
driver.implicitly_wait(2)

# Making a search.
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(search)
buttons = ActionChains(driver)
buttons.send_keys(Keys.ENTER).perform()
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()

# Downloading Images
count = scroll = 0
while True:
    count += 1
    scroll += 100 # Scrolling 100 pixels everytime.
    try:
        # Finding Image and gettin its source url
        img = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img'.format(count))
        img_url = img.get_property('src')

        # Setting the file name
        filepath = Download_Directory + '/Img_' + str(count) + '.jpg'

        # Downloading the file
        urllib.request.urlretrieve(img_url,filepath)
        driver.implicitly_wait(2)

        # Scrolling the window 100 pixels after retrieving 1 image
        driver.execute_script('window.scrollTo(0, {})'.format(scroll))
        print(count)
    except:
        # If a particular Xpath is not found, it is skipped
        print(str(count) + ' Not found ')

driver.close() # Closes the tab
