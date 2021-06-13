# Importing necessary libraries and tools
# -------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import csv


#define dataframe
# df = pd.DataFrame(columns=['bewertungen'])

# import pandas as pd
kliniken =  ['https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-klinik-am-zuckerberg-braunschweig']
#'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-kliniken-herzogin-elisabeth-braunschweig', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-klinik-am-zuckerberg-braunschweig'], 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-kliniken-herzogin-elisabeth-braunschweig', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-klinik-am-zuckerberg-braunschweig', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-stadtkrankenhaus-wolfsburg', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-peine', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-st-martini-duderstadt', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-henriettenstiftung-hannover', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-eilenriede-klinik-hannover', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-sophien-klinik-hannover', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-agnes-karl-krankenhaus-laatzen', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-klinikum-wahrendorff-sehnde', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-landeskrankenhaus-hildesheim', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-nienburg', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-stadtkrankenhaus-cuxhaven', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-drk-krankenhaus-seepark-debstedt-langen', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-buchholz', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-winsen', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-landeskrankenhaus-lueneburg', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-diakoniekrankenhaus-rotenburg', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-osterholz-scharmbeck', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-klinik-fallingbostel', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-rehazentrum-soltau', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-walsrode', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-buxtehude', 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-diana-klinik-physikalische-medizin-bad-bevensen']

DRIVER_PATH = '/Users/yigit/Github/chromedriver'

for k in kliniken:
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(k +'/bewertungen?allbew#more')

    driver.find_element_by_id("ez-accept-naecesary").click()

    
# Locating the xpaths and finding elements on the website
# -------------------------------------


    name = driver.find_element_by_xpath('//*[@id="content"]/header/h1')
    titels = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/header')
    daten = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/div/time')
    fachbereiche = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/span')
    berichte = driver.find_elements_by_xpath("//p[@itemprop='reviewBody']")
    gesamtListe = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/section/dl/dd[1]/img')
    qBeratung = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/section/dl/dd[2]/img')
    medBehandlung = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/section/dl/dd[3]/img')
    verwaltAbl = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/section/dl/dd[4]/img')
    # ausGestaltung = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/section/dl/dd[5]/img')


    # berichte = driver.find_elements_by_xpath('//section[@class="report"]/dl/dd/p')



# Scraping texts
# -------------------------------------

    NameKlinik = [name.text for a in titels]
    Titel = [a.text for a in titels]
    DatumBewertung = [a.text for a in daten]
    Fachbereich = [a.text for a in fachbereiche]
    Erfahrungsbericht = [a.text for a in berichte]

# Scraping attributes for review starts
# -------------------------------------

    Gesamtzufriedenheit = [a.get_attribute("class") for a in gesamtListe]
    QualitaetBeratung = [a.get_attribute("class") for a in qBeratung]
    MedizBehandlung = [a.get_attribute("class") for a in medBehandlung]
    VerwaltungAblaeufe = [a.get_attribute("class") for a in verwaltAbl]
    # AusstattungGestaltung = [a.get_attribute("class") for a in ausGestaltung]


    # print(len(QualitaetBeratung))
    



# Create the dataframe and csv
# -------------------------------------

    df = pd.DataFrame(zip(NameKlinik, Titel, DatumBewertung, Fachbereich, Erfahrungsbericht, Gesamtzufriedenheit, QualitaetBeratung, MedizBehandlung, VerwaltungAblaeufe), columns=["NameKlinik", "Titel", "DatumBewertung", "Fachbereich", "Erfahrungsbericht", "Gesamtzufriedenheit", "QualitätBeratung", "MedizBehandlung", "VerwaltungAblaeufe"])
    df.to_csv('kb.csv', index=False, encoding="utf-8")


    time.sleep(3)
    driver.quit()


















# df2 = pd.DataFrame([bewertungen],columns=['bewertungen'])
    # df = df.append(df2,ignore_index=True)
    # df.to_csv("aaa.csv",index=False)



    # bewCount = 1

    # with open("bewertungen.txt","w",encoding = "UTF-8") as file:
    #     for bewertung in bewertungen:
    #         file.write(str(bewCount) + ".\n" + bewertung + "\n")
    #         file.write("**************************\n")
    #         bewCount += 1
                    

    # elements = driver.find_elements_by_xpath('//article[@class="bewertung"]/span')
    # liste = []
    # for element in elements:
    #     liste.append(element.text)
    # print(liste)