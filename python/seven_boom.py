def sevenBOOM(n):
	print(['BOOM BOOM!!!!' if str(i)[-1] == '7' and i % 7 == 0 
		else 'BOOM!' if str(i)[-1] == '7' or i % 7 == 0 
		else i 
		for i in range(0,n+1)
	])

sevenBOOM(77)
