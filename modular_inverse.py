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

#TEST
#print(exp_mod(8976, 879349, 32489))