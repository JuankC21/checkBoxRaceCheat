#Works on local.
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path='<PATH WHERE YOU HAVE CHROMEDRIVER>')
driver.get('https://www.checkboxrace.com/')

for i in range (1,101):
    #If loop gets stuck, increase sleep time
    sleep(0.02)
    driver.find_element(By.XPATH,'/html/body/div[1]/input[{}]'.format(i)).click()
    sleep(0.03)





