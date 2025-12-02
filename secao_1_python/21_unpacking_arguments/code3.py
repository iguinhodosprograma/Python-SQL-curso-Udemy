def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
        
    return total
    
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator to apply()."
    
print(apply(1, 3, 6, 7, operator="*"))