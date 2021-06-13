from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv

DRIVER_PATH = '/Users/yigit/Github/chromedriver'

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'de'})

driver = webdriver.Chrome(executable_path=DRIVER_PATH,chrome_options=options)
driver.get("https://www.google.com/maps/place/Herzogin+Elisabeth+Hospital/@52.2329937,10.5267147,15z/data=!4m5!3m4!1s0x0:0x66131345a9ba3dfe!8m2!3d52.2329937!4d10.5267147")
time.sleep(10)

#bewertungen clicken
driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[21]/div/div[2]/button').click()
time.sleep(3)

#scroll
jscommand = """
berichte = document.querySelector(".section-layout.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc");
berichte.scrollTo(0, berichte.scrollHeight);
var lenOfPage=berichte.scrollHeight;
return lenOfPage;
"""
lenOfPage = driver.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = driver.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

#mehr button click
loads = driver.find_elements_by_css_selector('.ODSEW-KoToPc-ShBeI.gXqMYb-hSRGPd')
for load in loads:
    load.click()
time.sleep(4)    


#kommentar auswählen
i=1
elements = driver.find_elements_by_css_selector('.ODSEW-ShBeI.NIyLF-haAclf.gm2-body-2')
try:
    #csv speichern
    with open('kommentar.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow('        '+'Result')
        for element in elements:
            writer.writerow(element.text) 
            i+=1
except Exception:
    print('KEINE')   
print('i = ',i)     

driver.quit()