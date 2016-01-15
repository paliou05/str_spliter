import operator

#finds the operator in the string and keeps the index of it

def find_operation(string, ops):
        index = 0
        for char in string:
                if char == '+':
                    op = list(ops.keys())[0]
                    op_indx = index 
                elif char == '-':
                    op = list(ops.keys())[2]
                    op_indx = index
                elif char == '*':
                    op = list(ops.keys())[1]
                    op_indx = index   
                elif char == '/':
                    op = list(ops.keys())[3]
                    op_indx = index
                index +=1
        operation = string[op_indx]
        return op, operation
#check for parenthesys and split the string so we extract the numbers out of it
def check_string(string, operation, ops):
        if string.startswith('(') == True and string.endswith(')') == True:
                split_str = string.split(operation)
                num1 = split_str[0].split('(')
                num2 = split_str[1].split(')')
                try:
                        a = int(num1[1])
                        b = int(num2[0])
                except ValueError:
                        print "\nThat's not a number, please enter only numbers\n"
                if b == 0 and op == ops['/']:
                        raise Exception("\nDivision by 0 can't happen\n")
                else:
                        answer = int(ops.get(op)(a,b))
                        print answer
        else:
                print ("\nForgot to close parenthesys\n")
if __name__ == '__main__':
        string = raw_input("Give your math type\n>")
        ops = {'+':operator.add,
                '-':operator.sub,
                '*':operator.mul,
                '/':operator.truediv}
        op, operation = find_operation(string, ops)
        check_string(string, operation, ops)
        
        