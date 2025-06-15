# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Step 1: Attempt to convert inputs to float.
        # This will raise a ValueError if inputs are not numeric.
        num = float(numerator)
        den = float(denominator)

        # Step 2: Handle division by zero.
        # This will raise a ZeroDivisionError if denominator is 0.
        if den == 0:
            return "Error: Cannot divide by zero."

        # Step 3: Perform division if no errors occurred.
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Catch errors specifically for non-numeric inputs during float conversion.
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Although we explicitly check for den == 0,
        # it's good practice to also catch ZeroDivisionError
        # as a fallback or for different scenarios.
        return "Error: Cannot divide by zero."
    except Exception as e:
        # Catch any other unexpected errors.
        return f"An unexpected error occurred: {e}"