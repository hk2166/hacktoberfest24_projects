def calculate_bmi(height, weight):
    """
    Calculate the Body Mass Index (BMI) based on height and weight.

    Args:
        height (float): The height in meters.
        weight (float): The weight in kilograms.

    Returns:
        float: The calculated BMI.
    """
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive numbers")

    bmi = weight / (height ** 2)
    return round(bmi, 2)  # Round to 2 decimal places

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Healthy"
    elif 24.9 <= bmi < 30:
        return "Overweight"
    else:
        return "Suffering from Obesity"

# Driver Code
if __name__ == "__main__":
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))

        bmi = calculate_bmi(height, weight)
        category = get_bmi_category(bmi)

        print(f"Your BMI is: {bmi}")
        print(f"Your BMI category is: {category}")
    except ValueError as e:
        print(f"Error: {e}")
