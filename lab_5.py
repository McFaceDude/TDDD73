#TDDD73 Lab 5 Språk
#Samuel Lindgren samli627 
#The lab instructions said to only hand in the code I wrote myself, I therfor left out the functions 
#in the calc.py file. The code will not compile now because the functions are missing. 

"""
5A
"""
import copy #Use for deepcopy
def eval_program(program, *opt_variables):
	"""
	Create the variables dict and use the opt_variables if provided.
	Iterate through the stmts in the program and check what type of statement it is.
	Return the now updated variables dict.

	Examples:
	
	#If x is less than 4, return 3, else, return x.
	math = ["calc", ["read", "x"],  
					["if", ["x", "=", 3],
						["set", "x", 2]],
					["if", ["x", "<", 3],
						["set", "x",[12, "/", [7, "-", [1, "+", 2]]]],
						["print", "x"]],
					["if", ["x", "=", 3], 
						["print", "x"]]]
	>>>eval_program(math)
	Enter value for n: 2
	x = 3
	>>>eval_program(math)
	Enter value for n: 6
	x = 6

	Return the factorial for n:
	factorial = ['calc', ["read", "n"],
					["set", "res", 1],
					["while", ["n", ">", 1],
						["set", "res", ["res", "*", "n"]],
						["set", "n", ["n", "-", 1]]],
					["print", "res"]]
	>>>eval_program(factorial)
	Enter value for n: 4
	res = 24
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
	Check what typ of stmt it is and call the appripriate function.
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
	if isexpression(stmt) or iscondition(stmt):
		return iterate_expression(stmt, variables)

	if isselection(stmt):
		return selection(stmt, variables)
	
	if isrepetition(stmt):
		repetition(stmt, variables) 

def iterate_expression(stmt, variables):
	"""
	If the stmt is a list, call iterate_expression with the parts of the expression seperated so that
	they can be evaluated seperatly. This is to allow expressions with many lists in them.
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
	While the condition is True, apply the check_type_of_func on the statments.
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
	userInput = input("Enter value for " + str(stmt[1]) + ": ")
	assignment(['set', stmt[1], userInput], variables)

