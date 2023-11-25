from new_files import *
from new_files import lms_project as pr



import json
import os
#os.mkdir("all_files")

with open("./new_files/lms_project.py" , "r") as file:
    a = file.read()
    print(a)

data_to_json = json.dumps(pr.dict)
with open("table_as_json" , "w") as file:
     file.write(data_to_json)

with open("./new_files/lms_project.py" , "r") as fl:
    for line in fl.readlines():
          print(line)


def add_to_file(path):
    with open(path,  "a") as f:
        f.write("lst = []\n")
        f.write(f"lst.append({pr.dict})\n")
        f.write("print(lst)\n")
    
add_to_file("students_teachers_info.py")

#os.renames("all_files" , "new_files")



with open("extra_info" , "a") as note:
    note.write(f"{pr.info.contact_info}\n")
    note.write(pr.info.phone_number)





    



