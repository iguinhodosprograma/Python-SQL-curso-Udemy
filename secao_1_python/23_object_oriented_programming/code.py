student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def avarage(sequence): 
    return sum(sequence) / len(sequence)

print(avarage(student["grades"]))