def dict_to_tup(dict_):
	tup_lst = []
	for item in dict_.items():
		tup_lst.append(item)
	return tup_lst

"""
Here's a functional version which is pretty cool in my opinion:

def dict_to_tup(dict_):
	return list(map(lambda k,v : (k,v), dict_.keys(), dict_.values()))

Could use zip pretty much the same way, but it gives a tuple of tuples (not a list):

def dict_to_tup(dict_):
	return zip(dict_keys(), dict_.values())

"""
