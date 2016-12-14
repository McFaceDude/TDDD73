#TDDD73 Lab 5 Språk
#Samuel Lindgren samli627 

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
#Extra help functions.
def expression_operator(p):
    return p[1]

def expression_left(p):
    return p[0]

def expression_right(p):
    return p[2]

#Use for deepcopy.
import copy 
def eval_program(program, *opt_variables):
	"""
	Return the variables dictionary.
	"""
	variables = {}
	if opt_variables:
		variables = copy.deepcopy(opt_variables[0])

	if isprogram(program):
		variables = interpret_program(program_statements(program), variables)
			
	return(variables)

def interpret_program(program, variables):
	"""
	Return the updated temp_variables when there are no more stmts.
	"""
	temp_variables = copy.deepcopy(variables)
	if empty_statements(program):
		return temp_variables

	if isstatements(program):
		temp_variables = interpret_stmt(first_statement(program), 
			temp_variables)

	return interpret_program(rest_statements(program), temp_variables)
	

def interpret_stmt(stmt, variables):
	"""
	Return the updated temp_variables when the function has been applied. 
	"""
	temp_variables = copy.deepcopy(variables);
	if isconstant(stmt):
		return stmt

	if isvariable(stmt):
		return temp_variables[stmt]
	#Interpret the assignmnet_expression and assign the variable to the result.
	if isassignment(stmt):
		temp_variables[assignment_variable(stmt)] = interpret_stmt(
			assignment_expression(stmt), temp_variables);
		return temp_variables	
		
	if isinput(stmt):
		temp_variables = input_func(stmt, temp_variables)
		return temp_variables
					
	if isoutput(stmt):
		output(stmt, temp_variables)
	#Calculate the expression and return the result.
	if isbinary(stmt) or iscondition(stmt):
		return calc_expression(interpret_stmt(expression_left(stmt), 
			temp_variables), expression_operator(stmt), 
			interpret_stmt(expression_right(stmt), temp_variables))

	if isselection(stmt):
		temp_variables = selection(stmt, temp_variables)
		return temp_variables
	
	if isrepetition(stmt):
		temp_variables = repetition(stmt, temp_variables) 
		return temp_variables
	#If no known function, return the result of the interpret_program.
	else:
		return interpret_program(stmt, temp_variables)
	#Return the updated temp_variables.
	return temp_variables;

def calc_expression(left, operator, right):
	"""
	Return the result of the calculation.
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
	Interpret the repetition_condition and return the updated temp_variables.
	"""
	temp_variables = copy.deepcopy(variables)
	while interpret_stmt(repetition_condition(stmt), temp_variables):
		temp_variables = interpret_program(repetition_statements(stmt), temp_variables)
	return temp_variables

def selection(stmt, variables):
	"""
	Interpret the selection_condition and return the updated temp_variables.
	"""
	temp_variables = copy.deepcopy(variables)
	if interpret_stmt(selection_condition(stmt), temp_variables):
		return interpret_stmt(selection_true(stmt), temp_variables)

	elif hasfalse(stmt):
		return interpret_stmt(selection_false(stmt), temp_variables)
	return temp_variables

def output(stmt, variables):
	"""
	Print the output.
	"""
	print(str(output_variable(stmt)) + " = " + str(variables[output_variable(stmt)]))

def input_func(stmt, variables):
	"""
	Get the input from the user and assign it to the variable.
	Return the updated temp_variables.
	"""
	temp_variables = copy.deepcopy(variables);
	userInput = input("Enter value for " + str(assignment_variable(stmt)) + ": ")
	temp_variables[assignment_variable(stmt)] = int(userInput);
	return temp_variables

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

#Return the factorial for n
factorial = ['calc', ["read", "n"],
				["set", "res", 1],
				["while", ["n", ">", 1],
					["set", "res", ["res", "*", "n"]],
					["set", "n", ["n", "-", 1]]],
				["print", "res"]]


