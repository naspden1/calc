# calc

def has_number_been_used(num, used_numbers):
    return num in used_numbers

"""
def EvaluateGoToExpr(input, used_numbers):
    tokens = input.split()
    if len(tokens)==2:
        newindex = int(tokens[1])-1
        if has_number_been_used(newindex):
            # bingo
            return true, 
        else:
            used_numbers.append(newindex)

        # if newindex in used numbers then we've metbefore
        return EvaluateExpr(calcs[newindex])

    operator = tokens[2]
    if operator == 'x':
        operator = '*'

    evaluation = (eval(tokens[3] + operator + tokens[4]))
    newIndex = int(evaluation)-1
    return EvaluateExpr(newIndex)
"""
def EvaluateExpr(input):
    tokens = input.split()

    operator = tokens[1]
    if operator == 'x':
        operator = '*'
    elif operator == '^':
        operator = '**'
    elif operator == '%':  # not necessary but used durnig git conflict resolution exercise!
        operator = '%'

    evaluation = (eval(tokens[2] + operator + tokens[3]))
    return evaluation

def ParseInput(inputstr):
    return inputstr

def GetUserInput():
    while True:
        userinput = input("Enter op and two single-digit integers: ")
        if (len(userinput) != 3):
          print("Try again")
          continue
        else:
            # todo parse input
          userinput = ParseInput(userinput)
          return userinput

#input = GetUserInput()
#print(eval(input[1] + input[0] + input[2]))

with open('calc.txt', 'r') as fileinput:
    all_the_calcs = fileinput.read().splitlines()

running_total = 0
num_of_lines = 0
for index in range(0,len(all_the_calcs)):
    this_total = EvaluateExpr(all_the_calcs[index])
    running_total = running_total + this_total
    num_of_lines = num_of_lines + 1
    
print('Total is ' + str(running_total) + ', number of lines processed is ' + str(num_of_lines))

#######################################################
"""
with open('gotocalc.txt', 'r') as gotofileinput:
    all_the_calcs = gotofileinput.read().splitlines()

running_total = 0
num_of_lines = 0
for index in range(0,len(all_the_calcs)):
    this_total = EvaluateGoToExpr(all_the_calcs[index])
    running_total = running_total + this_total
    num_of_lines = num_of_lines + 1
    
print('Total is ' + str(running_total) + ', number of lines processed is ' + str(num_of_lines))
"""