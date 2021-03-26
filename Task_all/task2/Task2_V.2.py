'''
Получить с русской википедии список всех животных (Категория:Животные по алфавиту) и вывести количество животных на каждую
букву алфавита. Результат должен получиться в следующем виде:
А: 642
Б: 412
В:....

### Реализация через функцию ###
'''

import requests
from bs4 import BeautifulSoup
from collections import defaultdict

url = 'https://ru.wikipedia.org'
pagin = ['/w/index.php?title=Категория:Животные_по_алфавиту&from=А']
number_of_animals = defaultdict(int)

while pagin:
        res = requests.get(url + pagin[0])
        del pagin[0]

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")
            animal_category = soup.find_all('div', class_='mw-category-group')

            for animal in animal_category:
                for _ in animal.select('li'):
                    number_of_animals[animal.find('h3').text] += 1

        current_pagin = soup.find('div', id='mw-pages').find_all('a')
        for link in current_pagin:
            if link.text == "Следующая страница":
                if link.get('href') not in pagin:
                    pagin.append(link.get('href'))

for k, v in number_of_animals.items():
    print(k, ":", v)