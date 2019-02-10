z=1
for i in range(5,1,-1):
	for j in range(i):
		print(end=" ")
	for j in range(6-i):
		print(z,end=" ")
		z+=1
	print()
