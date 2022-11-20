import httpx
from bs4 import *
from tkinter import *

FIRST_YEAR_START_DAY = 1
START_DAY = 1
END_DAY = 25

START_YEAR = 2015
END_YEAR = 2021

year = START_YEAR
day = FIRST_YEAR_START_DAY
index = 0
paragraphs = list()


def reload_paragraphs():
    global paragraphs
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


def update():
    global year, day, index
    index += 1
    if index >= len(paragraphs):
        index = 0
        day += 1
        if day > END_DAY:
            year += 1
            if year > END_YEAR:
                exit()
        reload_paragraphs()


def save_label(sel_label):
    global year, day, index, paragraph_display
    file = open('Labels.csv', 'a')
    saved_label = str(year) + ',' + str(day) + ',' + str(index) + ',' + sel_label
    file.write(saved_label + '\n')
    file.close()

    update()
    paragraph_display.set(paragraphs[index])


def label_story():
    save_label('s')


def label_algorithm():
    save_label('a')


def label_story_algorithm():
    save_label('as')


def label_example():
    save_label('e')


def label_quest():
    save_label('q')


# window generation
window = Tk()
window.title('Labeling Tool')

paragraph_display = StringVar()
paragraph_display_label = Label(window, textvariable=paragraph_display, wraplength=300)

buttons = list()

buttons.extend([
    Button(window, text='Story',                command=label_story),
    Button(window, text='Algorithm',            command=label_algorithm),
    Button(window, text='Algorithm with Story', command=label_story_algorithm),
    Button(window, text='Example',              command=label_example),
    Button(window, text='Final Quest',          command=label_quest)
])

paragraph_display_label.pack()
for button in buttons:
    button.pack(side=LEFT)

reload_paragraphs()
paragraph_display.set(paragraphs[0])
window.mainloop()
