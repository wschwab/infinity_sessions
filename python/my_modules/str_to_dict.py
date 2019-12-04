def str_to_dict(stringy):
	char_dict = {char : stringy.count(char) for char in stringy}
	return char_dict

if __name__ == "__main__":
	print(str_to_dict("It was the best of times, it was the worst of times."))
