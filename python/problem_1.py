limit = 1000
multiples_of = [3, 5]

sum = 0
for i in xrange(1,limit):
	for number in multiples_of:
		if (i % number == 0):
			sum += i
			break

print sum 
#266168
