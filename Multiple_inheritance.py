class Parent:
    def name(self,father,mother):
          Father_name=father
          mother_name=mother
          print("Father Name : ",father)
          print("Mother Name : ",mother)
          
          
class Marks:
    def mark(self,eng,mat,sci):
          English_mark=eng
          Maths_mark=mat
          Science_mark=sci
          Total_mark= eng+mat+sci
          print("English Mark : ",eng)
          print("Maths Mark : ",mat)
          print("Science Mark : ",sci)
          print("Total Marks : ",Total_mark)
          
class Student(Parent,Marks):
    def stud(self,reg,n):
          Reg_no=reg
          Name=n
          print("Reg.no : ",Reg_no)
          print("Name : ", Name)
          
s1=Student()
s1.stud("reg.no","Student Name")
s1.name("Father Name","Mother Name")
s1.mark(100,100,100)
