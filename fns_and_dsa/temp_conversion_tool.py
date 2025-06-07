FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
        
        celsius_input = float(input("Enter temperature in Celsius: "))
        fahrenheit_result = convert_to_fahrenheit(celsius_input)
        print(f"{celsius_input}°C is {fahrenheit_result:.2f}°F")
        
    except ValueError:
        print("Please enter a valid number for the temperature.")

if __name__ == "__main__":
    main()