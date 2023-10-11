class LinearModel:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute(self, x):
        output = self.a * x + self.b
        return output

    def __call__(self, x):
        output = self.a * x + self.b
        return output

lm = LinearModel(2, 3)
# out1 = lm.compute(0)
out1 = lm(0)
# out2 = lm.compute(10)
out2 = lm(10) 

print(out1)
print(out2)