def modular_inverse(a, P):

	if(findGCD(a, P)==1):
		return exp_mod(a, P-2, P)
	else:
		return -1

def exp_mod(a, b, m):
	

	remaining=b
	mod=1
	while(remaining>0):

		iters, done_upto=max_power_of_two_upto(remaining)

		loop_mod=a%m
		for i in range(iters):
			loop_mod=(loop_mod*loop_mod)%m

		mod=(mod*loop_mod)%m
		remaining=remaining - done_upto

	return mod

def max_power_of_two_upto(num):

	if(num>=1):
		ans=0
		comparator=1
		while(comparator<=num):
			comparator=comparator*2
			ans=ans+1

		return (ans-1, int(comparator/2))

	else:
		return -1

def findGCD(a, b):
	if(a>b):
		return EuclideanGCD(a, b)

	else:
		return EuclideanGCD(b, a)

def EuclideanGCD(a, b):

	if(b==0):
		return a

	else:
		return EuclideanGCD(b, a%b)

#TEST
#print(modular_inverse(89342893493428, 1000000007))