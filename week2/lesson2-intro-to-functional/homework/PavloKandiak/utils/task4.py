from re import search

def have_o(data: list):
	return list(filter(lambda x: search(r'o',x['name']), data))