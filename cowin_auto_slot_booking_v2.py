#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from win32com.client import Dispatch
import datetime
import time

speak = Dispatch("SAPI.SpVoice").Speak
# driver = webdriver.Chrome(input("Enter the chromedriver.exe path, For example enter like this: 'F:\cowin\chromedriver_win32\chromedriver.exe' :"))
driver = webdriver.Chrome('F:\cowin\chromedriver_win32\chromedriver.exe')
driver.get("https://selfregistration.cowin.gov.in/")
# mobile_number = input("Enter your mobile number : ")
mobile_number = '7743821001'
# age = input('Enter your age(45 or 18) :')
age = '18'
# pincode = input('Enter your area Pincode :')
pincode = '411017'#441209
if age == '18':
    age_key = '1' 
else:
    age_key = '2'

when = '2'

# vaccine_num = input("Enter the specific vaccine you want: \n Enter '1' for COVISHIELD or '2' for COVAXIN:")
vaccine_num = '1'
if vaccine_num == '1':
    vaccine_id = '3'
elif vaccine_num == '2':
    vaccine_id = '4'

driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(mobile_number)

driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button').click()

time.sleep(5)

driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(input('Enter the received OTP within 180s :'))

driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[3]').click()
a = datetime.datetime.now()
time.sleep(5)

driver.find_element_by_link_text('Schedule').click()

driver.find_element_by_xpath('//*[@id="main-content"]/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[4]/ion-col/div/div[2]/div').click()

time.sleep(1)
# pincode
driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[2]/mat-form-field/div/div[1]/div/input').send_keys(pincode)
#search
# driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[3]/ion-button').click()
# # time.sleep(1)
# # driver.find_element_by_xpath('//*[@id="flexRadioDefault'+age_key+'"]').click()
# # age
# driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[5]/div/div['+age_key+']').click()
# if vaccine_num == '1':
#     driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[5]/div/div['+vaccine_id+']').click()
# elif vaccine_num == '2':
#     driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[5]/div/div[4]').click()
# else:
#     pass

while_condition = True
d = datetime.datetime.now()
while while_condition :
    driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[3]/ion-button').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[5]/div/div['+age_key+']').click()
    # driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[5]/div/div['+vaccine_id+']').click()
    time.sleep(0.1)
    tags = driver.find_elements_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[8]/div/div/mat-selection-list/div/mat-list-option/div/div[2]/ion-row/ion-col[2]/ul/li['+when+']')
    # print(len(tags),'tags found')
    for i,tag in enumerate(tags):
        # print(tag.text)
        booking_status = tag.text.split('\n')
        try:
            if (booking_status[0]!='Booked' and booking_status[1]== 'COVISHIELD' and  booking_status[2]=='Age '+age+'+'):
                tags[i].click()
                time.sleep(1)
                while_condition = False
                break
        except:
            pass
driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/div/ion-button[1]').click()
speak('Hurry!!! enter the Captcha')
e = datetime.datetime.now()
f = e-d
print('Total time to find the availability : ',f.seconds,'seconds',f.microseconds,'microseconds')
# driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row[3]/ion-col/div/ion-button').click()
# speak('Vaccine Booked successfully!')
print('Thanks for using!')
b = datetime.datetime.now()
c = b - a
print('Total Logged in time : ',c.seconds,'seconds',c.microseconds,'microseconds')

# In[ ]:




