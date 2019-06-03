def expanded_form(num) :
	result = []
	for x in range(len(str(num))):
		comp = num % 10 **(x + 1)
		if comp != 0 : result.append(str(comp))
		num -= comp

	result.reverse()
	return " + ".join(result)

print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))