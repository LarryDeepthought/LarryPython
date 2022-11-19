import httpx
from bs4 import *

FIRST_YEAR_START_DAY = 1
START_DAY = 1
END_DAY = 25

START_YEAR = 2015
END_YEAR = 2021

labels = list()

for year in range(START_YEAR, END_YEAR + 1):
    for day in range(START_DAY if year != START_YEAR else FIRST_YEAR_START_DAY, END_DAY + 1):
        request = httpx.get(f'https://adventofcode.com/{year}/day/{day}')
        if request.is_success:
            soup = BeautifulSoup(request.text, 'html.parser')
            paragraphs = list()
            for paragraph in list(map(lambda p: p.get_text(), soup.find('article', recursive=True).find_all('p'))):
                for sentence in paragraph.replace('!', '.').split('.'):
                    sentence = sentence.lstrip()
                    if len(sentence) > 0:
                        paragraphs.append(sentence)
            for ul in [ul.get_text().split('\n') for ul in soup.find('article', recursive=True).find_all('ul')]:
                for li in ul:
                    if len(li.strip()) != 0:
                        paragraphs.append(li)
            index = 0
            for paragraph in paragraphs:
                print(paragraph)
                label_input = input('Label: ')
                if label_input == "SAVE":
                    label_file = open('Labels.csv', 'a')
                    for label in labels:
                        label_file.write(label + '\n')
                    label_file.close()
                labels.append(str(year) + ',' + str(day) + ',' + str(index) + ',' + label_input)
                index += 1

label_file = open('Labels.csv', 'w')
for label in labels:
    label_file.write(label + '\n')
label_file.close()
