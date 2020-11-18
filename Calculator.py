from typing import List

from Stack import Stack
from scipy import stats
import math


class Calculator:
    __list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    __operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '^': lambda a, b: pow(a, b),
    }

    __functions = {
        'sqrt': lambda a: math.sqrt(a),
        'sin': lambda a: math.sin(a),
        'cos': lambda a: math.cos(a),
        'ln': lambda a: math.log(a),
    }

    __priority = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
    }

    def __init__(self):
        self.stack = Stack()

    def is_float(self, num: str):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def countFunction(self, phrase: str, function: str):
        x = float(self.count(phrase))
        return str(float(self.__functions[function](x)))

    def count(self, phrase: str) -> str:
            onp_phrase = self.convertToONP(phrase)
            for char in onp_phrase:
                if self.is_float(char):
                    self.stack.push(char)
                else:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    c = self.__operators[char](float(a), float(b))
                    self.stack.push(c)
            res = self.stack.pop()
            if not self.stack.isEmpty():
                return str(0)
            return str(res)

    def convertToONP(self, phrase: str):
        stack = Stack()
        onp_phrase = []
        lastNumber = False
        for char in phrase:
            if char in self.__list_of_numbers or char == '.':
                if lastNumber:
                    last = onp_phrase.pop()
                    onp_phrase.append(last + char)
                else:
                    onp_phrase.append(char)
                lastNumber = True
            elif char == '(':
                stack.push(char)
            elif char == ')':
                while stack.peek() != '(':
                    onp_phrase.append(stack.pop())
                stack.pop()
            else:
                while not stack.isEmpty() and self.__priority[stack.peek()] >= self.__priority[char]:
                    onp_phrase.append(stack.pop())
                stack.push(char)
                lastNumber = False

        while not stack.isEmpty():
            onp_phrase.append(stack.pop())

        return onp_phrase

    @staticmethod
    def normaDistribution(listVar: List[float]):
        print(listVar)
        shapiro_test = stats.shapiro(listVar)
        return shapiro_test.statistic, shapiro_test.pvalue