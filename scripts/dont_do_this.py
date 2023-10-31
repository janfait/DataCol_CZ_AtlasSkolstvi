

import requests
from bs4 import BeautifulSoup

starting_url = 'https://www.itgymnazium.cz/en/teachers/'


def get_teachers(url):

    data = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    teacher_boxes = soup.find_all('div', class_='mt-item')
    for tb in teacher_boxes:

        name = tb.find('h3').text
        position = tb.find('h4').text

        data.append({'name': name, 'position': position})

    return data



if __name__ == '__main__':

    teachers = get_teachers(starting_url)
    print(teachers)
    