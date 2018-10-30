def rom_num(n: int):
	r = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
	d = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	rm = ''
	for i in range(len(r)):
		while(n >=d[i]):
			rm += r[i]
			n -= d[i]
	return rm
