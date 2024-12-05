class Rescursion:
    
    def NaturalNumber(self,n):
        if n == 1:
            print(n)
        else:
            self.NaturalNumber(n-1)
            print(n)
    
    def NaturalNumberR(self, n):
        if n == 1:
            print(n)
        else:
            print(n)
            self.NaturalNumberR(n-1)
    
    def OddNumber(self, n):
        if n == 1:
            print(n)
        else:
            self.OddNumber(n-1)
            if n%2==1:
                print(n)

    def EvenNumber(self, n):
        if n == 1:
            pass
        else:
            self.EvenNumber(n-1)
            if n%2==0:
                print(n)

    def OddNumberR(self, n):
        if n == 1:
            print(n)
        else:
            if n%2==1:
                print(n)
            self.OddNumberR(n-1)

    def EvenNumberR(self, n):
        if n == 1:
            pass
        else:
            if n%2==0:
                print(n)
            self.EvenNumberR(n-1)

re = Rescursion()
re.NaturalNumber(8)
print(".......................")
re.NaturalNumberR(8)
print(".......................")
re.OddNumber(10)
print(".......................")
re.EvenNumber(10)
print(".......................")
re.EvenNumberR(10)
print(".......................")
re.OddNumberR(10)
