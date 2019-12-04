from my_modules.leftListShift import leftListShift

def leftTupShift(tup, rotations):
	temp = list(tup)
	shifted = leftListShift(temp, rotations)
	result = tuple(shifted)
	return result

if __name__ == "__main__":
	tup = (1,2,3,4,5)
	print(leftTupShift(tup, 1))
	print(leftTupShift(tup, 2))
	print(leftTupShift(tup, 3))
	print(leftTupShift(tup, 4))
	print(leftTupShift(tup, 5))
	print(leftTupShift(tup, 6))
	print(leftTupShift(tup, 7))
