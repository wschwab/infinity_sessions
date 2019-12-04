def fibo_iter(n):
	fib_list = [0,1]
	for i in range(1,n):
		fib_list.append(fib_list[-1] + fib_list[-2])
	print(fib_list)

def fibo_recurs(n, fibs=[0,1]):
	if n==1:
		print(fibs)
	else:
		fibs.append(fibs[-1] + fibs[-2])
		fibo_recurs(n-1, fibs)

n = int(input("GIMME NUMBER: "))

print("Now we'll go iterative...")
fibo_iter(n)

print("And now for the recursive...")
fibo_recurs(n)
