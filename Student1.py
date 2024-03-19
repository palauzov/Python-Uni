import csv

class Student1:
    def __init__(self, fnum, name, mark):
        self.fnum = fnum
        self.name = name
        self.mark = mark
    def __str__(self):
        return f"({self.fnum}, {self.name}, {self.mark})"
    def __repr__(self):
        return self.__str__()
class Group: 
    def __init__(self):
       self.group = []

    def __str__(self):
       return self.group
    
    def __repr__(self):
        return self.__str__()
    
    def readFromCSV(self, fileName):
        with open(fileName) as f:
            reader = csv.reader(f)
            for student in reader:
               try:
                  fnum = int(student[0])
                  name = student[1]
                  mark = float(student[2])
               except ValueError:
                   pass
               else: self.group.append(Student1(fnum, name, mark))
               

    def averageMark(self):
       try:
          sumMark = 0
          for student in self.group:
             sumMark += student.mark
          return sumMark/len(self.group)
       except ZeroDivisionError:
          print("No data")









group = Group()
print(group)
#fnum = int(input("Faculty number: "))
#name = input("Name: ")
#mark = float(input("Mark: "))
#student = Student1(fnum, name, mark)
#print(student)

