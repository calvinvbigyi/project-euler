## largest prime factor of 600851475143 

## sqrt 600851475143 = 775146.099225

import math

count = 3

prime_number = []
while count < 775147:
    isprime = True
    
    for x in range(2, int(math.sqrt(count) + 1)):
        if count % x == 0: 
            isprime = False
            break
    
    if isprime:
        prime_number.append(count)    
    count += 1


for i in reversed(prime_number):
	if 600851475143 % i == 0:
		print(i)
		break