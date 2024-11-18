class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        assert isinstance(a, int) and isinstance(b, int), "Arguments must be integers"
        result = 0
        if b < 0 and a < 0:
            b = abs(b)
            a = abs(a)
            for i in range(b):
                result = self.add(result, a)
            return result
        elif b < 0 and a > 0:
            b = abs(b)
            a = abs(a)
            result = 0
            for i in range(b):
                result = self.add(result, a)
            return -result
        elif b > 0 and a < 0:
            b = abs(b)
            a = abs(a)
            result = 0
            for i in range(b):
                result = self.add(result, a)
            return -result
        else:
            for i in range(b):
                result = self.add(result, a)
            return result

    def divide(self, a, b):
        assert isinstance(a, int) and isinstance(b, int), "Arguments must be integers"
        assert b != 0, "Cannot divide by zero"
        if (a < 0 or b < 0) and abs(a) > abs(b):
            a = abs(a)
            b = abs(b)
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result -= 1
            return result
        elif (a < 0 and b < 0) or (a > 0 and b > 0):
            a = abs(a)
            b = abs(b)
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result
        else:
            a = abs(a)
            b = abs(b)
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return -result
    
    def modulo(self, a, b):
        if b == 0:
            return "divisor can't be 0"

        # If the original a was negative, adjust the result to keep it non-negative
        if a < 0 and self.modulo(b,2) != 0 :#(-,odd)
            a = -a
            while a >= b:
                a -= b
            return a + 1
        elif a < 0 and self.modulo(b,2) == 0 :#(-,even)
            a = -a
            while a >= b:
                    a -= b
            return a
        elif b < 0 and self.modulo(b,2) != 0 :#(...,-odd)
            b = -b
            while a >= b:
                a -= b
            return -(a + 1)
        elif b < 0 and self.modulo(b,2) == 0 :#(...,-even)
            b = -b
            while a >= b:
                a -= b
            return -a
        else:
            while a >= b:
                a -= b
            return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))