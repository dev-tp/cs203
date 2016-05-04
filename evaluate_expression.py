#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stack(list):
    def peek(self):
        return self[len(self) - 1]

    def push(self, item):
        self.append(item)

    def not_empty(self):
        if len(self) != 0:
            return True
        return False


def evaluate_expression(expression):
    operands = Stack()  # Stack<Int>
    operators = Stack()  # Stack<Character>

    expression = insert_blanks(expression)  # Insert blanks around (, ), +, -, /, *, %, and ^

    tokens = expression.split(" ")
    tokens = [token for token in tokens if token != '']  # Remove all white spaces

    for token in tokens:
        if len(token) == 0:  # Blank space
            continue

        elif token[0] == '+' or token[0] == '-':
            while operators.not_empty() and \
                    (operators.peek() == '+' or operators.peek() == '-'
                     or operators.peek() == '*' or operators.peek() == '/' or operators.peek() == '%'
                     or operators.peek() == '^'):
                process_an_operator(operands, operators)
            operators.push(token[0])  # Push the + or - operator into the operator stack

        elif token[0] == '*' or token[0] == '/' or token[0] == '%':
            # Process all *, /, % in the top of the operator stack
            while operators.not_empty() and \
                    (operators.peek() == '*' or operators.peek() == '/' or operators.peek() == '%'):
                process_an_operator(operands, operators)
            operators.push(token[0])

        elif token[0] == '^':
            while operators.not_empty() and operators.peek() == '^':
                process_an_operator(operands, operators)
            operators.push(token[0])

        elif token[0] == '(':
            operators.push('(')

        elif token.strip()[0] == ')':
            while operators.peek() != '(':
                process_an_operator(operands, operators)
            operators.pop()  # Pop ( from stack

        else:
            operands.push(int(token))

    while operators.not_empty():  # Clear stacks; Process all the remaining operators in the stack
        process_an_operator(operands, operators)

    return operands.pop()


def process_an_operator(operands, operators):
    operator = operators.pop()
    a = operands.pop()
    b = operands.pop()

    if operator == '+':
        operands.push(b + a)
    elif operator == '-':
        operands.push(b - a)
    elif operator == '*':
        operands.push(b * a)
    elif operator == '/':
        operands.push(b / a)
    elif operator == '%':
        operands.push(b % a)
    elif operator == '^':
        operands.push(b ** a)


def insert_blanks(string):
    result = ""
    for i in range(len(string)):
        if string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-' \
                or string[i] == '*' or string[i] == '/' or string[i] == '%' or string[i] == '^':
            result += " " + string[i] + " "
        else:
            result += string[i]
    return result


def main():
    print evaluate_expression("(5*2^3+2*3%2)*4")  # 160
    print evaluate_expression("5 + 5 * 3")  # 20
    print evaluate_expression("( 1+2)*4 -3")  # 9
    print evaluate_expression("4 ^ 2")  # 16


if __name__ == "__main__":
    main()
