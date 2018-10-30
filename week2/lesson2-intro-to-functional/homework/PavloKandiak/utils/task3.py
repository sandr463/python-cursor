def add_load(data: list):
	for i in data:
		l = i['age'] * 100 / 200
		i['load'] = int(l) if l.is_integer() else l