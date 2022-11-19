import os
import openai
from dotenv import load_dotenv

import httpx
from bs4 import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# load the .env to get the OpenAI API key
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


# OpenAI Codex
def get_code(description):
    response = openai.Completion.create(
        engine='code-davinci-001',
        prompt='"""\n' + description + '\n"""\n\n',
        temperature=0.2,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print('Codex Done')
    if 'choices' in response:
        x = response['choices']
        if len(x) > 0:
            return x[0]['text']
        else:
            return ''
    else:
        return ''


# -------------------------------------------------------------------------
#                              The real Larry
# -------------------------------------------------------------------------

# defining some parameters
YEAR = 2022
DAY = 13

# first part is to get today's puzzle

# aoc_request = httpx.get(f'https://adventofcode.com/{YEAR}/day/{DAY}')
aoc_request = httpx.get('http://localhost:8000')
raw_html = ''
if aoc_request.is_success:
    raw_html = aoc_request.text
# puzzle_input = httpx.get(f'https://adventofcode.com/{YEAR}/day/{DAY}/input')

input_request = httpx.get('http://localhost:8000/input')
input_data = ''
if input_request.is_success:
    input_data = input_request.text
input_file = open('input.txt', 'w')
input_file.write(input_data)
input_file.close()

soup = BeautifulSoup(raw_html, 'html.parser')
raw_puzzle = soup.find('article', recursive=True)
puzzle_desc_list = list(map(lambda c: c.get_text(), raw_puzzle.findChildren()))
i = 0
while i < len(puzzle_desc_list):
    if puzzle_desc_list[i].strip() == "":
        puzzle_desc_list.pop(i)
    else:
        i += 1
for d in puzzle_desc_list:
    print(d)

exit()

# Response = get_code(raw_puzzle)
Response = get_code(
    '' + '\n' +
    'A transparent paper is marked with random dots and includes instructions on how to fold it up.' + '\n' +
    'The input is a list of random dots like X,Y' + '\n' +
    'Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines)' + '\n' +
    'Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.' + '\n' +
    'Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.' + '\n' +
    'Compute the number of visible dots after the first fold'
)
PythonFile = open('FinalScript.py', 'w')
PythonFile.write(Response)
PythonFile.close()

print('final script generated')
x = input()
os.system('python FinalScript.py')
