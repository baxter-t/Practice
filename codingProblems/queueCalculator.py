'''
customers: an array of positive integers representing the queue. 
Each integer represents a customer, and its value is the amount of 
time they require to check out.
	n: a positive integer, the number of checkout tills.

The function should return an integer, the total time required.
'''

def queue_time(customer, n) :
	if len(customer) == 0 or n == 0:
		return 0

	queue = []
	for x in customer :
		if len(queue) < n :
			queue.append(x)
		else:
			queue.sort()
			queue[0] += x

	queue.sort()
	return queue[-1]

print(queue_time([], 1))
print(queue_time([5], 1))
print(queue_time([2], 5))
print(queue_time([1,2,3,4,5], 1))
print(queue_time([1,2,3,4,5], 100))
print(queue_time([2,2,3,3,4,4], 2))