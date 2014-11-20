#Program < fibonacci sequance
#Author < Denis Karanja
#Date < 18-11-2014
def fibonacci(number):
	total = 0

	if number == 1 or number == 0:
		return 1
	else:
		result = fibonacci(number - 1) + fibonacci(number - 2)
		
		if result % 2 == 0:
			total = total + result
		print "\n-------", result
		return result

def evenTerm(number):
	if number % 2 == 0:
		return number


user = int(raw_input("Enter a number to get it's fibonacci sequence\n"))
print "Fibonacci %d is %d" % (user, fibonacci(user))

