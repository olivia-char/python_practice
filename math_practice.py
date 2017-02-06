#multiples
#print all the odd numbers 1 to 1000
for odd_numbers in range (1, 1000, 2):
	print odd_numbers 

#print all multiples of 5 from 1 to 1000
for multiples_5 in range (0, 1000, 5):
	print multiples_5

#sum list
#prints the sum in all the values in the list
my_list = [1, 2, 5, 10, 255, 3]
count = 0
for element in my_list:
	count = count + element
	print count

#average list
#print the average of the values in the list
other_list = [1, 2, 5, 10, 255, 3]
average = 0
count = 0
for element in other_list:
	count = count + element
	average = count/len(other_list)
	print average