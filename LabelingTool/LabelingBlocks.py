import httpx
from bs4 import *

START_DAY = 1
END_DAY = 1

START_YEAR = 2015
END_YEAR = 2015

labels = list()

for year in range(START_YEAR, END_YEAR + 1):
    for day in range(START_DAY, END_DAY + 1):
        request = httpx.get(f'https://adventofcode.com/{year}/day/{day}')
        if request.is_success:
            soup = BeautifulSoup(request.text, 'html.parser')
            paragraphs = soup.find('article', recursive=True).find_all('p')
            for ul in [ul.get_text().split('\n') for ul in soup.find('article', recursive=True).find_all('ul')]:
                for li in ul:
                    if len(li.strip()) != 0:
                        paragraphs.append(li)
            index = 0
            for paragraph in paragraphs:
                print(paragraph)
                labels.append(str(year) + ',' + str(day) + ',' + str(index) + ',' + input('Label: '))
                index += 1

label_file = open('Labels.csv', 'w')
for label in labels:
    label_file.write(label + '\n')
label_file.close()
