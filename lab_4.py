#TDDD73 Lab 4 Funktionell programmering
#Samuel Lindgren samli627 

"""
4A
"""
def powerset(elements):
	"""
	Return the powerset of a list of elements.
	
	Examples:
	>>>powerset([1,2])
	[[], [2], [1], [1, 2]]

	>>>powerset([1,2,3,4,5])
	[[], [5], [4], [4, 5], [3], [3, 5], [3, 4], [3, 4, 5], [2], [2, 5], [2, 4], 
	[2, 4, 5], [2, 3], [2, 3, 5], [2, 3, 4], [2, 3, 4, 5], [1], [1, 5], [1, 4], 
	[1, 4, 5], [1, 3], [1, 3, 5], [1, 3, 4], [1, 3, 4, 5], [1, 2], [1, 2, 5], 
	[1, 2, 4], [1, 2, 4, 5], [1, 2, 3], [1, 2, 3, 5], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
	"""
	if not elements:
		return [[]]

	#Create a temp variable of the function
	tempPowerset = powerset(elements[1:])
	
	#Iterate through the elements in the list and use the temp function call plus a 
	#second loop to generate the powerset.
	for n in powerset(elements[1:]):
		return tempPowerset + [[elements[0]] + n for n in powerset(elements[1:])]

"""
4B
"""
def generate_height(h0, v0, t0, a):
	"""
	Return a lambda function that calculates the height and takes a 
	number as argument.

	Arguments:
	h0 -- Height at time 0
	v0 -- Speed at time 0
	t0 -- Time 0
	a  -- Acceleration
	Return value:
	Lambda function that takes an int as argument.
	"""
	return lambda t: h0 + v0*(t - t0) + 0.5*a*(t - t0)**2

"""
4C
"""
#Part 1
def smooth(func):
	"""
	Return a lambda function that takes the average of three function 
	calls done by the argument func.
	"""
	DX = 0.001
	return lambda x: (func(x-DX) + func(x) + func(x + DX))/3

#Part 2
def twice_smoothed_square(x):
	"""
	Return the result of the smooth function applied to x squared twice,
	and then applied to the argument x. 

	Argument:
	x -- Number
	Return value:
	Number
	"""
	once_smoothed = smooth(lambda x: x**2)
	twice_smoothed = smooth(once_smoothed)
	return twice_smoothed(x)

import math #Use to calculate sin 
def twice_smoothed_sin(x):
	"""
	Return the result of the smooth function applied to the math 
	operation sin, twice, and then applied to the argument x. 

	Argument:
	x -- Number
	Return value:
	Number
	"""
	once_smoothed = smooth(math.sin)
	twice_smoothed = smooth(once_smoothed)
	return twice_smoothed(x)

#Part 3
def compose(f, g):
	"""
	Return a lambda function that applies one function to another 
	where the second function takes one argument as input.

	Argumnets:
	f -- Function
	g -- Function
	Return value:
	Lambda function that takes one argumnet.
	"""
	return lambda x: f(g(x))

def repeat(func, n):
	"""
	Return a lambda function that apllies a function on itself n number
	of times.

	Argumnets:
	func -- Function
	n 	 -- number
	Return value:
	Lambda function.
	"""
	if n < 1:
		return lambda x: x
	if n == 1:
		return func
	else:
		return  compose(func, repeat(func, n-1))

def repeatedly_smoothed(func, n):
	"""
	Return a lambda function that applies the function smooth to istself 
	n number of times and applies the result on a function.

	Argumnet:
	func -- Function
	n 	 -- Number
	Return value:
	Lambda function.
	"""
	res = repeat(smooth, n)
	return res(func)

"""
4D
"""
#Part 1
def left_subtree(tree):
    return tree[0]

def right_subtree(tree):
    return tree[2]

def inner_node(tree):
	return tree[1]

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
	"""
	Return the value of three functions applied to different sections of
	a list.

	Argumnets:
	tree -- List stuctured as a binary search tree.
	inner_node_fn -- Functions that is applied to inner nodes of the 
	tree.
	leaf-fn -- Function that is applied to leafs of the tree.
	empty_tree_fn -- Function that is applied to empty parts of the 
	tree.
	Return value:
	The result of the fucntions applied to the tree. 
	"""
	if is_empty_tree(tree):
		return empty_tree_fn()

	if is_leaf(tree):
		return leaf_fn(tree)

	return inner_node_fn(inner_node(tree), traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn), 
		traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn))

#Part 2
def contains_key(og_key, tree):
	"""
	Return a boolean depending on if a tree contains a value or not.

	Arguments:
	og_keey -- value
	tree -- List stuctured as a binary search tree.
	Return value:
	Boolean
	"""
	return traverse(tree, lambda x,y,z: y or z or x == og_key, lambda x : x == og_key, lambda: False)

#Part 3
def tree_size(tree):
	"""
	Return the number of inner nodes and leafs in a tree.
	
	Argument:
	tree -- List stuctured as a binary search tree.
	Return value:
	Int
	"""
	return (traverse(tree, lambda x,y,z: y + z + 1, lambda x: 1, lambda: 0))

def tree_depth(tree):
	"""
	Return the length of the longest branch of a tree from root to leaf. 
	
	Argument:
	tree -- List stuctured as a binary search tree.
	Return value:
	Int
	"""
	return (traverse(tree, lambda x,y,z: max(y,z) + 1, lambda x: 1, lambda: 0))
