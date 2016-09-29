#5A





# ----------------------------------------------------------------------------
#  Grammar for the Calc language
# ----------------------------------------------------------------------------

"""

PROGRAM    ::= [ 'calc', STATEMENTS ]

STATEMENTS ::= STATEMENT
               | STATEMENT, STATEMENTS
			   
STATEMENT  ::= ASSIGNMENT
               | REPETITION
               | SELECTION
               | INPUT
               | OUTPUT
			  
ASSIGNMENT ::= [ 'set', VARIABLE, EXPRESSION ]

REPETITION ::= [ 'while', CONDITION, STATEMENTS ]

SELECTION  ::= [ 'if', CONDITION, STATEMENT ]
               | [ 'if', CONDITION, STATEMENT, STATEMENT ]
			   
INPUT      ::= [ 'read', VARIABLE ]

OUTPUT     ::= [ 'print', VARIABLE ]

EXPRESSION ::= CONSTANT
               | VARIABLE
               | BINARYEXPR
			   
BINARYEXPR ::= [ EXPRESSION, BINARYOPER, EXPRESSION ]
			   
CONDITION  ::= [ EXPRESSION, CONDOPER, EXPRESSION ]

BINARYOPER ::= '+' | '-' | '*' | '/'

CONDOPER   ::= '<' | '>' | '='
			  
VARIABEL   ::= a Python string

KONSTANT   ::= a Python number

"""

# ----------------------------------------------------------------------------
#  Primitive functions for the Calc language constructs
# ----------------------------------------------------------------------------

# ----- PROGRAM -----

def isprogram(p):
    return isinstance(p, list) and len(p) > 1 and p[0] == 'calc'

def program_statements(p):
    return p[1:]

# ----- STATEMENTS -----

def isstatements(p):
    isstmnt = lambda s: isassignment(s) or isrepetition(s) or isselection(s) \
                        or isoutput(s) or isinput(s)
    return isinstance(p, list) and p and all(map(isstmnt, p))

def first_statement(p):
    return p[0]

def rest_statements(p):
    return p[1:]

def empty_statements(p):
    return not p

# ----- STATEMENT -----

# No functions for statements in general. Instead, see the differenct
# types of statements: assignments, repetitions, selections, input
# and output.

# ----- ASSIGNMENT -----

def isassignment(p):
    return isinstance(p, list) and len(p) == 3 and p[0] == 'set'

def assignment_variable(p):
    return p[1]

def assignment_expression(p):
    return p[2]

# ----- REPETITION -----

def isrepetition(p):
    return isinstance(p, list) and len(p) > 2 and p[0] == 'while'

def repetition_condition(p):
    return p[1]

def repetition_statements(p):
    return p[2:]

# ----- SELECTION -----

def isselection(p):
    return isinstance(p, list) and (3 <= len(p) <= 4) and p[0] == 'if'

def selection_condition(p):
    return p[1]

def selection_true(p):
    return p[2]

def hasfalse(p):
	return len(p) == 4
	
def selection_false(p):
    return p[3]

# ----- INPUT -----

def isinput(p):
    return isinstance(p, list) and len(p) == 2 and p[0] == 'read'

def input_variable(p):
    return p[1]

# ----- OUTPUT -----

def isoutput(p):
    return isinstance(p, list) and len(p) == 2 and p[0] == 'print'

def output_variable(p):
    return p[1]

# ----- EXPRESSION -----

# No functions for expressions in general. Instead, see the differenct
# types of expressions: constants, variables and binary expressions.

# ----- BINARYEXPR -----

def isbinary(p):
    return isinstance(p, list) and len(p) == 3 and isbinaryoper(p[1])

def binary_operator(p):
    return p[1]

def binary_left(p):
    return p[0]

def binary_right(p):
    return p[2]

# ----- CONDITION -----

def iscondition(p):
    return isinstance(p, list) and len(p) == 3 and iscondoper(p[1])

def condition_operator(p):
    return p[1]

def condition_left(p):
    return p[0]

def condition_right(p):
    return p[2]

# ----- BINARYOPER -----

def isbinaryoper(p):
    return p in ['+', '-', '*', '/']

# ----- CONDOPER -----

def iscondoper(p):
    return p in ['<', '>', '=']

# ----- VARIABLE -----

def isvariable(p):
    return isinstance(p, str) and p

# ----- CONSTANT -----

def isconstant(p):
    return isinstance(p, int) or isinstance(p, float)

"""
-------------------------------------------------------------------------------------------------------
"""

import copy

def eval_program(program, *opt_arg):
	variables = {}
	
	if opt_arg:
		variables = copy.deepcopy(opt_arg[0])

	if isprogram(program):
		for stmt in program_statements(program):
			finalOutput = check_typ(stmt, variables)
		return(variables)

def check_typ(stmt, variables):
	
		#print("")
		#print("stmt: " + str(stmt))

		if isassignment(stmt):
			print("assignment: " + str(stmt))
			if isinstance(assignment_expression(stmt), list):
				assignment(['set', assignment_variable(stmt), check_typ(assignment_expression(stmt), variables)], variables)
			else: 
				assignment(stmt, variables)	
			
		if isinput(stmt):
			print("input: " + str(stmt))
			input_func(stmt, variables)
						
		if isoutput(stmt):
			print("output: " + str(stmt))
			print("------------")
			return output(stmt, variables)
			
		if isbinary(stmt):
			print("binary: " + str(stmt))
			return binary_check(stmt, variables)

		if iscondition(stmt):
			print("condition: " + str(stmt))
			return binary_check(stmt, variables)
		if isselection(stmt):
			if hasfalse(stmt):
				print("Selsection, has false!")
			return selection(stmt, variables)

def binary_check(stmt, variables):

	if isconstant(stmt):
		return stmt

	if isvariable(stmt):
		#print("varible = " + str(variables[stmt]))
		return variables[stmt]

	if isinstance(stmt, list):
		return binary(binary_check(stmt[0], variables), stmt[1], binary_check(stmt[2], variables))
	
	print("ERROR binary_check")

def binary(left, operator, right):
	if operator == '+':
		print("add")
		return left + right	

	if operator == '-':
		print("dif " + str(left) +" - " +str(right))	
		return left - right
		

	if operator == '*':
		print("multi")
		return int(left) * int(right)

	if operator == '/':
		print("div")
		return left / rightt

	if operator == '<':
		#print("<")
		return int(left) < int(right)

	if operator == '>':
		#print(">")
		return int(left) > int(right)

	if operator == '=':
		print("equal")
		return left == right
	
	print("ERROR no binary operator")
	print(stmt)
	print("")

def selection(stmt, variables):
	if binary_check(selection_condition(stmt), variables):
		check_typ(selection_true(stmt), variables)
	elif hasfalse(stmt):
		check_typ(selection_false(stmt), variables)

def assignment(stmt, variables):
	variables[assignment_variable(stmt)] = assignment_expression(stmt)
	return assignment_expression(stmt)
	

def output(stmt, variables):
	print  (str(output_variable(stmt)) + " = " + str(variables[output_variable(stmt)]))

def input_func(stmt, variables):
	userInput = input("Enter value for " + str(stmt[1]) + ": ")
	assignment(['set', stmt[1], userInput], variables)



calc3 = ['calc', ['read', 'p1'],
                  ['set', 'p2', 47],
                  ['set', 'p3', 179],
                  ['set', 'result', [['p1', '*', 'p2'], '-', 'p3']],
                  ['print', 'result']]

calc1 = ['calc', ['set', 'a', 5], ['print', 'a']]

calc2 = ['calc', ['set', 'x', 7],
                  ['set', 'y', 12],
                  ['set', 'z', ['x', '+', 'y']],
                  ['print', 'z']]

calc4 = ['calc',
                ['read', 'x'],
                ['set', 'zero', 0],
                ['set', 'pos', 1],
                ['set', 'nonpos', -1],
 
                ['if', ['x', '>', 0],
                 	['print', 'pos'], ['print', 'nonpos']]]
   
   
eval_program(calc4)

