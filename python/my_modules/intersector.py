def intersector(list1, list2):
	return list(set(list1).intersection(list2))

print(intersector([1,2,3,4],[3,4,5,6]))

"""
More methods:
	return list(set(list1) & set(list2))

	interlist = [value for value in list1 if value in list2]
	return interlist
"""
