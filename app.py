
def calculate_bmi(weight, height):
    """
    BMI Formula = weight (kg) / (height (m) ** 2)
    """
    return weight / (height ** 2)

def bmi_category(bmi):
    """
    Categorization of BMI values.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the WWD BMI Calculator!")
    try:
        # Get user input for weight and height
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        # Validate inputs
        if weight <= 0 or height <= 0:
            print("Please enter appropriate values. Weight & height must be greater than 1.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Display results
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {bmi_category(bmi)}")

    except ValueError:
        print("Please enter numerical values for weight & height greater than 1.")

if __name__ == "__main__":
    main()
