def up_name(members: list):
	return list({'age': memb['age'], 'name':memb['name'].upper()} for memb in members)