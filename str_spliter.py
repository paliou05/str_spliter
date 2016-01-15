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

#check for parenthesys at start and end of the string
def check_string(string, operation, ops):
        if string.startswith('(') == True and string.endswith(')') == True:
                split_str(string, operation, ops) 
        else:
                print ("\nForgot to close parenthesys\n")
                
#split the string and keeps the two numbers
def split_str(string, operation, ops):
        split_str = string.split(operation)
        num1 = split_str[0].split('(')
        num2 = split_str[1].split(')')
        try:
                first_num = int(num1[1])
                second_num = int(num2[0])
        except ValueError:
                print "\nThat's not a number, please enter only numbers\n"
        if second_num == 0 and op == list(ops.keys())[3]:
                raise Exception("\nDivision by 0 can't happen\n")
        else:        
                give_answer(first_num, second_num, ops)
                
#calculates and prints our math operation result
def give_answer(first_num, second_num, ops):
        answer = int(ops.get(op)(first_num,second_num))
        print answer
        
if __name__ == '__main__':
        string = raw_input("Give your math type\n>")
        ops = {'+':operator.add,
                '-':operator.sub,
                '*':operator.mul,
                '/':operator.truediv}
        op, operation = find_operation(string, ops)
        check_string(string, operation, ops)
        
        