#TDDD73 Lab 3 Bearbetning av listor
#Samuel Lindgren samli627 

"""
#3a
"""

def split_rec(seq):
    return split_rec_loop(seq, "", "")

def split_rec_loop(seq, res_lower, res_upper):

    if not seq:
        return(res_lower, res_upper)
    
    elif seq[0].islower() or seq[0] == "_" or seq[0] == ".":
        res_lower += seq[0]
        return split_rec_loop(seq[1:], res_lower, res_upper)
   
    elif seq[0].isupper() or seq[0] == " " or seq[0] == "|":
        res_upper += seq[0]
        return split_rec_loop(seq[1:], res_lower, res_upper)
        
    else:
        return split_rec_loop(seq[1:], res_lower, res_upper)
        
    return split_rec_loop(seq, res_lower, res_upper)
"""
def split_rec(seq):
    return split_rec_loop(seq, "", "")

def split_rec_loop(seq):

    if not seq:
        return []
    
    elif seq[0].islower() or seq[0] == "_" or seq[0] == ".":
        
        return ([str(seq[0]) + str(split_rec_loop(seq[1:]), split_rec_loop(seq[1:]))])
   
    elif seq[0].isupper() or seq[0] == " " or seq[0] == "|":
        
        return (split_rec_loop([seq[1:], str(seq[0]) + str(split_rec_loop(seq[1:]))]))
        
    else:
        return split_rec_loop(seq[1:])
        
"""    

def split_it(str):
    res_lower = ""
    res_upper = ""
    for i in str:
    
        if not str:
            return 0
            
        elif i.islower() or i == "_" or i == ".":
            res_lower += i
    
        elif i.isupper() or i == " " or i == "|":
            res_upper += i
            
    return(res_lower, res_upper)


#print(split_rec_loop("lMiED)teD5E,_hLAe;Nm,0@Dli&Eg ,#4aI?rN@T§&e7#4E #<(S0A?<)NT8<0"))

"""
3B
"""
def interpret(expr ,dictio):
       
    boolean_type_list = ["true", "false"]
    logic_list = ["NOT", "OR", "AND"]
    not_list_left = []
    not_list_right = []
    or_exist = False
    and_exist = False
    value_list = []
    not_lists = []

    expr_func_res = (expr_func(expr, not_list_left, not_list_right, or_exist, 
        and_exist, boolean_type_list, logic_list, value_list))
    print("test1", expr_func_res)
    not_list_left = expr_func_res[0];
    not_list_right = expr_func_res[1];
    or_exist = expr_func_res[2];
    and_exist = expr_func_res[3];
    value_list = expr_func_res[4];

    print(expr_func_res)

    print("")
    print("or_exist", or_exist)
    print("and_exist", and_exist)
    print("value_list", value_list)


    not_lists.append(not_list_left)
    not_lists.append(not_list_right)
    print("not_lists: ", not_lists)

    for index, value in enumerate(value_list):
        print("")
       
        if value == boolean_type_list[0]:
            dictio[value] = boolean_type_list[0]
        elif value == boolean_type_list[1]:
            dictio[value] = boolean_type_list[1]
        print(dictio)
        print(and_exist, dictio[value], boolean_type(not_lists[index]))

        if and_exist:
            if dictio[value] != boolean_type(not_lists[index]):
                print("Output:")
                return boolean_type_list[1]
            elif index == len(value_list)-1:

                print("Output:")
                return boolean_type_list[0]
        elif or_exist:
            if dictio[value] == boolean_type(not_lists[index]):
                print("Output:")
                return boolean_type_list[0]

            elif index == len(value_list)-1:
                print("Output:")
                return boolean_type_list[1]
            else:
                print("loop 2 error")
        elif dictio[value] == boolean_type(not_lists[index]):
            print("Output:")
            return boolean_type_list[0]
        else:
            print("Output:")
            return boolean_type_list[1]

    
def is_logic_constant(value):
    if value in boolean_type_list:
        return True
    else: 
        return False

def is_logic_expression(expr):
    if len(expr) == 2:
        return False
    else:
        return True


def expr_func(expr, not_list_left, not_list_right, or_exist, and_exist, boolean_type_list, 
    logic_list, value_list):
    
    print("expr", expr)
    if not expr:
        print("DONE")
        return(not_list_left, not_list_right, or_exist, and_exist, value_list)

    elif isinstance(expr[0], list):
        print("list", expr[0])
        return expr_func(expr[0], not_list_left, not_list_right, or_exist, and_exist
            ,boolean_type_list, logic_list, value_list)
    
    elif expr[0] == logic_list[0] and is_logic_expression(expr[1:]) == True:
        if or_exist or and_exist:
            not_list_right.append(expr[0])
            print("right 'not' found!")
            return expr_func(expr[1:], not_list_left, not_list_right, or_exist, 
                and_exist, boolean_type_list, logic_list, value_list)
        else:    
            not_list_left.append(expr[0])
            print("left 'not' found!")
            return expr_func(expr[1:], not_list_left, not_list_right, or_exist, 
                and_exist, boolean_type_list, logic_list, value_list)
    
    elif len(expr[1:]) > 0:
        print("len > 0")
        if expr[0] == logic_list[1] :
            or_exist = True
            print("'OR' found!")
            return expr_func(expr[1:], not_list_left, not_list_right, or_exist, 
                and_exist, boolean_type_list, logic_list, value_list)
        
        elif expr[0] == logic_list[2]:
            and_exist = True
            
            print("'AND' found!")
            return expr_func(expr[1:], not_list_left, not_list_right, or_exist, 
                and_exist, boolean_type_list, logic_list, value_list)
 
    if isinstance(expr, str):
        print("value found")
        print("DONE")
        value_list.append(expr)
        return(not_list_left, not_list_right, or_exist, and_exist, value_list)  

    else:
        print("value found")
        value_list.append(expr[0])
        
        
        return expr_func(expr[1:], not_list_left, not_list_right, or_exist, 
            and_exist, boolean_type_list, logic_list, value_list)
    
    #print(not_list_left)   
    
   
