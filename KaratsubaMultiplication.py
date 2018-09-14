def product(x,y,n):
	
	if n==1:
		return x*y
	t = 10**(n/2)
	a,b,c,d = int(x/t),int(x%t),int(y/t),int(y%t)
	ac = product(a,c,n/2)
	bd = product(b,d,n/2)
	ab_cd = product(a+b,c+d,n/2)
	acp = ac*(10**(n))
	abcdp = (ab_cd-ac-bd)*(10**(n/2))
	return acp+abcdp+bd

	
print(product(2718281828459045235360287471352662497757247093699959574966967627,3141592653589793238462643383279502884197169399375105820974944592,64))