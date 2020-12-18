class A:
    @staticmethod
    def meth(value):
        print('hello')

a = A()
print(a.meth(1))
print(A.meth('Hello'))