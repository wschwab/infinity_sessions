def while_even():
	list_=[]
	i=1
	while i<=100:
		if i % 2 == 0:
			list_.append(i)
		i += 1
	print("WHILE LOOP FOR THE WIN:\n", list_)

def for_even():
	list_=[]
	for i in range(1,101):
		if i % 2 == 0:
			list_.append(i)
	print("FOR LOOP IS THE RAD BOMB:\n", list_)

while_even()
for_even()
