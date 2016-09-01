# coding: utf-8 


#str=("hTEeSj_CO")
#str = str.decode('utf-8')

#------------------
#3a
#Working
def split_rec(seq):
    res_lower = ""
    res_upper = " "
    def inner_loop(seq, res_lower, res_upper):
    
        if not seq:
            return(res_lower + res_upper)
        
        elif seq[0].islower() or seq[0] == "_" or seq[0] == ".":
            res_lower += seq[0]
            return inner_loop(seq[1:], res_lower, res_upper)
       
        elif seq[0].isupper() or seq[0] == " " or seq[0] == "|":
            res_upper += seq[0]
            return inner_loop(seq[1:], res_lower, res_upper)
            
        else:
            return inner_loop(seq[1:], res_lower, res_upper)
            
    return inner_loop(seq, res_lower, res_upper)



    
def split_it(str):
    res_lower = ""
    res_upper = " "
    for i in str:
    
        if not str:
            return 0
            
        elif i.islower() or i == "_" or i == ".":
            res_lower += i
    
        elif i.isupper() or i == " " or i == "|":
            res_upper += i
            
    return(res_lower + res_upper)

#print(split_it(str))
#print(split_it("lMiED)teD5E,_hLAe;Nm,0@Dli&Eg ,#4aI?rN@T§&e7#4E #<(S0A?<)NT8<0"))

#------------------
#3b
def interpret(expr ,dictio):
       
    boolean_list = ["true", "false"]
    logic_list = ["NOT", "OR", "AND"]
    res_left = []
    res_right = []
    or_exist = False
    and_exist = False
    value_list = []
    res_list_list = []
    
    def expr_func(expr, res_left, res_right, or_exist, and_exist):
        
        #print(expr)
        if not expr:
            print("DONE")
            return(res_left,  res_right, or_exist, and_exist, value_list)
  
        
        elif expr[0] == logic_list[0]:
            if or_exist or and_exist:
                res_right.append(expr[0])
                print("right 'not' found!")
                return expr_func(expr[1:], res_left, res_right, or_exist, and_exist)
            else:    
                res_left.append(expr[0])
                print("left 'not' found!")
                return expr_func(expr[1:], res_left, res_right, or_exist, and_exist)
            
        elif expr[0] == logic_list[1]:
            or_exist = True
            print("'OR' found!")
            return expr_func(expr[1:], res_left, res_right, or_exist, and_exist )
        
        elif expr[0] == logic_list[2]:
            and_exist = True
            
            print("'AND' found!")
            return expr_func(expr[1:], res_left, res_right, or_exist, and_exist)
            
        elif isinstance(expr[0], list):
            print("list")
            return expr_func(expr[0], res_left, res_right, or_exist, and_exist)
        
        else:
            print("value found")
            value_list.append(expr[0])
            return expr_func(expr[1:], res_left, res_right, or_exist, and_exist)
        
        #print(res_left)   
    
    expr_func(expr, res_left, res_right, or_exist, and_exist)
    
    print("")
    print("or_exist", or_exist)
    print("and_exist", and_exist)
    
    def before_boolean(res_array):
        if len(res_array) % 2 == 0:
            return "false"
        else:
            return "true"
    
    res_list_list.append(res_left)
    res_list_list.append(res_right)
    
    
    
    for i, j in enumerate(value_list):
        print("")
        print(and_exist, dictio[j], before_boolean(res_list_list[i]))
        
        if not and_exist:
            if dictio[j] != before_boolean(res_list_list[i]):
                print("FALSE MA DA FACKA!")
                return False
        else:
            print("TRUE MA DA FACKA!")
        
   
    
#print(interpret(["yoyoy"], [{"eheh":"false"}]))

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
        
print (func( ["NOT",["NOT", ["NOT", ["cat_asleep"]]]]))
#print(func([1, [2, [3, [4, 5]]]]))

# [1, [3, [5, [1, 3]]]]

# 1   [3, [5, [1, 3]]]

# 3    [5, [1, 3]] = 9

# 5    [1, 3] = 4

