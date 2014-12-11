class Class_my():
    x = 100

    def __init__(self, x=100):
        y = x
        self.y = y + 100

    def print_res(self):
        print(self.y)
    

class New_class(Class_my):
    def __init__(self):
        self.y = 100

obj = Class_my()
obj_1 = New_class()
obj_1.print_res()
obj_1.x1 = 100
obj_1.x2 = 200

