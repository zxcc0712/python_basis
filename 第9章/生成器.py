class  Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self

a = Fibs()
for f in a:
    if f>1000:
        print(f)
        break


def flateen(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1,2],[3,4],[5]]
for num in flateen(nested):
    print(num)
print(sum(i**2 for i in range(100)))