def boolean_type(not_list):
        
    if len(not_list) % 2 == 0:
        return "true"
    else:
        return "false"

#test_list = ["cat_asleep", "OR", ["NOT", "cat_asleep"]]
#print(test_list[1:])
#is_logic_expression(test_list[1:])
        
    
#print(interpret(["cat_asleep", "OR", ["NOT", ["NOT",["NOT", "cat_gone"]]]],
#               {"door_open" : "false", "cat_gone" : "true", "cat_asleep" : "true"}))


def func(input):

    if not input:
        print("DONE", input)
    
    elif input == "NOT":
        print("")
        print("NOT found", input)
        
        return input
        
    elif isinstance(input, list):
        print("")
        print("list found")
        print(input[0],  input[1])
       
        return func(input[0]), func(input[1])
        


def interpret_new(input):
    if isinstance(input, int):
        return input
        
    return interpret_new[0] + interpret_new(input[1])
        
#print (func( ["NOT",["NOT", ["NOT", ["cat_asleep"]]]]))
#print(func([1, [2, [3, [4, 5]]]]))

"""
3C
"""

board = {};

def reset_board():
    """
    Remove all entries to board.
    Return value:
    Nothing
    """

    board.clear();

def isfree(x, y):
    """
    Check if place (x,y) exists in board. Return boolean.
    Arguments:
    x -- column, number 
    y -- row, number
    Return value:
    Boolean
    """
   
    return ((x, y) not in board)

def place_piece(x, y, player):
    """
    Place player on position (x,y). Return boolean if successful or not.
    Arguments:
    x -- column, number
    y -- row, number
    player -- player namne, string
    Return Value:
    Boolean -- True if succesfull, False if position is taken.
    """
    if isfree(x, y):
        board[x, y] = player;
        return True
    else:
        return False

def get_piece(x, y):
    """
    Return the name of a player on a position, if no player, return 
    false.
    Argumnets:
    x -- column, number
    y -- row, number
    Return value:
    player -- player namne, string, if the position is taken.
    boolean -- False if the position is free.
    """
    if isfree(x, y):
        return False
    else:
        return board[(x, y)]

def remove_piece(x, y):
    """
    Remove player from position. Return if it was successful.
    Argumnets:
    x -- column, number
    y -- row, number
    Return value:
    boolean -- True if player was removed, False if no player existed. 
    """
    if isfree(x, y):
        return False
    else:
        del board[(x, y)]
        return True

def move_piece(old_x, old_y, new_x, new_y):
    """
    Move a player from one position to another, return boolean depending
    on if it was successful.
    Return value:
    Boolean -- True if piece was moved. False if piece did not exist or
    if the new position was taken.
    """
    if not isfree(old_x, old_y) and isfree(new_x, new_y):
        place_piece(new_x, new_y, board[(old_x, old_y)])
        remove_piece(old_x, old_y)
        return True
    else:
        return False

def count(row_or_column, number, player):
    """
    Return the number of times a player has a piece on a row or column 
    with the argument number.
    """
    res = 0;

    if row_or_column == "column":
        row_or_column = 0;
    else:
        row_or_column = 1;

    for position, player_name in board.items():
        if position[row_or_column] == number and player_name == player:
            res += 1;
    return res

def nearest_piece(x, y):
    """
    Return the position which is closests to the argument cordinates.
    If board is empty, return False.
    """
    if len(board.keys()) == 0:
        return False

    shortest_distance = [];

    
    #Loop through all the pieces on the board
    for position, player_name in board.items():
        #Calculate the distance with pythagoras definition
        if position[0] < x:
            x_res = (x - position[0])**2;
        else:
            x_res = (position[0] - x)**2;

        if position[1] < y:
            y_res = (y - position[1])**2;
        else:
            y_res = (position[1] - y)**2;

        current_distance = (x_res + y_res)**0.5;
        
        #Check if there is previous shortest_distance.
        if len(shortest_distance) > 0:
            #Check if it is shorter
            if current_distance < shortest_distance[0]:
                shortest_distance[0] = current_distance;
                shortest_distance[1] = position;
        #If no privious distance, set current_distance as shortest.
        else:
            shortest_distance.append(current_distance);
            shortest_distance.append(position);

    return shortest_distance[1];



