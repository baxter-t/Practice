'''
	I am the one who establishes the list so I told him: "Don't worry any more,
	I will modify the order of the list". It was decided to attribute a "weight" 
	to numbers. The weight of a number will be from now on the sum of its digits.
'''

def order_weight(strng) :
	weights = strng.split(" ")
	digWeight = []
	for weight in weights :
		w = sum([int(x) for x in weight])
		digWeight.append((w, weight))

	digWeight.sort()

	result = ""
	for weight, strn in digWeight:
		result += strn + " "

	return result[:-1]

print(order_weight("103 123 4444 99 2000"))
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))

