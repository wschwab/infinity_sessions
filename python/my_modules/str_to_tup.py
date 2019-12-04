from str_to_dict import str_to_dict
from dict_to_tup import dict_to_tup

def str_to_tup(stringy):
	dict_ = str_to_dict(stringy)
	tups = dict_to_tup(dict_)
	print(tups)
	return tups

if __name__ == "__main__":
	str_to_tup("It was the best of times, it was the worst of times.")
