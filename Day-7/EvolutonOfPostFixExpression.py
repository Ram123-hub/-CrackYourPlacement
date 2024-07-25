def evaluatePostfixExpression(s:str)->int:
    stack = []

    for char in s:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == "+":
                stack.append(operand1 + operand2)
            elif char == "-":
                stack.append(operand1-operand2)
            elif char == "*":
                stack.append(operand1*operand2)
            elif char == "/":
                stack.append(int(operand1/operand2))
    return stack[0]

print(evaluatePostfixExpression("231*+9-"))
print(evaluatePostfixExpression("123+*8-"))

