def sorter(lst, result=[]):
	if len(lst) == 0:
		return result
	if len(result) == 0:
		result.append(lst.pop())
		print(f"Initializing results: {result}")
	else:
		n = lst.pop()
		print(f"n = {n}")
		for i in range(len(result)):
			if n <= result[i]:
				result.insert(i,n)
				print(f"In for loop, results: {result}, list: {lst}")
				print(len(lst))
				break
			elif i == len(result) -1:
				result.append(n)
				print(f"should have new max value: {result}")
	print("RECURSING")
	sorter(lst, result)

if __name__ == "__main__":
	print(sorter([5,3,9,1,3]))
