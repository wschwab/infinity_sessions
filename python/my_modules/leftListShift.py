def leftListShift(list_, rotations):
	if rotations >= len(list_):
		rotations %= len(list_)
	temp=list_[rotations:]
	temp.extend(list_[:rotations])
	return temp

if __name__ == "__main__":
	print(leftListShift([1,2,3,4,5], 1))
	print(leftListShift([1,2,3,4,5], 2))
	print(leftListShift([1,2,3,4,5], 3))
	print(leftListShift([1,2,3,4,5], 4))
	print(leftListShift([1,2,3,4,5], 5))
	print(leftListShift([1,2,3,4,5], 6))
	print(leftListShift([1,2,3,4,5], 7))
	print(leftListShift([1,2,3,4,5], 8))
