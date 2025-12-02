def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

grades = []

print("Welcome to the avarage grade program.")

try:
    avarage = divide(sum(grades), len(grades))
    
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")

else:
    print(f"The avarage grade is {avarage}.")

finally:
    print("Thank you!")