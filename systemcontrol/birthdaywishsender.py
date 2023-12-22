from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime


def wish(date,timetowish,contact,message):
    timenow=datetime.now()
    wishtime=(datetime.strptime(date, "%Y-%m-%d").replace(hour=int(timetowish.split(":")[0]), minute=int(timetowish.split(":")[1]),
                                                    second=0))
    options = webdriver.ChromeOptions()
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome.get("https://web.whatsapp.com")
    time.sleep(200)

    phone=("+91"+contact)
    chrome.get(f"https://web.whatsapp.com/phone={phone}")#&text=Hello

    while(True):
        if(timenow>wishtime):
            try:
                textbox=chrome.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                textbox.send_keys(message)
                send=chrome.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
                send.click()
            except Exception as ex:
                print(ex)


# wish("2023-12-22","00:00")