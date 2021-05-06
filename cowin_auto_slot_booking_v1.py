#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from win32com.client import Dispatch
import time
speak = Dispatch("SAPI.SpVoice").Speak
driver = webdriver.Chrome(input("Enter the chromedriver.exe path, For example enter like this: 'F:\cowin\chromedriver_win32\chromedriver.exe' :"))
driver.get("https://selfregistration.cowin.gov.in/")
mobile_number = input("Enter your mobile number : ")
age = input('Enter your age(45 or 18) :')
pincode = input('Enter your area Pincode :')
if age == '18':
    age_key = '1' 
else:
    age_key = '3'
vaccine_num = input("Enter the specific vaccine you want: \n Enter '1' for COVISHIELD or '2' for COVAXIN or '3' for Any vaccine :")
if vaccine_num == '1':
    vaccine = 'COVISHIELD'
elif vaccine_num == '2':
    vaccine = 'COVAXIN'
elif vaccine_num == '3':
    vaccine = ('COVISHIELD' or 'COVAXIN')
mobile_number_enter = driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(mobile_number)

driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(input('Enter the received OTP within 180s :'))

driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[3]').click()

time.sleep(3)

driver.find_element_by_link_text('Schedule').click()

driver.find_element_by_xpath('//*[@id="main-content"]/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[4]/ion-col/div/div[2]/div').click()

time.sleep(1)

driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[2]/mat-form-field/div/div[1]/div/input').send_keys(pincode)

driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[3]/ion-button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="flexRadioDefault'+age_key+'"]').click()
time.sleep(1)
while_condition = True
i = 1
while while_condition :
    driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[3]/ion-button').click()
    time.sleep(1)
    tags = driver.find_elements_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[8]/div/div/mat-selection-list/div/mat-list-option/div/div[2]/ion-row/ion-col[2]/ul/li[2]')
    for tag in tags:
        booking_status = tag.text.split('\n')
        try:
            if vaccine_num == '1':
                if (booking_status[0]!='Booked' and booking_status[1]== 'COVISHIELD' and  booking_status[2]=='Age '+age+'+'):
                    tags[0].click()
                    time.sleep(1)
                    while_condition = False
                    break
            elif vaccine_num == '2':
                if (booking_status[0]!='Booked' and booking_status[1]== 'COVAXIN' and  booking_status[2]=='Age '+age+'+'):
                    tags[0].click()
                    time.sleep(1)
                    while_condition = False
                    break
            elif vaccine_num == '3':
                if (booking_status[0]!='Booked' and booking_status[2]=='Age '+age+'+'):
                    tags[0].click()
                    time.sleep(1)
                    while_condition = False
                    break
        except:
            pass
driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/div/ion-button[1]').click()

driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row[3]/ion-col/div/ion-button').click()
speak('Vaccine Booked successfully!')
print('Thanks for using!')


# In[ ]:




