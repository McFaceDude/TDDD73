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
               | expressionEXPR
			   
expressionEXPR ::= [ EXPRESSION, expressionOPER, EXPRESSION ]
			   
CONDITION  ::= [ EXPRESSION, CONDOPER, EXPRESSION ]

expressionOPER ::= '+' | '-' | '*' | '/'

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
# types of expressions: constants, variables and expression expressions.

# ----- expressionEXPR -----

def isexpression(p):
    return isinstance(p, list) and len(p) == 3 and isexpressionoper(p[1])

def expression_operator(p):
    return p[1]

def expression_left(p):
    return p[0]

def expression_right(p):
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

# ----- expressionOPER -----

def isexpressionoper(p):
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
			check_func(stmt, variables)
		return(variables)

def check_func(stmt, variables):
		if isassignment(stmt):
			if isinstance(assignment_expression(stmt), list):
				assignment(['set', assignment_variable(stmt), str(check_func(assignment_expression(stmt), variables))], variables)
			else: 
				assignment(stmt, variables)	
			
		if isinput(stmt):
			input_func(stmt, variables)
						
		if isoutput(stmt):
			return output(stmt, variables)
			
		if isexpression(stmt) or iscondition(stmt):
			return interate_expression(stmt, variables)

		if isselection(stmt):
			return selection(stmt, variables)
		
		if isrepetition(stmt):
			repetition(stmt, variables) 

def interate_expression(stmt, variables):
	if isconstant(stmt):
		return stmt

	if isvariable(stmt):
		return variables[stmt]

	if isinstance(stmt, list):
		return expression(interate_expression(stmt[0], variables), stmt[1], interate_expression(stmt[2], variables))

def expression(left, operator, right):
	if operator == '+':
		return int(left) + int(right)	

	if operator == '-':
		return int(left) - int(right)

	if operator == '*':
		return int(left) * int(right)

	if operator == '/':
		return int(left) // int(right)

	if operator == '<':
		return int(left) < int(right)

	if operator == '>':
		return int(left) > int(right)

	if operator == '=':
		return left == right

def repetition(stmt, variables):
	while interate_expression(repetition_condition(stmt), variables):
		for statement in repetition_statements(stmt):
				check_func(statement, variables)
	return variables

def selection(stmt, variables):
	if interate_expression(selection_condition(stmt), variables):
		check_func(selection_true(stmt), variables)
	elif hasfalse(stmt):
		check_func(selection_false(stmt), variables)

def assignment(stmt, variables):
	variables[assignment_variable(stmt)] = int(assignment_expression(stmt))
	return assignment_expression(stmt)
	

def output(stmt, variables):
	print  (str(output_variable(stmt)) + " = " + str(variables[output_variable(stmt)]))

def input_func(stmt, variables):
	userInput = input("Enter value for " + str(stmt[1]) + ": ")
	assignment(['set', stmt[1], userInput], variables)

#return the factorial for n
faculty = ['calc', ["read", "n"],
					["set", "res", 1],
					["while", ["n", ">", 1],
						["set", "res", ["res", "*", "n"]],
						["set", "n", ["n", "-", 1]]],
					["print", "res"]]

#if x < 4 then return 3
#else return x
math = ["calc", ["read", "x"],  
					["if", ["x", "=", 3],
						["set", "x", 2]],
					["if", ["x", "<", 3],
						["set", "x",[12, "/", [7, "-", [1, "+", 2]]]],
						["print", "x"]],
					["if", ["x", "=", 3], 
						["print", "x"]]]
   
#eval_program(math)



