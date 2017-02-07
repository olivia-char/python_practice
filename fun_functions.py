#odd/even
#loop through 1 to 2000 print if integer is either odd or even

# def odd_even():
# 	for numbers in range (1, 2000):
# 		if numbers%2 != 0:
# 			print "Number is " + str(numbers) + "." + "This is an odd number"
# 		else:
# 			print "Number is " + str(numbers) + "."  + "This is an even number"
# odd_even()

#multiples
#loop through an array and multiply each index by 5
def multiply(array, num):
	new_array = []
	for value in array:
		x = num * value
		new_array.append(x)
	return new_array
multiply([2,4,10,16], 5)

#hacker challenge 

def layered_multiples(arr):
	new_array = []
	for value in range(0, len(arr)):	
		array2 =[]
		for value in range(0, arr[value]):
			array2.append(1)
		new_array.append(array2)
	return new_array

# print layered_multiples([2,4,6,10])
x = layered_multiples(multiply([2,4,5],3))
print x 

