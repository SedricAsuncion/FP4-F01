from time import sleep

class Student:
    def __init__(self, fname, lname, age, grade):
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.grade = grade
    
    #Properties
    #Gets First Name
    def get_fname(self):
        return self.first_name
    #Gets Last Name
    def get_lname(self):
        return self.last_name
    #Gets Age
    def get_age(self):
        return self.age
    #Gets Grade
    def get_grade(self):
        return self.grade

    #Behaviours
    def introduce(self):
        return(f"""Hello, my name is {self.first_name} {self.last_name}.
I am {self.age} years old and I am currently in {self.grade} grade.""")
    def complain(self, topic):
        return(f"""Have you hear about that stupid {topic}?
It shouldn't be a thing on this Earth.
If I ever think about {topic} again, I'll kill myself.""")
    
    def brag(self, topic):
        return(f"""Imagine being so successful that you don't even know {topic} 
and still pass""") 
    
    def work(self, topic):
        return(f"I'm working on {topic} right now.")


Sedric = Student("Sedric", "Asuncion" ,16, 12)
Marb = Student("Marb", "Pano", 18, 12)

print(Sedric.introduce())
sleep(1)
print(Sedric.brag("simple math"))
sleep(2)
print(Marb.introduce())
sleep(1)
print(Marb.complain("simple math"))
sleep(2)

print("Now, some random values from the student class:")
sleep(2)
print(Sedric.get_age())
sleep(1)
print(Marb.get_grade())
sleep(1)
print(Sedric.get_fname())
sleep(1)
print(Marb.get_lname())
sleep(2)

print(f"Now buzz off, politely, {Sedric.work("Python Object Oriented Programming")}")
quit()
