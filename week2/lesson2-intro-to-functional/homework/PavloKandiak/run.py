from utils.task1 import members as M
from utils.task2 import *
from utils.task3 import *
from utils.task4 import *
from utils.task5 import *
from utils.task6 import *
from utils.task7 import *

if __name__ == "__main__":
	import copy
	#task1
	print(M, '\n')

	#task2
	members = copy.deepcopy(M)
	name_uppercase(members)
	print(members, '\n')

	#task3
	members = copy.deepcopy(M)
	add_load(members)
	print(members, '\n')

	#task4
	members = copy.deepcopy(M)
	print(have_o(members), '\n')

	#task5
	members = copy.deepcopy(M)
	print(age(members),'\n')

	#task6
	members = copy.deepcopy(M)
	print(sort(members),'\n')

	#task7
	#
	x = int(input("0 < x < 4000\nInput x:"))
	print(rom_num(x))
