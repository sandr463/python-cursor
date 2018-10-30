def sort(data: list):
	s = sorted(data, key = lambda x : x['age'])
	return sorted(s, key = lambda x : len(x['name']))