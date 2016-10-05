#lab 6 samli627
##########
#6A
##########
import unittest


def match(seq, pattern):
	
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

	res = []
	if not pattern: #no pattern to match
		return []

	for bookIndex, book in enumerate(db): #We iterate over all the books in the db
		matchCounter = 0

		for partCount, bookPart in enumerate(book): #Iterate over the författare, titel and år parts, and see if they match

			if pattern[partCount] == "--": #Matches everything
				matchCounter += 1

			elif partCount == 2: 	#If we are on the year part of the database, we have no 
									#lists in lists and can match bookPart(["år", "something"]) directly.

				if match(bookPart, pattern[partCount]):
					matchCounter += 1
			
			elif match(bookPart[1], pattern[partCount][1]): #Do a standard check and see if the patterns match
				matchCounter += 1
				
		if matchCounter == 3: #If all the parts of the book matches, the whole book matched.
			res.append(book)

	return res

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

class searchTests(unittest.TestCase): # 4 tests for search.
	
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


##########
#6B
##########
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

class quicksortTests(unittest.TestCase):# 3 tests fpr quicksort.
	def testStandardList(self):
		self.assertEqual(quicksort([26, 4, 18, 27, 6, 4, 12]), [4, 4, 6, 12, 18, 26, 27])

	def testSortedList(self):
		self.assertEqual(quicksort([112, 90, 50, 3, 3, 2, 1]), [1, 2, 3, 3, 50, 90, 112])

	def testEmptyList(self):
		self.assertEqual(quicksort([]), [])


def main(): #7 tests in total 
	unittest.main()

if __name__ == '__main__':
	main()
	