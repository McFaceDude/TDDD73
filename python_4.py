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

""""
"4A"
"""
"##########"
def powerset(elements):

	if not elements:
		return [[]]

	tempPowerset = powerset(elements[1:])

	for n in powerset(elements[1:]):
		return tempPowerset + [[elements[0]] + n for n in powerset(elements[1:])]

#print(powerset([1,2]))
"##########"

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

""""
"4B"
"""
"##########"
def generate_height(h0, v0, t0, a):
	return lambda t: h0 + v0*(t - t0) + 0.5*a*(t - t0)**2

#h_fas_ett = generate_height(0,0,0,290)
#print(h_fas_ett(5))
"##########"

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
def compose(f, g):
	return lambda x: f(g(x))

def f(x): return x + 10
def g(y): return 2 * y + 7
#h = compose(f,g)
#print(h(2))

#412 
def repeat(func, n):

	if n < 1:
		return lambda x:x

	if n == 1:
		return func
	
	else:
		return  compose(func, repeat(func, n-1))

square_thrice = repeat(lambda x: x**2 , 3)
square_two = repeat(lambda x: x**2 , 2)
square_once = repeat(lambda x: x**2 , 1)

#print(square_thrice(3))
#print(square_two(3))
#print(square_once(3))

""""
"4C"
"""
"##########"
#part 1
def smooth(func):
	dx = 0.001
	return lambda x: (func(x-dx) + func(x) + func(x + dx))/3


#print(smoothed_square(10))
import math

#print(smoothed_sin)
#print(math.sin(0.456))
#print(smoothed_sin(0.456))

#part 2
def twice_smoothed_square(x):
	smoothed_square = smooth(lambda x: x**2)
	res = smooth(smoothed_square)
	res2 = smooth(res)
	return res2(x)
#print(twice_smoothed_square(10))

def twice_smoothed_sin(x):
	smoothed_sin = smooth(math.sin)
	res = smooth(smoothed_sin)
	res2= smooth(res)
	return res2(x)
#print(twice_smoothed_sin(0.456))

#part 3
def repeatedly_smoothed(func, n):
	res = repeat(smooth, n)
	return (res(func))


fivefold_smoothed_square = repeatedly_smoothed(lambda x: x**2, 2)
#print(fivefold_smoothed_square)
fivefold_smoothed_sin = repeatedly_smoothed(math.sin, 5)
#print(fivefold_smoothed_square(10))
#print(fivefold_smoothed_sin(0.456))
"##########"

""""
"4D"
"""
"#########"

#part 1

def left_subtree(tree):
    return tree[0]

def right_subtree(tree):
    return tree[2]

def is_empty_tree(tree):
    return isinstance(tree, list) and not tree


def is_leaf(tree):
    return isinstance(tree, int)


def create_tree(left_tree, key, right_tree):
    return [left_tree, key, right_tree]


def inner_node_fn(key, left_value, right_value): 
	return key + left_value

def empty_tree_fn(): 
	return 0 

def leaf_fn(key): 
	return key**2

def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
	if is_empty_tree(tree):
		return empty_tree_fn()

	if is_leaf(tree):
		return leaf_fn(tree)

	return inner_node_fn(tree[1], traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn), 
		traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn))
#print(traverse([6, 7, 8], inner_node_fn, leaf_fn, empty_tree_fn))

#part 2

def contains_key(og_key, tree):
	return traverse(tree, lambda x,y,z: y or z or x == og_key, lambda x : x == og_key, lambda: False)

#print(contains_key(2, [[], 1, 5]))

#part 3

def tree_size(tree):
	return (traverse(tree, lambda x,y,z: y + z + 1, lambda x: 1, lambda: 0))

#print(tree_size([[1, 2, []], 4, [[], 5, 6]]))

def tree_depth(tree):
	return (traverse(tree, lambda x,y,z: max(y,z) + 1, lambda x: 1, lambda: 0))

#print(tree_depth([1, 5, [10, 7, 14]]))