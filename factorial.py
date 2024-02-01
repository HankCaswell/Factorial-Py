def factorial(num):
	result = 1 
	# your code here
# Handle Exception for negative numbers
	if num < 0:
		return "Factorials don't work for negative numbers"
#Handle 1 and 0 
	elif num == 1 or num == 0:
		return 1

# For Loop
	for x in range(num, 1, -1):
		result *= x	

	return result





