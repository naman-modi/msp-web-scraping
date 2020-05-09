"""
This script logins to your Instagram Account and
displays the text of all the posts by simultaneous
scrolling.
"""

from selenium import webdriver
from sys_rar import PracticePWD
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Driver Location
driver = webdriver.Chrome("C:/Users\KSHITIJ R. SANGAR\Desktop\Kshitij Projects\Python projects\chromedriver_win32\chromedriver.exe")

# Getting the INSTAGRAM login page
path = 'https://www.instagram.com/accounts/login/'
driver.get(path)

# Waiting to load the page
driver.implicitly_wait(5)


# Sending UserName to the TextBox ------------------------------------------------------------------------
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys("_.h.o.r.i.z.o.n._")

# Sending Password to the TextBox
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(PracticePWD)

# Click on the submit button
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
driver.implicitly_wait(5)


# Notification Pop-up ------------------------------------------------------------------------------------
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
driver.implicitly_wait(20)

article = '//*[@id="react-root"]/section/main/section/div/div[2]/div'
count = j = 0
while True:
    count += 1
    j +=1
    if count == 8:
        count = 1
    print(str(j), " - " ,str(count)) # Displaying on the console -----------------------------------------

    try:
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, article + '/article[{}]'.format(count)))
        )
    except:
        print("Couldn't load Page...")

    # Getting text of an Insta. post... -------------------------------------------------------------------
    element = driver.find_elements_by_xpath(article + '/article[{}]'.format(count))
    for i in element:
        print(i.text)
    print('\n\n')
    driver.implicitly_wait(2)

    # Scrolling page for the height of the screen ---------------------------------------------------------
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
