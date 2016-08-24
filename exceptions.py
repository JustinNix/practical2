"""1. A ValueError will occur when the user enters something that is NaN
   2. A ZeroDivisionError will occur when the user tries to divide by zero
   3. Have an error checking function which keeps asking the user for a denominator until it is > or < 0."""

try:
 numerator = int(input("Enter the numerator: "))
 denominator = int(input("Enter the denominator: "))
 fraction = numerator / denominator
except ValueError:
 print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
 print("Cannot divide by zero!")
print("Finished.")
