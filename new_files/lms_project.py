dict = {
    "Students": "",
    "Teachers": [],
}

import random

class table_sheet:
    def __init__(self , name):
        self.name = name

    @staticmethod
    def random_pop():
        return random.randint(0 , 100)
         

    def add_to_dict():
        dict.update({"Students": result})
           

class students(table_sheet):
    def __init__(self, name , sphere):
        super().__init__(name)
        self.sphere = sphere

        
    @property
    def get_info(self):
        return self.name , self.sphere
    
class teachers(students):
    def __init__(self , name , rating):
        super().__init__(name ,rating)
        self.name = name 

    def add_to_dict():
        dict["Teachers"].append(obj_3.name)
     
    def get_info(self):
        return super().get_info
    
class choose_sphere(table_sheet):
    def __init__(self , name , popularity):
        super().__init__(name)
        self.popularity = popularity

class info:
    phone_number = "Our phone number: + 7 777 008 90 66"
    contact_info = "You can visit our team on: Instagram , Youtube , Twitter"


        
pop = choose_sphere("Math" , 90)  
print(f"{pop.name}'s popularity is {pop.popularity}%")
    
result = []

obj_1 = students("Miras" , "Mathematics")
print(obj_1.get_info)
result.append(obj_1.get_info[0])
students.add_to_dict()

obj_2 = students("Aliya" , "Russian language")
result.append(obj_2.get_info[0])
students.add_to_dict()


obj_3 = teachers("Zhaks" , 100)
print(obj_3.get_info())
teachers.add_to_dict()

for key ,value in dict.items():
    print(f"{key}: {value}")

print(f"{info.phone_number}\n{info.contact_info}")