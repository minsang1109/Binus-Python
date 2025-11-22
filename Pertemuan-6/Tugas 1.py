class student:
    "Common base class for all student"
    stuCount = 0
    
    def __init__(self, name="Student", nilai=100):
        self.name = name
        self.nilai = nilai
        student.stuCount += 1
        
    def displayCount(self):
        print("Total Student: %d" % student.stuCount)
    
    def printStudent(self):
        print("Name:", self.name, "\nNilai:", self.nilai)

name = input("Masukan nama: ")
nilai = input("Masukan nilai: ")


student1 = student(name, nilai)

student1.printStudent()
student1.displayCount()

student2 = student("Yanti", 60)

student2.printStudent()
student2.displayCount()

student3 = student("Titi", 80)

student3.printStudent()
student3.displayCount()
 
