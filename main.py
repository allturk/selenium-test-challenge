from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


chrome_driver_path=r"c:\Development\chromedriver.exe"
s=Service(executable_path=chrome_driver_path)
driver=webdriver.Chrome(service=s)
wait=WebDriverWait(driver,20)
driver.get("https://python.org")

#My Solution

#*****************************************************

# upcoming_events=wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,'.shrubbery li [href*="/events/"]')))
# events_time=wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'.shrubbery li')))
# count=0
# events={}
# testdic={}
# for time in events_time:
#     for t in time.find_elements(By.CSS_SELECTOR,"time"):
       
#         for e in time.find_elements(By.CSS_SELECTOR,'a[href*="/events/"]'):
#             testdic["time"]=t.text
#             testdic["name"]=e.text
#             events[count]={}
#             events[count].update(testdic)
#             # print(events)
#             count+=1
 

# print(events)
# *****************************************************
# for event in upcoming_events:
#     print(event.text)
# ****************************************************
# events_=driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# event_list=events_.text.split("\n")

# for i in range(int(len(event_list)/2)):
#     events[i]={}
# print(events)
# itr=0
# for i in range(int(len(event_list)/2)):
#     testdic["time"]=event_list[itr]
#     testdic["name"]=event_list[itr+1]
#     events[i].update(testdic)
#     itr+=2

# print(events)
# *******************************************************

# text=""
# events_time=driver.find_elements_by_tag_name("time")

# for item in events_time:
#     text=text+item.text+"\n"
# with open("pythonorg.txt","w",encoding="utf-8") as file:
#     file.write(text)
#************************************************************
# Angela's solution
# event_times=driver.find_elements_by_css_selector(".event-widget time")
# event_names=driver.find_elements_by_css_selector(".event-widget li a")

# improved deprecated codes
event_times=driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_names=driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
# for time in event_times:
#     print(time.text)
# for name in event_names:
#     print(name.text)
eventsdic={}

for n in range(len(event_times)):
    eventsdic[n]={
        "time":event_times[n].text,
        "name":event_names[n].text
    }
print(eventsdic)

driver.quit()