class Recursion:
    def __init__(self):
        self.s = 0

    def NaturalNumberSum(self, n):
        if n==1:
            return 1
        return n+ self.NaturalNumberSum(n-1)
    
    def OddNumberSum(self, n):
        if n == 1:
            return 1
        return 2*n -1 + self.OddNumberSum(n-1)
    
    def EvenNumberSum(self, n):
        if n == 1:
            return 2
        return 2*n + self.EvenNumberSum(n-1)

    def factorial(self, n):
        if n==1:
            return 1
        return n* self.factorial(n-1)
    
    def SquareSum(self, n):
        if n==1:
            return 1
        return n*n+ self.SquareSum(n-1)
    
    
re = Recursion()
# print(re.NaturalNumberSum(3))
print(re.SquareSum(3))