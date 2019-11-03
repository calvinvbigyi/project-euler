sum = 0
feb = 1
feb_next = 0
feb_previous = 1

while feb_next < 4000000:	
	if feb_next % 2 == 0:
		sum += feb_next
	feb_next = feb + feb_previous
	feb_previous = feb
	feb = feb_next


print(sum)