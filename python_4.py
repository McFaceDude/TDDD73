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
def pascal_line(n):
	line = [1]
	for k in range(n):
		line.append(int(line[k] * (n-k) / (k+1)))
	return line

def pascal(n):
	return [pascal_line(i) for i in range(n)]
	
#print(pascal(7))

####
#4A#
####

def powerset(count, elements):
	print("")
	count += 1
	print("count 1 = " + str(count))
	if not elements:
		return [[]]
	
	print("elements = "+ str(elements))	
	print("elements[0] = "+ str([elements[0]]))
	print("elements[1:] = " + str(elements[1:]))
	print("")

	tempPowerset = powerset(count, elements[1:])
	print("tempPowerset = " + str(tempPowerset))
	print("count 2 = " + str(count))

	return tempPowerset + [[elements[0]] + n for n in powerset(count, elements[1:])]

print(powerset(0, [1, 2, 3]))











