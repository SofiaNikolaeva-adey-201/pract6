class A:
    @staticmethod
    def meth():
        print('meth')

#A.meth()
a=A()
print(a.meth())
print(A.meth())


#b=10
#A.meth(b)

#b=10
#b.meth()
