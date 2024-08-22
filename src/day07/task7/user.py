names = [ ]
class studentList :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"student(name='{self.name}', age={self.age})"