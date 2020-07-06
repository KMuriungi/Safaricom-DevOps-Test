# Define

# the solution.

def solution(S):

    # Define the stack.

    stack = []

    # Get the list

    # of operations.

    operations = S.split()

    # Run the loop to traverse

    # the list of operations.

    for currOperation in operations:

        # Define the try block to check

        # if the current operation

        # is a number.

        try:

            # If the conversion fails,

            # move to the except block.

            x = int(currOperation)

            

            # Otherwise, the push the

            # number onto the stack.

            stack.append(x)

        

        except:

            # Perform the required operation.

            if currOperation == 'POP':

                stack.pop()

            elif currOperation == 'DUP':

                x = stack[len(stack) - 1]

                stack.append(x)

            elif currOperation == '+':

                if(len(stack)<2):

                    return -1

                else:

                    x = stack.pop()

                    y = stack.pop()

                    if x+y > 2**20:

                        return-1

                    stack.append(x+y)

            elif currOperation == '-':

                if(len(stack)<2):

                    return -1

                else:

                    x = stack.pop()

                    y = stack.pop()

                    if(x -y) < 0:

                        return -1

                    stack.append(x-y)

        

    if len(stack) == 0:

        return -1

    else:

        return stack.pop()

# Define the main() function to

# test the working of the function.

def main():

    # Call the function with different

    # operations and print their results.

    

    S = "13 DUP 4 POP 5 DUP + DUP + -"

    print('S = ', S)

    print('solution(S) = ', solution(S))

    S = "5 6 + -"

    print('S = ', S)

    print('solution(S) = ', solution(S))

    S = "3 DUP 5 - -"

    print('S = ', S)

    print('solution(S) = ', solution(S))

# Call the main() function.

main()