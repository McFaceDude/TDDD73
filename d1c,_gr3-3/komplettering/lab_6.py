#Tddd73 Lab 6 Algoritmer
#Samuel Lindgren samli627 

"""
6A
"""
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

import unittest #For the tests

def match(seq, pattern):
  """
  Match a seq to a pattern. Return True if match, otherwise, return False.
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
  
  #This elif is added to the code given by the lab.
  #If the first element of the seq is a list, 
  #match it with the fist element of the pattern.
  elif isinstance(seq[0], list):
    return match(seq[0], pattern[0])

  else:
    return False
  
def search(pattern, db):
  """
  Match a pattern to a db. Return the books (in a list) that match the 
  pattern. If no books match, return an empty list.
  """
  matched_books = []
  for book in db:
    if match(book, pattern):
      matched_books.append(book)
    
  return matched_books
