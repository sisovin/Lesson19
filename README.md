# Chapter 19 - Exceptions & Errors

## Learn Python fast with some content ideas

Learning Python is a great choice, especially given your interest in web development, mobile app development, and software engineering. Here are some excellent resources to get you started:

**1. LearnPython.org:** This interactive Python tutorial offers free lessons for beginners. It covers topics like variables, loops, functions, and more. You can even get certified after completing the [`tutorials[1]`](https://www.learnpython.org/).

**2. Python Official Documentation:** The official Python documentation provides comprehensive information about the language. Start with the Python Tutorial for beginners and explore further as you gain [`confidence[2]`](https://stackoverflow.com/questions/70577/best-online-resource-to-learn-python).

**3. freeCodeCamp’s Python Courses:**
**- [`Full Course for Beginners`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/):** This YouTube course covers programming basics, including lists, conditionals, strings, and small projects like a calculator and a guessing game.
**- [`The Ultimate Python Beginner’s Handbook`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/)** Dive deeper into Python concepts and explore its growing popularity [`3`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/) and [`4`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/).

**REMEMBER:** practice coding regularly, work on small projects, and explore real-world examples.

## What is Chapter 19 - Exceptions & Errors in Python?

Chapter 19 - Exceptions & Errors in Python typically covers the following topics:

1. **Introduction to Exceptions**:

   - What exceptions are and why they are used.
   - Difference between syntax errors and exceptions.

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

2. **Handling Exceptions**:

   - Using `try`, `except`, `else`, and `finally` blocks.
   - Multiple `except` clauses.
   - Catching specific exceptions.
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

print(divide(10, 2)) # Should print the result and "Division successful."
print(divide(10, 0)) # Should print "Error: Division by zero is not allowed."
print(divide(10, 'a')) # Should print "Error: Both arguments must be numbers."

3. **Raising Exceptions**:

   - Using the `raise` statement to trigger exceptions.
   - Custom exceptions by subclassing the `Exception` class.
     Certainly! Here is an example of how to raise exceptions in Python, using the provided context from your file:

```python
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
```

### Explanation:

1. **`check_positive_number` Function**:
   - Raises a `ValueError` if the input value is negative.
2. **`greet` Function**:
   - Raises a `TypeError` if the input name is not a string.
   - Raises a `ValueError` if the input name is an empty string.
3. **Example Usage**:
   - Demonstrates how to call these functions and handle the raised exceptions using `try` and `except` blocks.

This example shows how to raise exceptions to enforce certain conditions and how to handle these exceptions gracefully.

4. **Built-in Exceptions**:

   - Common built-in exceptions like `ValueError`, `TypeError`, `IndexError`, etc.
   - Understanding the exception hierarchy.
     Built-in exceptions in Python are a set of predefined exceptions that are provided by the Python standard library. These exceptions cover a wide range of error conditions that can occur during the execution of a program. Here are some common built-in exceptions:

1. **`Exception`**: Base class for all exceptions.
1. **`AttributeError`**: Raised when an attribute reference or assignment fails.
1. **`ImportError`**: Raised when an import statement fails to find the module definition or when a `from ... import` fails.
1. **`IndexError`**: Raised when a sequence subscript is out of range.
1. **`KeyError`**: Raised when a dictionary key is not found.
1. **`NameError`**: Raised when a local or global name is not found.
1. **[`TypeError`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fchien%2F.vscode%2Fextensions%2Fms-python.vscode-pylance-2024.7.1%2Fdist%2Ftypeshed-fallback%2Fstdlib%2Fbuiltins.pyi%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A1935%2C%22character%22%3A6%7D%5D 'c:/Users/chien/.vscode/extensions/ms-python.vscode-pylance-2024.7.1/dist/typeshed-fallback/stdlib/builtins.pyi')**: Raised when an operation or function is applied to an object of inappropriate type.
1. **[`ValueError`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fchien%2F.vscode%2Fextensions%2Fms-python.vscode-pylance-2024.7.1%2Fdist%2Ftypeshed-fallback%2Fstdlib%2Fbuiltins.pyi%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A1936%2C%22character%22%3A6%7D%5D 'c:/Users/chien/.vscode/extensions/ms-python.vscode-pylance-2024.7.1/dist/typeshed-fallback/stdlib/builtins.pyi')**: Raised when a function receives an argument of the correct type but inappropriate value.
1. **`FileNotFoundError`**: Raised when a file or directory is requested but doesn’t exist.
1. **[`ZeroDivisionError`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fchien%2F.vscode%2Fextensions%2Fms-python.vscode-pylance-2024.7.1%2Fdist%2Ftypeshed-fallback%2Fstdlib%2Fbuiltins.pyi%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A1939%2C%22character%22%3A6%7D%5D 'c:/Users/chien/.vscode/extensions/ms-python.vscode-pylance-2024.7.1/dist/typeshed-fallback/stdlib/builtins.pyi')**: Raised when the second argument of a division or modulo operation is zero.

### Example Usage of Built-in Exceptions

Here is an example demonstrating how some of these built-in exceptions can be used:

```python
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
try:
    import non_existent_module
except ImportError as e:
    print(f"ImportError: {e}")

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
try:
    print(undefined_variable)
except NameError as e:
    print(f"NameError: {e}")

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
```

This example demonstrates how to handle various built-in exceptions in Python, providing a clear understanding of how each exception can be caught and managed.

5. **Exception Propagation**:

   - How exceptions propagate through the call stack.
   - Using `traceback` to understand the source of exceptions.
     Exception propagation refers to the process by which an exception is passed up the call stack until it is caught by an appropriate exception handler. If no handler is found, the program terminates. Here's an example demonstrating how to use exception propagation with the custom exceptions defined in your [`exceptions.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson19%2Fexceptions.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D 'd:\\learnPython\Lesson19\exceptions.py') file:

### Step-by-Step Plan:

1. Define a function that calls another function which might raise an exception.
2. In the calling function, do not handle the exception, allowing it to propagate up the call stack.
3. In the main function or higher-level function, catch and handle the exception.

### Example Code:

```python
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
```

### Explanation:

1. **Function Definitions**:

   - `process_number(value)`: Calls `check_positive_number(value)` and lets any exceptions propagate.
   - `process_greeting(name)`: Calls `greet(name)` and lets any exceptions propagate.

2. **Main Function**:

   - `main()`: Calls `process_number` and `process_greeting` within `try` blocks to catch and handle exceptions.
   - Handles `NegativeValueError`, `NotAStringError`, and `ValueError` exceptions.

3. **Running the Main Function**:
   - The `main()` function is called if the script is executed directly.

This example demonstrates how exceptions can propagate up the call stack and be caught at a higher level, allowing for centralized exception handling.

6. **Assertions**:

   - Using `assert` statements for debugging and testing.
     Assertions are a debugging aid that tests a condition as an internal self-check in your program. They help catch bugs by verifying that certain conditions hold true. If an assertion fails, an `AssertionError` is raised, which can help identify issues early in the development process.

Here's how you can use assertions in your code:

### Step-by-Step Plan:

1. Define conditions that should always be true at a certain point in your code.
2. Use the `assert` statement to check these conditions.
3. If the condition is `False`, an `AssertionError` is raised with an optional error message.

### Example Code:

```python
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
```

### Explanation:

1. **Function with Assertion**:

   - `divide(a, b)`: Uses an assertion to ensure that the divisor `b` is not zero. If `b` is zero, an `AssertionError` is raised with the message "Division by zero is not allowed."

2. **Test Function**:

   - `test_assertions()`: Tests the `divide` function with valid and invalid inputs.
   - The first call to `divide(10, 2)` should pass and print the result.
   - The second call to `divide(10, 0)` should fail and raise an `AssertionError`, which is caught and printed.

3. **Running the Test Function**:
   - The `test_assertions()` function is called if the script is executed directly.

This example demonstrates how to use assertions to enforce conditions that should always be true, helping to catch bugs early in the development process.

7. **Best Practices**:

   - Writing clean and maintainable exception handling code.
   - Avoiding overuse of exceptions for control flow.
     Certainly! Here are some best practices for handling exceptions in Python:

### Best Practices for Handling Exceptions

1. **Use Specific Exceptions**:

   - Catch specific exceptions rather than a generic `Exception` to avoid masking other unexpected errors.

2. **Avoid Using Bare `except`**:

   - Always specify the exception type you are catching to avoid catching unexpected exceptions.

3. **Clean Up Resources with `finally`**:

   - Use the `finally` block to clean up resources, such as closing files or releasing locks, regardless of whether an exception was raised.

4. **Use `else` for Code That Should Run If No Exception Occurs**:

   - The `else` block can be used to run code that should only execute if no exceptions were raised in the `try` block.

5. **Log Exceptions**:

   - Use logging to record exceptions, which can help with debugging and monitoring.

6. **Raise Exceptions with Meaningful Messages**:

   - Provide informative error messages when raising exceptions to make debugging easier.

7. **Create Custom Exceptions for Your Application**:
   - Define custom exceptions to represent specific error conditions in your application.

### Example Code Demonstrating Best Practices:

```python
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
```

### Explanation:

1. **Logging Configuration**:

   - Configures logging to log errors.

2. **Custom Exceptions**:

   - Defines `CustomError`, `NegativeValueError`, and `NotAStringError` with meaningful messages.

3. **Example Functions**:

   - `check_positive_number` and `greet` raise custom exceptions for specific error conditions.

4. **Function Demonstrating Best Practices**:

   - `process_data` demonstrates catching specific exceptions, using `else` for code that runs if no exceptions occur, and using `finally` for cleanup.
   - Logs exceptions using the `logging` module.

5. **Running the Function**:
   - The `process_data()` function is called if the script is executed directly.

This example follows best practices for handling exceptions in Python, making the code more robust and easier to debug.

8. **how to create Custom Exceptions?**
   Certainly! Creating custom exceptions in Python involves defining a new class that inherits from the built-in `Exception` class or one of its subclasses. Here is an example of how to create and use custom exceptions:

```python
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
```

### Explanation:

1. **Define Custom Exceptions**:
   - `CustomError`: A base class for other custom exceptions.
   - `NegativeValueError`: Raised when a negative value is encountered.
   - `NotAStringError`: Raised when a non-string value is encountered.
2. **Example Functions**:

   - `check_positive_number`: Raises `NegativeValueError` if the input value is negative.
   - `greet`: Raises `NotAStringError` if the input name is not a string, and raises `ValueError` if the name is an empty string.

3. **Example Usage**:
   - Demonstrates how to call these functions and handle the custom exceptions using `try` and `except` blocks.

This example shows how to create custom exceptions to handle specific error conditions in your code, making your error handling more meaningful and easier to understand.

This chapter is essential for writing robust and error-resistant Python programs.

## What are some common built-in exceptions in Python?

Some common built-in exceptions in Python include:

1. **`Exception`**: Base class for all exceptions.
2. **`AttributeError`**: Raised when an attribute reference or assignment fails.
3. **`ImportError`**: Raised when an import statement fails to find the module definition or when a `from ... import` fails.
4. **`IndexError`**: Raised when a sequence subscript is out of range.
5. **`KeyError`**: Raised when a dictionary key is not found.
6. **`NameError`**: Raised when a local or global name is not found.
7. **`TypeError`**: Raised when an operation or function is applied to an object of inappropriate type.
8. **`ValueError`**: Raised when a function receives an argument of the correct type but inappropriate value.
9. **`FileNotFoundError`**: Raised when a file or directory is requested but doesn’t exist.
10. **`ZeroDivisionError`**: Raised when the second argument of a division or modulo operation is zero.

These exceptions help in identifying and handling errors in Python programs effectively.

## What are some best practices for handling exceptions in Python?

Some best practices for handling exceptions in Python include:

1. **Catch Specific Exceptions**:

   - Always catch specific exceptions rather than using a bare `except` clause.

   ```python
   try:
       # code that may raise an exception
   except ValueError:
       # handle ValueError
   ```

2. **Use `finally` for Cleanup**:

   - Use the `finally` block to ensure that cleanup code runs regardless of whether an exception occurred.

   ```python
   try:
       # code that may raise an exception
   finally:
       # cleanup code
   ```

3. **Avoid Swallowing Exceptions**:

   - Avoid catching exceptions without handling them or re-raising them.

   ```python
   try:
       # code that may raise an exception
   except SomeException as e:
       # handle exception or log it
       raise
   ```

4. **Log Exceptions**:

   - Log exceptions to help with debugging and monitoring.

   ```python
   import logging

   try:
       # code that may raise an exception
   except Exception as e:
       logging.error("An error occurred", exc_info=True)
   ```

5. **Use Custom Exceptions**:

   - Define custom exceptions for your application to make your error handling more meaningful.

   ```python
   class MyCustomError(Exception):
       pass

   try:
       # code that may raise an exception
   except MyCustomError as e:
       # handle custom exception
   ```

6. **Avoid Using Exceptions for Control Flow**:

   - Do not use exceptions to control the flow of your program. Use them for error handling only.

   ```python
   # Bad practice
   try:
       value = my_dict[key]
   except KeyError:
       value = default_value

   # Better practice
   value = my_dict.get(key, default_value)
   ```

7. **Document Exceptions**:

   - Document the exceptions that your functions can raise using docstrings.

   ```python
   def my_function():
       """
       Does something.

       Raises:
           ValueError: If an invalid value is provided.
       """
       pass
   ```

Following these best practices will help you write more robust and maintainable Python code.
