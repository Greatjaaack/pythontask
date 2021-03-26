'''
Получить с русской википедии список всех животных (Категория:Животные по алфавиту) и вывести количество животных на каждую
букву алфавита. Результат должен получиться в следующем виде:
А: 642
Б: 412
В:....

### Реализация через класс ###
'''

import requests
from bs4 import BeautifulSoup
from collections import defaultdict


class NumberOfAnimals:
    number_of_animals = defaultdict(int)

    def __init__(self, url, pagin):
        '''
        url: главная ссылка
        pagin: ссылка пагинации (добавляется к главной ссылке)
        number_of_animals: словарь для хранения животных и количества
        '''
        self.url = url
        self.pagin = pagin
        self.number_of_animals = NumberOfAnimals.number_of_animals

    def open_next_page(self, pagin):
        '''открытие страницы и поиск нужного блока с перечислением животных'''
        self.res = requests.get(url + pagin[0])
        del pagin[0]
        if self.res.status_code == 200:
            self.soup = BeautifulSoup(self.res.text, "html.parser")
            self.animal_category = self.soup.find_all('div', class_='mw-category-group')
            return self.soup, self.animal_category

    def add_num_animals(self, animal_category):
        '''формирование словаря {Первая буква названия животного: Кол-во животных}'''
        for animal in animal_category:
            for _ in animal.select('li'):
                self.number_of_animals[animal.find('h3').text] += 1

    def add_pagin(self, pagin):
        '''добавляем ссылки пагинации в список, для дальнейшего перехода на следующую ссылку'''
        current_pagin = self.soup.find('div', id='mw-pages').find_all('a')
        for link in current_pagin:
            if link.text == "Следующая страница":
                if link.get('href') not in pagin:
                    pagin.append(link.get('href'))

    def print_num_animals(self, number_of_animals):
        '''вывод на экран словаря с животными и их кол-вом'''
        for k, v in self.number_of_animals.items():
            print(k, ":", v)


def get_dict_of_animals(url, pagin):
    '''получение списка животных и их кол-ва'''
    animals = NumberOfAnimals(url, pagin)

    while animals.pagin:
        animals.open_next_page(animals.pagin)
        animals.add_num_animals(animals.animal_category)
        animals.add_pagin(animals.pagin)

    return animals.print_num_animals(animals.number_of_animals)

url = 'https://ru.wikipedia.org'
pagin = ['/w/index.php?title=Категория:Животные_по_алфавиту&from=А']

get_dict_of_animals(url,pagin)