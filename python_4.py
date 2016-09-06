#Lab 4

#Practise 

#401
def double_elements(list):
	return[x*2 for x in list]
	
#print (double_elements([1,3,5]))

#402
def all_pairs_ordered(n):
	return [[y,x ] for y in range(n+1) for x in range((n+1)) ]
	
#print(all_pairs_ordered(2))

#403
def distribute(val, element):

	return [x+[val] for x in element] 

#print(distribute('k', [['o'], [0, 1, 2], ['o','o']]))

#404

def sum_list(element):
	return [x+element[index+1] for index, x in enumerate(element[:len(element)-1])]

#print(sum_list([1,3,3,1]))

def pascal(n):
	lists = [[] for x in range(n)]
	
	lists[0].append(1)
	lists[1].append(1)
	lists[1].append(1)
	print(lists)

	for index, alist in enumerate(lists[2:],2):
		alist.append(1)
		lists[index] = alist + sum_list(lists[index-1])
		
		lists[index].append(1)
		print(lists[index])



	# lists = distribute(1, lists)
	# lists[1].append(1)
	# for i, x in enumerate(lists[2:],2):

	# 	x = [alist + sum_list(lists[index-1]) for index, alist in enumerate(lists[len(lists)-1:], 2)]
	# 	x.append(1)
	# 	print(x)
	# print("")
	# print(lists[2])
	# print(sum_list(lists[3]))

	
	print(lists)
	

pascal(1)
