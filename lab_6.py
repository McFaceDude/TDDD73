#lab 6
#6A
import unittest


def match(seq, pattern):
	"""
	Returns whether given sequence matches the given pattern
	"""
	if not pattern:
		return not seq
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
		return False

def search(pattern, db):
	#print(pattern[0])

	res = []
	if not pattern: #no pattern to match
		return []

	for bookIndex, book in enumerate(db):
		matchCounter = 0

		for partCount, bookPart in enumerate(book):

			if pattern[partCount] == "--":
				print("partMatch1!")
				matchCounter += 1

			elif partCount == 2: 	#If we are on the year part of the database, we have no 
									#lists in lists and can match bookPart(["år", "something"]) directly.

				if match(bookPart, pattern[partCount]):
					print("partMatch2!")
					matchCounter += 1
			
			else:
			
				if match(bookPart[1], pattern[partCount][1]):
					print("match bookPart: "+ str(bookPart[1]))
					print("with pattern: " + str(pattern[partCount][1]))
					print("partMatch3!")
					matchCounter += 1
				
		if matchCounter == 3:
			print("BookMatch!")	
			res.append(book)
		else:
			print("no bookMatch!")
		
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

print(search([['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']], db))
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