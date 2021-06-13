from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import pandas as pd

DRIVER_PATH = '/Users/yigit/Github/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.google.de/')
driver.find_element_by_id('L2AGLb').click()    
searchArea = driver.find_element_by_css_selector(".gLFyf.gsfi")
searchArea.send_keys('deneme')
searchArea.send_keys(Keys.RETURN)

# scroll
jscommand = """
rezensionen = document.querySelector(".main");
rezensionen.scrollTo(0, rezensionen.scrollHeight);
var lenOfPage=rezensionen.scrollHeight;
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



Krankenhaeuser = ['Herzogin Elisabeth Hospital']
# ['Herzogin Elisabeth Hospital', 'Klinik am Zuckerberg','Klinikum Wolfsburg','Klinikum Peine,St. Martini Krankenhaus','DIAKOVERE Henriettenstift','Eilenriede Klinik Hannover','Sophienklinik','KRH Klinikum Agness Karll Laatzen','Klinikum Wahrendorff','AMEOS Klinikum Hildesheim','Helios Kliniken Mittelweser','HELIOS Klinik Cuxhaven','AMEOS Klinikum Seepark Geestland','Krankenhaus Buchholz','Krankenhaus Winsen','Psychiatrische Klinik Lüneburg','Agaplesion - Diakonieklinikum Rotenburg','Kreiskrankenhaus Osterholz','Klinik Fallingbostel','MediClin Klinikum Soltau','Krankenhaus Walsrode','Elbe Klinikum Buxtehude','Diana Kliniken']


# for k in range(len(Krankenhaeuser)):
#     driver = webdriver.Chrome(executable_path=DRIVER_PATH)
#     driver.get('https://www.google.de/')
#     driver.find_element_by_id('L2AGLb').click()    
#     searchArea = driver.find_element_by_css_selector(".gLFyf.gsfi")
#     searchArea.send_keys(Krankenhaeuser[k])
#     searchArea.send_keys(Keys.RETURN)
#     link = driver.find_element_by_css_selector(".hqzQac")
#     link.click()
#     deneme = driver.find_elements_by_class_name('.VFlF2c.review-dialog')
    
#     time.sleep(3)
#     #scroll
#     jscommand = """
#     rezensionen = document.querySelector(".VFlF2c.review-dialog");
#     rezensionen.scrollTo(0, rezensionen.scrollHeight);
#     var lenOfPage=rezensionen.scrollHeight;
#     return lenOfPage;
#     """
#     lenOfPage = driver.execute_script(jscommand)
#     match=False
#     while(match==False):
#         lastCount = lenOfPage
#         time.sleep(1)
#         lenOfPage = driver.execute_script(jscommand)
#         if lastCount == lenOfPage:
#             match=True
#     time.sleep(5)



    # bewertungs = driver.find_elements_by_class_name('review-snippet')
    # for b in bewertungs:
    #     print(b.text)



driver.close()









# driver.close()




# links = [elem.get_attribute('href') for elem in elems]
# link = driver.find_element_by_xpath("//html/body/div[7]/div/div[9]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/span[2]/span")

# deneme = driver.find_element_by_xpath("//span[@class='hqzQac']/a").get_attribute('href')
# reviewsButton = driver.find_elements_by_css_selector("span.hqzQac > span > a")
# clickButton = cssSelector.find_element_by_tag_name('a').
# link.click()
# searchArea = driver.find_element_by_xpath("//*[@id='searchboxinput']")
# searchButton = driver.find_element_by_xpath("//*[@id='searchbox-searchbutton']")

# searchArea.send_keys(hospitalName)
# driver.find_elements_by_css_selector(".pR49Ae.gsfi").send_keys(Keys.RETURN)

# searchButton.click()







# widget-pane-link



# krankenheuser = ['klinik-carolabad-chemnitz', 'klinikum-fuerth', 'krankenhaus-aschersleben']
# for i in krankenheuser:
#   url = 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-'+i
#   driver.get(url)
#   bewertungen = driver.find_elements_by_xpath('//article[@class="bewertung"]')

#   bewertungen_list = []
#   for b in range(len(bewertungen)):
#     bewertungen_list.append(bewertungen[b].text)

# print(len(bewertungen_list))
# print(bewertungen_list)










# bewertungen = driver.find_elements_by_xpath('//article[@class="bewertung"]')

# bewertungen_list = []
# for p in range(len(bewertungen)):
#     bewertungen_list.append(bewertungen[p].text)

