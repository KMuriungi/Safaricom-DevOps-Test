def solution(S):
    stack = []
    operations = S.split()
    for currOperation in operations:
        try:
            x = int(currOperation)
            stack.append(x)
        except:
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