from functools import reduce 

def age(data:list):
	s = sum([i['age'] for i in data])
	mx = reduce(lambda x, y: x if x['age'] > y['age'] else y, data)
	mn = reduce(lambda x, y: x if x['age'] < y['age'] else y, data)
	return s, mn, mx