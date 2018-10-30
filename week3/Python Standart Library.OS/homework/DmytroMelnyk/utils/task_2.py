# Task 2
#
# This is a test of your googling skills :D
# Using csv module from Standard Library, create a simple csv file of your study group
# (field names would be "First name", "Last name", "Telegram tag"). You need to use csv.
# DictWriter class. All the necessary data can be found in documentation.
# To check how the file looks - open it in excel or any similar program.

import csv


def create_csv(p: str, l: list):
    """
    Using csv module from Standard Library, create a simple csv file of your study group (
    field names would be "First name", "Last name", "Telegram tag").
    You need to use csv.DictWriter class. All the necessary data can be found in documentation.
    :param p: path of file to create
    :param l: list of list
    """
    with open(p, 'w') as csvfile:
        fieldnames = ["First name", "Last name", "Telegram tag"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list(map(lambda x: dict(zip(fieldnames, x)), l)))
        print("writing complete")
        print(f'Your csv file {p}')


if __name__ == '__main__':
    grouplistnames = [['Alexandr', 'Klimach', '@klimach'],
                      ['Alexander', 'Kozhokar', '@hey_alex'],
                      ['Viktor', 'B.', '@sancheezzz'],
                      ['Anton', 'Ivanov', None],
                      ['Roman', 'Rodomansky', '@romanrodomansky'],
                      ['Pavlo', 'Kandiak', '@kandiak_ps'],
                      ['Eugene', 'Zabolotny', '@eugenezabolotny'],
                      ['Дмитро', 'Bragarnik', '@Sarbai'],
                      ['Eugene', 'Semanyshyn', None],
                      ['Anton', 'Dotsenko', None],
                      ['Ruslan', 'Karelov', None],
                      ['Ostap', 'Rodomansky', '@ostap_rodomansky'],
                      ['Igor', 'Tagintsev', '@Ingvar1390'],
                      ['Maxim', 'Poleshko', '@Maxsim_P'],
                      ['Misha', 'Antonkin', '@Cosmander'],
                      ['Андрій', 'Станішевський', '@xlibchyk'],
                      ['Olga', 'Tregub', None],
                      ['Roman', 'Zhovna', None],
                      ['Yevheniia', 'Kyryliuk', '@EvgeniaCURSOR'],
                      ['Roman', 'Buryy', None],
                      ['Almost wise', 'Dragon', '@AlmostWise'],
                      ['Natali', 'Maslova', None],
                      ['Andrii', 'Homeniuk', '@AlmostWise'],
                      ['Arthur', 'Veres', '@Artooi'],
                      ['Dmytro', 'Melnyk', '@Ekut_v'],
                      ['Albert', 'Li', None],
                      ['Bohdan', 'Novakivskyy', '@AlmostWise'],
                      ['Igor', None, '@siriusnlo'],
                      ['Anna', None, None],
                      ['Igorosha', 'Prorochuk', None],
                      ['Jenia', 'Trofimenko', '@jeniaTrofimenko'],
                      ['Alina', 'Brygas', None],
                      ['Eugen', None, None]]

    path = '/mnt/48D443B7D443A5D2/Users/Melnyk.D/OneDrive/Python_Projects_education/python-cursor/week3/Python ' \
           'Standart Library.OS/homework/DmytroMelnyk/utils/batman.csv'

    create_csv(path, grouplistnames)
