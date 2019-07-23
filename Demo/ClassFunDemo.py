class MyClass:
    name="Vinay"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sum(self,a,b):
        print(a+b)


x=MyClass("vinay",3)
print(x.name)
x.sum(4,5)

