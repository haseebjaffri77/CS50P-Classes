students = [
    {"name": "Hermoine" , "house": "Gryffindor" , "patronus": "Otter"},
    {"name": "Harry" , "house": "Gryffindor" , "patronus": "Stag"},
    {"name": "Ron" , "house": "Gryffidnor" , "patronus": "Jack Terrier"},
    {"name": "Draco" , "house": "Slytherin" , "patronus": None}
]

for student in students:
    print(student["name"] , student["house"] , student["patronus"] , sep=" ,")