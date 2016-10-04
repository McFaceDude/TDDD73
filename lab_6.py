#lab 6
#6A
import unittest

def match(seq, pattern):
	print("")
	"""
	Returns whether given sequence matches the given pattern
	"""
	if not pattern:
		return not seq

	elif not isinstance(pattern[0], list): #then it the whole part must be a "--"
		print("notList = " + str(pattern[0]))
		
		if pattern[0] == '--':
			if match(seq[1:], pattern[1:]):
				return True
			else:
				return False
				
	elif not seq:
		print("not seq")
		return False

	elif not isinstance(pattern[0][0], list):

		if pattern[0][0] == "--":
			print("pattern = --")
			if match(seq[1:], pattern[0:][1:]):
				return True

		if pattern[0][0] == '&':
			print("& match " + str(seq[0][0]))
			print("return: " + str([seq[0][1:]] + seq[1:]))
			return match([seq[0][1:]] + seq[1:], [pattern[0][1:]] + pattern[1:])

		elif seq[0][0] == pattern[0][0]:
			print("perfect match " + str(seq[0][0]))
			print("return " + str([seq[0][1:]] + seq[1:]))# + " " + str(pattern[0][1])))
			return match([seq[0][1:]] + seq[1:], [pattern[0][1:]] + pattern[1:])

	elif isinstance(pattern[0][0], list):
		print("is List: " + str(seq[0][0]))

		
		if pattern[0][0][0] == "--":
			print("in list pattern = --")
			if match([seq[0][0][0:]] + seq[1:], [pattern[0][0:]] + pattern[1:]):
				return True
			
			elif not seq:
				return False
			else:
				return match([seq[0][0][1:]] + seq[1:], [pattern[0][0:]] + pattern)

		
		elif len(pattern[0][0]) == 0:
			print("not match, to long,  return False")
			return False

		elif pattern[0][0][0] == '&':
			print("& match " + str(seq[0][0][0]))
			print("return seq: " + str([[seq[0][0][1:]]] + seq[1:]) + " pattern: " + str([[pattern[0][0][1:]]] + pattern[1:]))
			

			return match([[seq[0][0][1:]]] + seq[1:], [[pattern[0][0][1:]]] + pattern[1:])
		
		elif seq[0][0][0] == pattern[0][0][0]:
			print("perfect match " + str(seq[0][0][0]))
			
			
			if len(seq[0][0]) <= 1:
				print("return seq: " + str(seq[1:]) + " pattern: " + str(pattern[1:]))
				return match(seq[1:], pattern[1:])
			else:
				print("return seq: " + str([[seq[0][0][1:]]] + seq[1:]) + " pattern: " + str([[pattern[0][0][1:]]] + pattern[1:]))
				return match([[seq[0][0][1:]]] + seq[1:], [[pattern[0][0][1:]]] + pattern[1:])
		else:
			print("no match, wrong name, return False")
			return False
		
	
	else:
		print("else")
		return False

"""
	elif pattern[0] == '--':
		if match(seq, pattern[1:]):
			return True
		elif not seq:
			return False
		else:
			return match(seq[1:], pattern)

	elif not seq: 
		return False 

	elif pattern[0] == '&':
		return match(seq[1:], pattern[1:])

	elif seq[0] == pattern[0]:
		return match(seq[1:], pattern[1:])

	else:
		#print(seq[0])
		return False
"""

def search(pattern, db):
	#print(pattern[0])

	res = []
	if not pattern: #base case
		return []

	for bookIndex, book in enumerate(db):
	
		if match(book, pattern):
			res.append(book)
			print("res: " + str(res))
	return res
"""
class matchTests(unittest.TestCase):
	
	def testAllMatch(self):
		self.assertEqual(search(['--', "--", '--'], db), db)
"""	

db = [[['författare', ['john', 'zelle']], 
	   ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']], 
	   ['år', 2010]], 

	  [['författare', ['armen', 'asratian']], 
	   ['titel', ['diskret', 'matematik']], 
	   ['år', 2012]], 

	  [['författare', ['j', 'glenn', 'brookshear']], 
	   ['titel', ['computer', 'science', 'an', 'overview']], 
	   ['år', 2011]], 

	  [['författare', ['john', 'zelle']], 
	   ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], 
	   ['år', 2009]], 

	  [['författare', ['anders', 'haraldsson']], 
	   ['titel', ['programmering', 'i', 'lisp']], 
	   ['år', 1993]]]

#testList = [[1,[2, 5]],[3,4]]
#res = [item for sublist in testList for item in sublist]
#print("res" + str(res))

print(search([['författare', ['&', 'zelle']], ["titel", ["--", "python", "--"]], '--'], db))
"""
print(flatten([['författare', ['john', 'zelle']], 
	   ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']], 
	   ['år', 2010]]))
"""
#6B

def quicksort(seq):

	if len(seq) <= 1:
		return seq

	pivot = seq[0]
	smaller = []
	bigger= []

	for i in seq[1:]:
		if i <= pivot:
			smaller.append(i)
		else:
			bigger.append(i)

	return quicksort(smaller) + [pivot] + quicksort(bigger)
"""
class quicksortTests(unittest.TestCase):
	def testStandardList(self):
		self.assertEqual(quicksort([26, 4, 18, 27, 6, 4, 12]), [4, 4, 6, 12, 18, 26, 27])

	def testSortedList(self):
		self.assertEqual(quicksort([112, 90, 50, 3, 3, 2, 1]), [1, 2, 3, 3, 50, 90, 112])

	def testEmptyList(self):
		self.assertEqual(quicksort([]), [])
"""
"""
def main():
	unittest.main()

if __name__ == '__main__':
	main()
	"""