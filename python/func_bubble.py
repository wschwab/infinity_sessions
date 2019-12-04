def bubblesort(lst):

	def bubble(lst, _len):
		for i in range(len(lst)-2):
			if l[i] > l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
		if _len>1:
			bubble(l,_len-1)
	len_ = len(lst)
	bubble(lst, len_)

l = [6,9,4,6,2,3,8]
bubblesort(l)
print(l)
