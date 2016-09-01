#Lab 4

#Practise 

#401
def double_elements(list):
	return[x*2 for x in list]
	
#print (double_elements([1,3,5]))

#402
def all_pairs_ordered(n):
	position_two = [x for x in range(n+1)]

	position_one = [[y,[x for x in range(position_two)]] for y in range((n+1)*3)]
	return position_one

print(all_pairs_ordered(2))
