import  random as rd
def merge(a,b):
	c =[]
	k,j=0,0
	for i in range(len(a)+len(b)):
		kl = k>=len(b)
		jl = j>=len(a)
		if kl and jl:
			break
		if j<len(a) and (kl or a[j]<b[k] ):
			c.append(a[j])
			j=j+1
		elif jl or a[j]>b[k]:
			c.append(b[k])
			k=k+1
		#print(c,a,b)
	return c
def mergesort(x):
	if len(x)==1:
		return x

	#print(x)
	a =  mergesort(x[:int(len(x)/2)])
	b =  mergesort(x[int(len(x)/2):])
	#print(b)
	#print("a,b")
	c= merge(a,b)

	return c
ab = [i for i in range(10000)]
rd.shuffle(ab)
print(mergesort(ab))