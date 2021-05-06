#!/usr/bin/env python
# coding: utf-8

# In[3]:


pincode = '413102'
age = '18' #45 or 18
mobile_number = '7743821001'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from win32com.client import Dispatch
import time
# speak = Dispatch("SAPI.SpVoice").Speak
driver = webdriver.Chrome("F:\cowin\chromedriver_win32\chromedriver.exe")
driver.get("https://selfregistration.cowin.gov.in/")

mobile_number_enter = driver.find_element_by_xpath('//*[@id="mat-input-0"]')

# mobile_number.send_keys(input("Enter your mobile number : "))
mobile_number_enter.send_keys(mobile_number)

driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button').click()
time.sleep(1)

input_otp = driver.find_element_by_xpath('//*[@id="mat-input-1"]')

input_otp.send_keys(input('Input the otp :'))

driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[3]').click()
time.sleep(3)
schedule = driver.find_element_by_link_text('Schedule')

schedule.click()

driver.find_element_by_xpath('//*[@id="main-content"]/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[4]/ion-col/div/div[2]/div').click()
time.sleep(1)

pincode_search = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[2]/mat-form-field/div/div[1]/div/input')
#     //*[@id="mat-input-2"]
#     //*[@id="mat-input-4"]

#     /html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[2]/mat-form-field/div/div[1]/div/input

# pincode_search.send_keys(input('Input your pincode :'))
pincode_search.send_keys(pincode)

driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[3]/ion-button').click()

# age = input('Input age(45 or 18):')
if age == '18':
    age_key = '1' 
else:
    age_key = '3'

driver.find_element_by_xpath('//*[@id="flexRadioDefault'+age_key+'"]').click()
while_condition = True
i = 1
while while_condition :
#     print(while_condition)
#     print(i)
    driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[3]/ion-button').click()
    time.sleep(1)
    tags = driver.find_elements_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[8]/div/div/mat-selection-list/div/mat-list-option/div/div[2]/ion-row/ion-col[2]/ul/li[2]')
    for tag in tags:
        booking_status = tag.text.split('\n')
        print(booking_status)
        try:
            if (booking_status[0]!='Booked' and booking_status[1]=='COVISHIELD' and  booking_status[2]=='Age 45+'):
                tags[0].click()
                time.sleep(1)
                while_condition = False
                break
        except:
            pass
#     while_condition = 'False'
#     i=+1
        
#             for i in range(10):
#                 speak('Vaccine Found!')
driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/div/ion-button[1]').click()

driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row[3]/ion-col/div/ion-button').click()


# In[ ]:




