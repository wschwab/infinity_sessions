def make_adder(n):
	n=n
	def additive(x):
		return x + n
	return additive

if __name__ == "__main__":
	add_7 = make_adder(7)
	print(add_7(35))
