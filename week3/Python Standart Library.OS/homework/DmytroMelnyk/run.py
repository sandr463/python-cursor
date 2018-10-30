import os
import csv
import requests
from pprint import pprint
from utils.task_1 import treefiles
from utils.task_2 import create_csv
from utils.task_3 import dowlnoad_from_url

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


print('Task_1')
user_path = '/mnt/48D443B7D443A5D2/Users/Melnyk.D/OneDrive/Python_Projects_education/Cursor'
pprint(treefiles(user_path), indent=10)
print('Task_2')
path = '/mnt/48D443B7D443A5D2/Users/Melnyk.D/OneDrive/Python_Projects_education/python-cursor/week3/Python ' \
           'Standart Library.OS/homework/DmytroMelnyk/utils/batman.csv '
create_csv(path, grouplistnames)
print('Task_3')
dowlnoad_from_url('https://dummyimage.com/600x400/000/fff')


