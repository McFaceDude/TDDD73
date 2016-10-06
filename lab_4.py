#TDDD73 Lab 4 Funktionell programmering
#Samuel Lindgren samli627 

"""
4A
"""
def powerset(elements):
	"""
	Return the powerset of a list of elements
	
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
	
	#Iterate through the elements in the list and use the temp functioncall plus a 
	#second loop to generate the powerset.
	for n in powerset(elements[1:]):
		return tempPowerset + [[elements[0]] + n for n in powerset(elements[1:])]

"""
4B
"""
def generate_height(h0, v0, t0, a):
	"""
	Generate a function to calculate the height with t as a unknown variable.
	"""
	return lambda t: h0 + v0*(t - t0) + 0.5*a*(t - t0)**2

"""
4C
"""
#Part 1
def smooth(func):
	"""
	Take the average of the three function calls with the dx variable.
	"""
	dx = 0.001
	return lambda x: (func(x-dx) + func(x) + func(x + dx))/3

#Part 2
def twice_smoothed_square(x):
	"""
	Smooth the square fucntion,
	then smooth that function,
	then smooth that function,
	finally, apply the last function on x.
	"""
	smoothed_square = smooth(lambda x: x**2)
	once_smoothed = smooth(smoothed_square)
	twice_smoothed = smooth(once_smoothed)
	return twice_smoothed(x)

import math #Use to calculate sin 
def twice_smoothed_sin(x):
	"""
	Smooth the sin fucntion,
	then smooth that function,
	then smooth that function,
	finally, apply the last function on x.
	"""
	smoothed_sin = smooth(math.sin)
	once_smoothed = smooth(smoothed_sin)
	twice_smoothed= smooth(once_smoothed)
	return twice_smoothed(x)

#Part 3
def compose(f, g):
	"""
	Apply the function f on the function g and return the resulting function.
	"""
	return lambda x: f(g(x))

def repeat(func, n):
	"""
	Apply the function func on itself n amount of times, return the resulting fucntion
	"""
	if n < 1:
		return lambda x: x

	if n == 1:
		return func
	#Use the compose function and call it with a recursive call to repeat.
	else:
		return  compose(func, repeat(func, n-1))

def repeatedly_smoothed(func, n):
	"""
	Use the repeat function to get the smooth smoothed n times, apply that function to the input function.
	"""
	res = repeat(smooth, n)
	return (res(func))

"""
4D
"""
#Part 1
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
	"""
	Traverse the tree and and apply the inner_node_fn and leaf_fn to the inner nodes and leafs.
	"""
	if is_empty_tree(tree):
		return empty_tree_fn()

	if is_leaf(tree):
		return leaf_fn(tree)

	#If it is not empty or a leaf, it is a inner node and we apply the inner_node_fn with a recursive 
	#call to traverse to iterate further down the branches of the inner leaf.
	return inner_node_fn(tree[1], traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn), 
		traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn))

#Part 2
def contains_key(og_key, tree):
	"""
	Call the traverse function with three lambda function;
	inner_node_fn checks if x,y or z is the og_key we are looking for,
	the leaf_fn checks if the leaf is the og_key,
	the empty_tree_fn returns False.
	"""
	return traverse(tree, lambda x,y,z: y or z or x == og_key, lambda x : x == og_key, lambda: False)

#Part 3
def tree_size(tree):
	"""
	Call the traverse function with three lambda function;
	inner_node_fn adds up the lengths of the branches,
	the leaf_fn adds 1 to the length of the branch,
	the empty_tree_fn returns 0 because it is 0 long.
	"""
	return (traverse(tree, lambda x,y,z: y + z + 1, lambda x: 1, lambda: 0))

def tree_depth(tree):
	"""
	Call the traverse function with three lambda function;
	inner_node_fn checks which branch is the longest and adds 1 for the lengt of the inner node,
	the leaf_fn adds 1 to the length of the branch,
	the empty_tree_fn returns 0 because it is 0 long.
	"""
	return (traverse(tree, lambda x,y,z: max(y,z) + 1, lambda x: 1, lambda: 0))
