"""
This file contains the core logic for all health-related calculations.
All functions for BMI, BMR, TDEE, and food tracking are here.
"""
from data import activity_levels, food_calories

# --- BMI Calculator Logic ---
def calculate_bmi(height, weight, height_unit, weight_unit):
    if not height or not weight:
        return "", "", "<p style='color:red;'>Please enter both height and weight.</p>"
    try:
        height, weight = float(height), float(weight)
    except (ValueError, TypeError):
        return "", "", "<p style='color:red;'>Invalid input. Please enter numbers.</p>"
    
    if height <= 0 or weight <= 0:
        return "", "", "<p style='color:red;'>Height and weight must be positive numbers.</p>"

    # Convert to metric for calculation
    if height_unit == "inches":
        height_m = height * 0.0254
    else:  # cm
        height_m = height / 100
    if weight_unit == "lbs":
        weight_kg = weight * 0.453592
    else:  # kg
        weight_kg = weight

    bmi = weight_kg / (height_m ** 2)
    bmi_rounded = round(bmi, 1)

    # Determine category and color
    if bmi < 18.5:
        category, color = "Underweight", "#A7C7E7"  # Pastel Blue
    elif 18.5 <= bmi < 25:
        category, color = "Normal weight", "#C1E1C1"  # Pastel Green
    elif 25 <= bmi < 30:
        category, color = "Overweight", "#FDFD96"  # Pastel Yellow
    else:
        category, color = "Obese", "#FFB347"  # Pastel Orange

    result_html = f"""
    <div style='text-align: center; padding: 20px; border-radius: 15px; background-color: {color};'>
        <p style='font-size: 1.2em; color: #333;'>Your BMI is</p>
        <p style='font-size: 2.5em; font-weight: bold; color: #000;'>{bmi_rounded}</p>
        <p style='font-size: 1.2em; color: #333;'>Category: {category}</p>
    </div>
    """
    return str(bmi_rounded), category, result_html

# --- BMR & TDEE Calculator Logic ---
def calculate_tdee(age, gender, height, weight, activity_level):
    if not all([age, gender, height, weight, activity_level]):
        return "Please fill all fields.", "", ""
    try:
        age, height, weight = float(age), float(height), float(weight)
    except (ValueError, TypeError):
         return "Invalid input. Please use numbers.", "", ""

    # Harris-Benedict Equation for BMR (revised)
    if gender == "Male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # Female
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    tdee = bmr * activity_levels[activity_level]
    bmr_rounded, tdee_rounded = int(bmr), int(tdee)

    goals = (
        f"**Maintain weight:** `{tdee_rounded}` kcal/day\n\n"
        f"**Mild weight loss (0.25 kg/week):** `{tdee_rounded - 250}` kcal/day\n\n"
        f"**Weight loss (0.5 kg/week):** `{tdee_rounded - 500}` kcal/day\n\n"
        f"**Mild weight gain (0.25 kg/week):** `{tdee_rounded + 250}` kcal/day\n\n"
        f"**Weight gain (0.5 kg/week):** `{tdee_rounded + 500}` kcal/day"
    )
    return f"{bmr_rounded} kcal/day", f"{tdee_rounded} kcal/day", goals

# --- Food Tracker Logic ---
def add_food_to_log(food_item, manual_calories, current_total):
    calories_to_add = 0
    try:
        manual_calories = float(manual_calories) if manual_calories else 0
    except (ValueError, TypeError):
        manual_calories = 0
    
    if food_item and food_item in food_calories:
        calories_to_add = food_calories[food_item]
    elif manual_calories > 0:
        calories_to_add = manual_calories

    new_total = current_total + calories_to_add
    return new_total, f"Daily Total: {int(new_total)} kcal"

def reset_log():
    return 0, "Daily Total: 0 kcal"

def compare_calories(daily_total, tdee_input):
    if not tdee_input:
        return "Enter your TDEE from Tab 2."
    try:
        tdee_value = float(tdee_input)
        difference = daily_total - tdee_value
        if difference > 0:
            return f"You are {abs(int(difference))} kcal OVER your goal."
        elif difference < 0:
            return f"You are {abs(int(difference))} kcal UNDER your goal."
        else:
            return "You have met your daily goal exactly!"
    except (ValueError, TypeError):
        return "Invalid TDEE. Please enter a number."
