# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:51:46 2024

@author: chien
"""

from turtle import title
from functools import reduce


print("")
title = " Chapter 19 - Exceptions & Errors in exceptions.py "
print(f"{title}".upper().center(80, "="))
print("")

title = " # 1. Introduction to Exceptions: # "
print(f"{title}".center(80, "#"))

class JustNetCoolError(Exception):
    pass

x = 2
try:
    raise JustNetCoolError("This isn't cool, man.")
    raise Exception("I'm a custom exception.")
    print(x /0)
    if not type(x) is str:
      raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("Please do not divide by zero.")
except Exception as error:
    print(f"An error occurred: {error}")
else:
    print('No errors occurred.')
finally:
    print("I'm going to print with or without an error.")
  
print("")
title = " # 2. Handling Exceptions: # "
print(f"{title}".center(80, "#"))
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("Execution of the divide function is complete.")

# Example usage
print(divide(10, 2))  # Should print the result and "Division successful."
print(divide(10, 0))  # Should print "Error: Division by zero is not allowed."
print(divide(10, 'a'))  # Should print "Error: Both arguments must be numbers."

print("")
title = " # 3. Raising Exceptions: # "
print(f"{title}".center(80, "#"))
def check_positive_number(value):
    if value < 0:
        raise ValueError("The value must be a positive number.")
    return value

def greet(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    if name == "":
        raise ValueError("Name cannot be an empty string.")
    print(f"Hello, {name}!")

# Example usage
try:
    print(check_positive_number(10))  # Should print 10
    print(check_positive_number(-5))  # Should raise ValueError
except ValueError as e:
    print(f"ValueError: {e}")

try:
    greet("Alice")  # Should print "Hello, Alice!"
    greet(123)      # Should raise TypeError
except TypeError as e:
    print(f"TypeError: {e}")

try:
    greet("")       # Should raise ValueError
except ValueError as e:
    print(f"ValueError: {e}")

print("")
title = " # 4. Built-in Exceptions: # "
print(f"{title}".center(80, "#"))
# Example of AttributeError
try:
    obj = None
    obj.some_method()
except AttributeError as e:
    print(f"AttributeError: {e}")

# Example of ImportError
# try:
#     import non_existent_module
# except ImportError as e:
#     print(f"ImportError: {e}")

# Example of IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print(f"IndexError: {e}")

# Example of KeyError
try:
    d = {'key': 'value'}
    print(d['non_existent_key'])
except KeyError as e:
    print(f"KeyError: {e}")

# Example of NameError
# Remove the line that references the undefined variable
# try:
#     print(undefined_variable)
# except NameError as e:
#     print(f"NameError: {e}")

# Example of TypeError
try:
    result = 'string' + 10
except TypeError as e:
    print(f"TypeError: {e}")

# Example of ValueError
try:
    num = int('not_a_number')
except ValueError as e:
    print(f"ValueError: {e}")

# Example of FileNotFoundError
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# Example of ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

print("")

title = " # 5. Custom Exceptions: # "
print(f"{title}".center(80, "#"))

# Define custom exceptions
class CustomError(Exception):
    """Base class for other exceptions"""
    pass

class NegativeValueError(CustomError):
    """Raised when the input value is negative"""
    def __init__(self, value):
        self.value = value
        self.message = f"Negative value error: {value} is not allowed."
        super().__init__(self.message)

class NotAStringError(CustomError):
    """Raised when the input value is not a string"""
    def __init__(self, value):
        self.value = value
        self.message = f"Not a string error: {value} is not a string."
        super().__init__(self.message)

# Example functions that raise custom exceptions
def check_positive_number(value):
    if value < 0:
        raise NegativeValueError(value)
    return value

def greet(name):
    if not isinstance(name, str):
        raise NotAStringError(name)
    if name == "":
        raise ValueError("Name cannot be an empty string.")
    print(f"Hello, {name}!")

# Example usage
try:
    print(check_positive_number(10))  # Should print 10
    print(check_positive_number(-5))  # Should raise NegativeValueError
except NegativeValueError as e:
    print(f"NegativeValueError: {e}")

try:
    greet("Alice")  # Should print "Hello, Alice!"
    greet(123)      # Should raise NotAStringError
except NotAStringError as e:
    print(f"NotAStringError: {e}")

try:
    greet("")       # Should raise ValueError
except ValueError as e:
    print(f"ValueError: {e}")

print("")
title = " # 6. Exception Propagation: # "
print(f"{title}".center(80, "#"))

# Assuming the custom exceptions and functions are already defined as in the provided code

# Function that calls check_positive_number and lets the exception propagate
def process_number(value):
    return check_positive_number(value)

# Function that calls greet and lets the exception propagate
def process_greeting(name):
    greet(name)

# Main function that handles the exceptions
def main():
    try:
        print(process_number(10))  # Should print 10
        print(process_number(-5))  # Should raise NegativeValueError
    except NegativeValueError as e:
        print(f"NegativeValueError caught in main: {e}")

    try:
        process_greeting("Alice")  # Should print "Hello, Alice!"
        process_greeting(123)      # Should raise NotAStringError
    except NotAStringError as e:
        print(f"NotAStringError caught in main: {e}")

    try:
        process_greeting("")       # Should raise ValueError
    except ValueError as e:
        print(f"ValueError caught in main: {e}")

# Run the main function
if __name__ == "__main__":
    main()
    
print("")
title = " # 7. Assertions: # "
print(f"{title}".center(80, "#"))
# Function to demonstrate assertions
def divide(a, b):
    assert b != 0, "Division by zero is not allowed."
    return a / b

def test_assertions():
    # This should pass
    try:
        result = divide(10, 2)
        print(f"10 / 2 = {result}")
    except AssertionError as e:
        print(f"AssertionError: {e}")

    # This should fail and raise an AssertionError
    try:
        result = divide(10, 0)
        print(f"10 / 0 = {result}")
    except AssertionError as e:
        print(f"AssertionError: {e}")

# Run the test function
if __name__ == "__main__":
    test_assertions()

print("")
title = " # 8. Best Practices: # "
print(f"{title}".center(80, "#"))
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Custom exceptions
class CustomError(Exception):
    """Base class for other exceptions"""
    pass

class NegativeValueError(CustomError):
    """Raised when the input value is negative"""
    def __init__(self, value):
        self.value = value
        self.message = f"Negative value error: {value} is not allowed."
        super().__init__(self.message)

class NotAStringError(CustomError):
    """Raised when the input value is not a string"""
    def __init__(self, value):
        self.value = value
        self.message = f"Not a string error: {value} is not a string."
        super().__init__(self.message)

# Example functions
def check_positive_number(value):
    if value < 0:
        raise NegativeValueError(value)
    return value

def greet(name):
    if not isinstance(name, str):
        raise NotAStringError(name)
    if name == "":
        raise ValueError("Name cannot be an empty string.")
    print(f"Hello, {name}!")

# Function to demonstrate best practices
def process_data():
    try:
        print(check_positive_number(10))  # Should print 10
        print(check_positive_number(-5))  # Should raise NegativeValueError
    except NegativeValueError as e:
        logging.error(f"NegativeValueError: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    else:
        print("All numbers are positive.")
    finally:
        print("Finished processing numbers.")

    try:
        greet("Alice")  # Should print "Hello, Alice!"
        greet(123)      # Should raise NotAStringError
    except NotAStringError as e:
        logging.error(f"NotAStringError: {e}")
    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    else:
        print("All greetings were successful.")
    finally:
        print("Finished processing greetings.")

# Run the function
if __name__ == "__main__":
    process_data()