# 1    3
            
                
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#practise exercises
#3.4
#Working
def sum_all_numbers(seq):
    def sum(seq, result):
        
        if not seq:
            return result
            
        elif isinstance(seq[0], int):
            result += seq[0]
            return sum(seq[1:], result)
            
        elif isinstance(seq[0], list):
            return sum(seq[0] + seq[1:], result)
            
        else:
            return sum(seq[1:], result)
        
    return sum(seq, 0)
#print (sum_all_numbers(["a", "b", ["c", 3, 4, [5, "d"], 10], 9]))

#working
def exists(char, seq):
    print (seq)
    if not seq:
        return False
    
    elif isinstance(seq[0], list):
        if char in seq[0]:
            return True
        else:
            return exists(char, seq[0]+seq[1:])

    elif char == seq[0]:
        return True
    else:
        return exists(char, seq[1:])

#print(exists("s", ["a", ["h", "e", "j"], ["t", "e", "s", "c", "o"]]))

#working
def without_vowels(seq):
    vowel_list = ['a', 'e', 'i', 'o', 'u']

    if not seq:
        return []
        
    elif isinstance(seq[0], list):
        return [without_vowels(seq[0])] + without_vowels(seq[1:])
        
    elif seq[0] in vowel_list:
        return without_vowels(seq[1:])
        
    else:
        return [seq[0]] + without_vowels(seq[1:])
        
#print(without_vowels(["a", ["h", "e", "j"], ["t", ["r", "a"], "e", "s", "c", "o"], "a", "t"]))

###################
#Omtenta 2014-4-25#
###################
#1a Working
def replace(seq, old, new):
    result = ""
    
    for i in seq:
        if i in old:
            result += new
        else:
            result += i
    
    return result
    
#print(replace('One, two, three!', ' .,!?', ''))

#1b working
def title(seq):
    result = ""
    new_word = True
    
    for i in seq:
        if i == " ":
            new_word = True
        
        elif new_word == True:
            result += " " + i.upper()
            new_word = False
            
        else:
            result += i.lower()
    
    return result[1:]
    
#print(title('66ONE, adtwo, thdsaree!'))

#2
#Working
def intersect_i(seq1, seq2):
    result= []
    
    for i in seq1:
        if i in seq2:
            result.append(i)
        
    return result
    

#Working
def intersect_r(seq1, seq2):
    
    if not seq1:
        return []
    elif seq1[0] in seq2:
        return [seq1[0]] + intersect_r(seq1[1:], seq2)
    else:
        return intersect_r(seq1[1:], seq2) 

#print (intersect_r([1, 2, 3, 6 ], [9, 1, 2,4,6,7,8]))
            
#3a Working
def each_pair(seq, fn):
    result = []
    for i, val in enumerate(seq):
        if i + 1 < len(seq):
            val = seq[i+1]
            result.append(fn(seq[i], val))
    return result
    
#print (each_pair([3, 7, 9, 15, 23, 27, 33], (lambda x, y: y-x)))

#3b Working
def combine_pairs(seq, fn_pair, fn_combine, boolean):
    result = []
    for i, val in enumerate(seq):
        if i + 1 < len(seq):
            val = seq[i+1]
            result.append(fn_pair(seq[i], val))         
    for j in result:
        if fn_combine(j, boolean) != True:
            return False        
    return True
    
#print(combine_pairs([5, 4, 3, 1], (lambda x, y:x>y),(lambda a, b:a and b), True))

#################
#Tenta 2014-1-15#
#################

#1a Working
def ascending(seq):
    res = ""
    res += seq[0]
    for i in seq:
        if i.lower() > res[-1].lower():
            res += i
    return res

#print(ascending("dEkOr"))

#1b Working
def decode(seq):
    res = ""
    temp_seq = ""
    
    for i, val in enumerate(seq):
        
        if val == " " or i + 1 == len(seq) :
            res += ascending(temp_seq)
            temp_seq = ""
        else:
            temp_seq += val
            
    return res
#print(decode("Mack ide dada namn atoll toviga idag dakob nissan ubat migg"))

def remove_empty_i(seq):
    res = []
    for e in seq:
        if e:
            res.append(e)
    return res
            
#print(  remove_empty_i([[3, 2, 3, 3, 4, 3, 2, 3, 4], [], [6, 5, 6, 7, 8], 
#[-2], [5, -2, 5, 3, 0, 4, 3], [], [4, 6, 0, 2, -3]]))










