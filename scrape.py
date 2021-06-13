from bs4 import BeautifulSoup
import requests
import csv
url = 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-klinik-am-zuckerberg-braunschweig'
source = requests.get(url +'/bewertungen?allbew#more').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Titel', 'Datum', 'Fachbereich', 'Erfahrungsbericht'])

for article in soup.find_all('article'):
    titels = article.header.text
    print(titels)

    # summary = article.find('div', class_='entry-content').p.text
    # print(summary)

    # try:
    #     vid_src = article.find('iframe', class_='youtube-player')['src']

    #     vid_id = vid_src.split('/')[4]
    #     vid_id = vid_id.split('?')[0]

    #     yt_link = f'https://youtube.com/watch?v={vid_id}'
    # except Exception as e:
    #     yt_link = None

    # print(yt_link)

    print()

    csv_writer.writerow([titels])

csv_file.close()


# datum = article.find('meta')['content']


