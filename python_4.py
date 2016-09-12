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

def powerset(elements):

	if not elements:
		return [[]]

	tempPowerset = powerset(elements[1:])

	for n in powerset(elements[1:]):
		return tempPowerset + [[elements[0]] + n for n in powerset(elements[1:])]

#print(powerset([1,2]))

#4A with comments

# def powerset(count, elements):
# 	print("")
# 	count += 1
# 	print("count 1 = " + str(count))

# 	if not elements:
# 		return [[]]
	
# 	print("elements = "+ str(elements))	
# 	print("elements[0] = "+ str(elements[0]))
# 	print("elements[1:] = " + str(elements[1:]))

# 	tempPowerset = powerset(count, elements[1:])
# 	print("tempPowerset = " + str(tempPowerset))
# 	print("count 2 = " + str(count))
# 	result = []
# 	print("elements = "+ str(elements))	
	
# 	for n in powerset(count, elements[1:]):
# 		print("loop:")
# 		print("elements = "+ str(elements))	
# 		print("elements[1:] = " + str(elements[1:]))
# 		print("[elements[0]] + n = "+ str([elements[0]]) + " + "+ str(n))
# 		result.append([elements[0]] + n)
# 		print("result = " + str(result))
		

# 	print("tempPowerset + result = " + str(tempPowerset) + " + " + str(result))
# 	return tempPowerset + result
#print(powerset(0, [1, 2]))

#405

def create_lock(code, message):
	def lock(n):
		if n == code:
			return message
		else:
			return "Fel kod!"
	return lock

#my_lock = create_lock(42, "Yeaaah!")

#print(my_lock(42))
#406
#print((lambda x: x*2)(3))
#407
#print((lambda x,y: x**2 + y**2)(2,3))
#408
#print((lambda x: (lambda y: y + x ))(5)(2))

####
#4B#
####

def generate_height(h0, v0, t0, a):
	return lambda t: h0 + v0*(t - t0) + 0.5*a*(t - t0)**2

#h_fas_ett = generate_height(0,0,0,290)
#print(h_fas_ett(5))


#409
def keep_if(function, data):
	res = ""
	for i in data:
		if function(i):
			res += i
	return res

#print(keep_if(lambda bokstav: False, 'Vimes'))

#410
def foreach(function, list):
	return [function(x) for x in list]

#print(foreach(lambda x: x**3, [0, 1, 2, 3]))

#411
def compose(f):
	return lambda x: f(f(x))

def f(x): return x + 10
def g(y): return 2 * y + 7
#h = compose(f,g)
#print(h(2))

#412
def repeat(func, n):
	for i in range(n):
		 return compose(func(x))
	
		
	#return lambda x: compose(func(x))

square_thrice = repeat(lambda x: x**2 , 3)

print(square_thrice(3))