"""
    This Script finds out the prices of two shoes
    with different color on club factory
    and tells us the best price.
"""
#!/usr/bin/python
import sys

#selenium package is used to automate web browser interaction  
from selenium import webdriver

argsLen = len(sys.argv)

if argsLen == 1:
    print("Please give the path to chrome driver.")
elif argsLen > 2:
    print("Please give the only 1 argument, that is, path to chrome driver. No other argument required.")

#setting the path for the driver   
path = str(sys.argv[1])

#path = 'C:/Users\KSHITIJ R. SANGAR\Desktop\Kshitij Projects\Python projects\chromedriver_win32\chromedriver.exe'

#there are different web browsers, so we are using chrome browser, and hence installing its driver
driver = webdriver.Chrome(path)

#the links for the website we want to scrape, that is, extract data from
links = ['https://www.clubfactory.com/amp/item-PID-5448256.html',
         'https://cutt.ly/zylaQ5A']

finalPrice = [0,0]
run = True
#using the driver to run on both the links
for i in range(len(links)):
    driver.get(links[i])
    driver.implicitly_wait(3)
    if(run):
        #using the method find_element_by_xpath for selecting the gender pop-up
        driver.find_element_by_xpath('//*[@id="genderSelectNotification"]/div/div/div[1]/amp-img/img').click()
    run = False
    #getting the price of the shoe
    Price = driver.find_element_by_xpath('//*[@id="product"]/div[3]/div/div/span').text
    finalPrice[i] = int(Price[2:])
driver.quit()

#comparing the prices
if finalPrice[0] < finalPrice[1]:
    print("\n\n Best Price : ", finalPrice[0], "\n Website = ", links[0],"\n\n")
elif finalPrice[0] > finalPrice[1]:
    print("\n\n Best Price : ", finalPrice[1], "\n Website = ", links[1],"\n\n") 
else:
    #if same  price
    print("\n\n Both Sites have same prize : ", finalPrice[0], "\n\n")
    
