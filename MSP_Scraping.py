"""
    This Script finds out the prices of two shoes
    with different color on club factory
    and tells us the best price.
"""

from selenium import webdriver

driver = webdriver.Chrome('C:/Users\KSHITIJ R. SANGAR\Desktop\Kshitij Projects\Python projects\chromedriver_win32\chromedriver.exe')

links = ['https://www.clubfactory.com/amp/item-PID-5448256.html',
         'https://cutt.ly/zylaQ5A']
finalPrice = [0,0]
run = True
for i in range(len(links)):
    driver.get(links[i])
    driver.implicitly_wait(3)
    if(run):
        driver.find_element_by_xpath('//*[@id="genderSelectNotification"]/div/div/div[1]/amp-img/img').click()
    run = False
    Price = driver.find_element_by_xpath('//*[@id="product"]/div[3]/div/div/span').text
    finalPrice[i] = int(Price[2:])
driver.quit()

if finalPrice[0] < finalPrice[1]:
    print("\n\n Best Price : ", finalPrice[0], "\n Website = ", links[0],"\n\n")
elif finalPrice[0] > finalPrice[1]:
    print("\n\n Best Price : ", finalPrice[1], "\n Website = ", links[1],"\n\n")
    
  
else:
    print("\n\n Both Sites have same prize : ", finalPrice[0], "\n\n")
    
