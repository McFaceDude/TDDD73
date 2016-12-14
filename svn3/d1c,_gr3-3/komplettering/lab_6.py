#TDDD73 Lab 6 Algoritmer
#Samuel Lindgren samli627 

"""
6A
"""
import unittest #For the tests

def match(seq, pattern):
	"""
	Match a seq to a pattern.
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
	"""
	Loop through the books in the database and for every book, loop through the three parts of every book.
	If a bookPart matches the same part of the pattern and all three parts of a book match, the book match
	and it is added to the res list. 
	"""
	res = []
	#If no pattern, then no match
	if not pattern: 
		return []
	#Iterate over all the books in the db
	for bookIndex, book in enumerate(db): 
		matchCounter = 0

		#Iterate over the författare, titel and år parts, and see if they match.
		for partCount, bookPart in enumerate(book): 

			#"--" matches everything and will match the book part. 
			if pattern[partCount] == "--": 
				matchCounter += 1

			#If it is the year part of the database, there is no 
			#lists in lists and it can match bookPart(["år", "something"]) directly to the pattern.
			elif partCount == 2: 	

				if match(bookPart, pattern[partCount]):
					matchCounter += 1
			
			#Do a standard check and see if the patterns match.
			elif match(bookPart[1], pattern[partCount][1]): 
				matchCounter += 1
		#If all the parts of the book matches, the whole book matched.		
		if matchCounter == 3: 
			res.append(book)
	#Return the list with the books that matched.
	return res

#The database provided by the lab.
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

class searchTests(unittest.TestCase):
	"""
	Ckeck the four cases, all match, computer book, author with three names and book that does not exists.
	"""
	def testAllMatch(self):
		self.assertEqual(search(['--', "--", '--'], db), db)

	def testComputerBooks(self):
		self.assertEqual(search(['--', ['titel', ['--', 'computer', "--"]], '--'], db), 
		[[['författare', ['john', 'zelle']], 
	   	['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']], 
	   	['år', 2010]], 
	   	[['författare', ['j', 'glenn', 'brookshear']], 
	   	['titel', ['computer', 'science', 'an', 'overview']], 
	   	['år', 2011]] ])
	
	def testThreeNamesAuthor(self):
		self.assertEqual(search([["författare",["&", "&", "&"]], "--", '--'], db), 
		[[['författare', ['j', 'glenn', 'brookshear']], 
	   	['titel', ['computer', 'science', 'an', 'overview']], 
	   	['år', 2011]]])

	def testNoMatch(self):
		self.assertEqual(search(['--', ['titel', ['super', 'cool', "mega", "awesome", "book"]], '--'], db),
		[])


"""
6B
"""
def quicksort(seq):
	"""
	Take the first element as pivot and sort the rest of the list in smaller and bigger and return 
	the sorted smaller and bigger lists plus the pivot.
	"""
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

class quicksortTests(unittest.TestCase):
	"""
	Check the three cases, standard, sorted and empty.
	"""
	def testStandardList(self):
		self.assertEqual(quicksort([26, 4, 18, 27, 6, 4, 12]), [4, 4, 6, 12, 18, 26, 27])

	def testSortedList(self):
		self.assertEqual(quicksort([112, 90, 50, 3, 3, 2, 1]), [1, 2, 3, 3, 50, 90, 112])

	def testEmptyList(self):
		self.assertEqual(quicksort([]), [])


def main(): 
	unittest.main()

if __name__ == '__main__':
	main()
	