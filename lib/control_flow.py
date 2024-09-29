#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

# Example usage
print(admin_login("admin", "12345"))  # Output: Access granted
print(admin_login("ADMIN", "12345"))  # Output: Access granted
print(admin_login("user", "password")) # Output: Access denied


def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

# Example usage
print(hows_the_weather(30))   # Output: It's brisk out there!
print(hows_the_weather(50))   # Output: It's a little chilly out there!
print(hows_the_weather(90))   # Output: It's too dang hot out there!
print(hows_the_weather(70))   # Output: It's perfect out there!

def fizzbuz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    
    # Example Usage
    print(fizzbuzz(15))  # Output: Fizzbuzz
    print(fizzbuzz(9))  # Output: Fizz
    print(fizzbuzz(10))  # Output: Buzz
    print(fizzbuzz(7))  # Output: 7


def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
    
    # Example usage
    print(calculator("+", 5,3)) # Output: 8
    print(calculator("-", 10, 4)) # Output: 6
    print(calculator("*", 7,6)) # Output: 42
    print(calculator("/", 20, 5)) # Output: 4.0
    print(calculator("x", 5, 3)) # Output: Invalid operation! and returns None