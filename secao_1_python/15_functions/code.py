def UserAgeInSeconds():
    userAge = int(input("Enter your age: "))
    AgeSeconds = userAge * 365 * 24 * 60 * 60
    print(f"Your age in seconds is: {AgeSeconds}")


print("Welcome to your age in seconds program! ")
UserAgeInSeconds()

print("Goodbye!")