import operator
import random


string = raw_input("Give your math type")
index = 0
op_ind = 0
ops = {'+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv}

for char in string:
        if char == '+':
            op = list(ops.keys())[0]
            opidx = op_ind
        elif char == '-':
            op = list(ops.keys())[2]
            opidx = op_ind
        elif char == '*':
            op = list(ops.keys())[1]
            opidx = op_ind   
        elif char == '/':
            op = list(ops.keys())[3]
            opidx = op_ind
        op_ind +=1

if string.startswith('(') == True and string.endswith(')') == True:
        split_str = string.split(string[opidx])
        num1 = split_str[0].split('(')
        num2 = split_str[1].split(')')
        a = int(num1[1])
        b = int(num2[0])
        if b == 0 and op == list(ops.keys())[3]:
                raise Exception("Division by 0 can't happen")
        else:
                answer = int(ops.get(op)(a,b))
                print answer
else:
        print ("Forgot to close parenthesys")

        
        
        
