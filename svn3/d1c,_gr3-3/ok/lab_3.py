#TDDD73 Lab 3 Bearbetning av listor
#Samuel Lindgren samli627 

"""
3A
"""
def split_rec(seq):
    """
    Return the output from the split_rec_loop function.
    """
    return split_rec_loop(seq, "", "")

def split_rec_loop(seq, res_lower, res_upper):
    """
    Return the two strings res_lower and res_upper.
    """
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

def split_it(str):
    """
    Return the two strings res_lower and res_upper.
    """
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

"""
3B
"""
def interpret(expr, dictio):
    """
    Return the sting "true" or "false" depending of the interpretation of the expr.
    """

    if isinstance(expr, str):
        return evaluate_variable(expr, dictio)

    if len(expr) == 2:
        return negate(interpret(expr[1], dictio))
    #Interpret the two variables and evaluate them together with the operator. 
    if len(expr) == 3:
        return evaluate_operation(interpret(expr[0], dictio), expr[1], interpret(expr[2], dictio))

def evaluate_variable(variable, dictio):
    """
    Return the value of the variable in the dictio.
    If the variable is not in the dictio, return the value.
    """
    if variable in dictio:
        temp = dictio[variable];
    else:
        temp = variable;
    return temp

def evaluate_operation(left, operator, right):
    """
    Return "true" if the operation is true, return "false" otherwise.
    """
    if operator == "AND":
        if left == "true" and right == "true":
            return "true"

    if operator == "OR":
        if left == "true" or right == "true":
            return "true"
    return "false"

def negate(value):
    """
    Return the opposite string of the value.
    """
    if value == "true":
        return "false"
    return "true"

"""
3C
"""
board = {};

def reset_board():
    """
    Remove all entries to board.
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
    player -- player name, string
    Return Value:
    Boolean -- True if successful, False if position is taken.
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
    Arguments:
    x -- column, number
    y -- row, number
    Return value:
    player -- player name, string, if the position is taken.
    boolean -- False if the position is free.
    """
    if isfree(x, y):
        return False
    else:
        return board[(x, y)]

def remove_piece(x, y):
    """
    Remove player from position. Return if it was successful.
    Arguments:
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
    Return the position which is closest to the argument coordinates.
    If board is empty, return False.
    """
    if len(board.keys()) == 0:
        return False

    shortest_distance = [];

    #Loop through all the pieces on the board
    for position, player_name in board.items():
        #Calculate the distance with Pythagoras definition
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
        #If no previous distance, set current_distance as shortest.
        else:
            shortest_distance.append(current_distance);
            shortest_distance.append(position);

    return shortest_distance[1];



