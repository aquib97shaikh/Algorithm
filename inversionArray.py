import  random as rd
def merge(a,b):
	c =[]
	count=0
	k,j=0,0
	for i in range(len(a)+len(b)):
		kl = k>=len(b)
		jl = j>=len(a)
		if kl and jl:
			break
		if j<len(a) and (kl or a[j]<b[k] ):
			c.append(a[j])
			j=j+1
		elif jl or a[j]>=b[k]:
			c.append(b[k])
			count=count+(len(a)-j)

			k=k+1
		#print("mm")
		#print(c,count)
	return (c,count)

def mergesort(x):
	if len(x)==1:
		return x,0

	#print(x)
	a,r =  mergesort(x[:int(len(x)/2)])
	b,y =  mergesort(x[int(len(x)/2):])
	#print("b")
	#print(a,b)
	c,z= merge(a,b)
	#print(c)

	return (c,r+y+z)

ab = [i for i in range(115)]

cb,ca =mergesort(ab)
print(ca,cb)