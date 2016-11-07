#TDDD73 Lab 5 Språk
#Samuel Lindgren samli627 
#The lab instructions said to only hand in the code I wrote myself, I therefor left out the functions 
#in the calc.py file. The code will not compile now because the functions are missing. 



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
5A
"""

def expression_operator(p):
    return p[1]

def expression_left(p):
    return p[0]

def expression_right(p):
    return p[2]

import copy #Use for deepcopy
def eval_program(program, *opt_variables):
	"""
	Create the variables dict and use the opt_variables if provided.
	Iterate through the stmts in the program and check what type of statement it is.
	Return the now updated variables dict.


	"""
	variables = {}
	
	if opt_variables:
		variables = copy.deepcopy(opt_variables[0])

	if isprogram(program):
		for stmt in program_statements(program):
			check_type_of_func(stmt, variables)
		return(variables)

def check_type_of_func(stmt, variables):
	"""
	Check what type of stmt it is and call the appropriate function.
	"""
	#If the assignment is to a list, evaluate the list to know what it is,
	#send the list back to check_type_of_func.
	if isassignment(stmt):
		if isinstance(assignment_expression(stmt), list):
			assignment(['set', assignment_variable(stmt), 
				str(check_type_of_func(assignment_expression(stmt), variables))], variables)
		else: 
			assignment(stmt, variables)	
		
	if isinput(stmt):
		input_func(stmt, variables)
					
	if isoutput(stmt):
		output(stmt, variables)
	
	#Call the help function iterate_expression
	if isbinary(stmt) or iscondition(stmt):
		return iterate_expression(stmt, variables)

	if isselection(stmt):
		return selection(stmt, variables)
	
	if isrepetition(stmt):
		repetition(stmt, variables) 

def iterate_expression(stmt, variables):
	"""
	If the stmt is a list, call iterate_expression with the parts of the expression separated so that
	they can be evaluated separately. This is to allow expressions with many lists in them.
	"""
	if isconstant(stmt):
		return stmt

	if isvariable(stmt):
		return variables[stmt]

	if isinstance(stmt, list):
		return expression(iterate_expression(expression_left(stmt), variables), expression_operator(stmt), 
			iterate_expression(expression_right(stmt), variables))

def expression(left, operator, right):
	"""
	Applies the operator to the left and right variables.
	"""
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
	"""
	Call the iterate_expression to evaluate the repetition condition.
	While the condition is True, apply the check_type_of_func on the statements.
	"""
	while iterate_expression(repetition_condition(stmt), variables):
		for statement in repetition_statements(stmt):
				check_type_of_func(statement, variables)
	return variables

def selection(stmt, variables):
	"""
	Call the iterate_expression to evaluate the selection condition.
	If the condition is True, apply the check_type_of_func on the selection_true condition.
	If not True and a False stmt exists, apply the check_type_of_func on the selction_false condition.
	"""
	if iterate_expression(selection_condition(stmt), variables):
		check_type_of_func(selection_true(stmt), variables)
	elif hasfalse(stmt):
		check_type_of_func(selection_false(stmt), variables)

def assignment(stmt, variables):
	"""
	Assign the expression to the variable in the variables dict.
	"""
	variables[assignment_variable(stmt)] = int(assignment_expression(stmt))
	return assignment_expression(stmt)
	

def output(stmt, variables):
	"""
	Print the output.
	"""
	print(str(output_variable(stmt)) + " = " + str(variables[output_variable(stmt)]))

def input_func(stmt, variables):
	"""
	Get the input from the user and assign it to the variable.
	"""
	userInput = input("Enter value for " + str(assignment_variable(stmt)) + ": ")
	assignment(['set', assignment_variable(stmt), userInput], variables)


#Example programs
	
#If x is less than 4, return 3, else, return x.
math = ["calc", ["read", "x"],  
				["if", ["x", "=", 3],
					["set", "x", 2]],
				["if", ["x", "<", 3],
					["set", "x",[12, "/", [7, "-", [1, "+", 2]]]],
					["print", "x"]],
				["if", ["x", "=", 3], 
					["print", "x"]]]
#eval_program(math)

#Return the factorial for n
factorial = ['calc', ["read", "n"],
				["set", "res", 1],
				["while", ["n", ">", 1],
					["set", "res", ["res", "*", "n"]],
					["set", "n", ["n", "-", 1]]],
				["print", "res"]]
eval_program(factorial)
