class parent:
    def m1(self):
        print('world')
    def m2(self):
        print('parent class')

class child(parent):
    def m3(self):
        print('hello')

    def m2(self):
        print('child class')
        super().m1()
        parent.m2(self)

obj1 = child()
obj1.m2()