"""
This script logins to your Instagram Account and
displays the text of all the posts by simultaneous
scrolling.
"""
#!/usr/bin/python
import sys

from selenium import webdriver
from sys_rar import PracticePWD
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


#You can either pass the argument from command prompt or send it manually.
argsLen = len(sys.argv)
if argsLen == 1:
    print("Please give the path to chrome driver.")
elif argsLen > 2:
    print("Please give the only 1 argument, that is, path to chrome driver. No other argument required.")

#setting the path for the driver   
path = str(sys.argv[1])

# Driver Location
driver = webdriver.Chrome(path)

# Getting the INSTAGRAM login page
path = 'https://www.instagram.com/accounts/login/'
driver.get(path)

# Waiting to load the page
driver.implicitly_wait(4)


# Sending UserName to the TextBox ------------------------------------------------------------------------
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys("YourInsta_Userid")

# Sending Password to the TextBox
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys("YourInsta_Password")

# Click on the submit button
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
driver.implicitly_wait(5)

# Notification Pop-up ------------------------------------------------------------------------------------
if "Try on desktop" in driver.page_source:
     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
     driver.implicitly_wait(20)

article = '//*[@id="react-root"]/section/main/section/div/div[2]/div' #It grab the information of a particular article at a time.
count = j = 0
scroll = 0
while j <= 20:
    count += 1
    j += 1
    if count == 7 or count > 7:
        count = 7

    print(str(j), " - " ,str(count)) # Displaying on the console -----------------------------------------
    try:
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, article + '/article[{}]'.format(count)))
        )
    except:
        print("Couldn't load Element...")

    # Getting text of an Insta. post... -------------------------------------------------------------------
    element = driver.find_elements_by_xpath(article + '/article[{}]'.format(count))
    for i in element:
        print(i.text)
    print('\n\n')
    driver.implicitly_wait(2)

    # Scrolling page for the height of the screen ---------------------------------------------------------
    scroll += 1070 #Page will scroll by 1070 pixels
    driver.execute_script("window.scrollTo(0, {});".format(scroll))
