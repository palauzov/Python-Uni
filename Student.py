class Student:
    class_data = 3
    def static_method(self):
        print("I am Student")

    def __init__(self):
        self.instance_data = 1
    
    def __str__(self):
        return "data: " + str(self.instance_data)
    
    def __repr__(self):
        return self.__str__()

print(Student.class_data)
obj = Student()
print(obj.instance_data)
obj.static_method()
