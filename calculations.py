"""
This file contains the core logic for all health-related calculations.
"""
from data import activity_levels, food_calories

# --- BMI Calculator Logic ---
def calculate_bmi(height, weight, height_unit, weight_unit):
    if not height or not weight:
        return "Please enter height and weight.", "", ""

    # Convert to metric
    if height_unit == "inches":
        height_m = height * 0.0254
    else:  # cm
        height_m = height / 100

    if weight_unit == "lbs":
        weight_kg = weight * 0.453592
    else:  # kg
        weight_kg = weight

    if height_m == 0:
        return "Height cannot be zero.", "", ""

    bmi = weight_kg / (height_m ** 2)
    bmi_rounded = round(bmi, 1)

    # Determine category
    if bmi < 18.5:
        category = "Underweight"
        color = "lightblue"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        color = "lightgreen"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "gold"
    else:
        category = "Obese"
        color = "lightcoral"

    result_html = f"""
    <div style='text-align: center; padding: 20px; border-radius: 10px; background-color: {color};'>
        <p style='font-size: 1.2em; color: #000;'>Your BMI is</p>
        <p style='font-size: 2.5em; font-weight: bold; color: #000;'>{bmi_rounded}</p>
        <p style='font-size: 1.2em; color: #000;'>Category: {category}</p>
    </div>
    """
    return f"{bmi_rounded}", category, result_html

# --- BMR & TDEE Calculator Logic ---
def calculate_tdee(age, gender, height, weight, activity_level):
    if not all([age, gender, height, weight, activity_level]):
        return "Please fill all fields.", "", ""

    # Harris-Benedict Equation for BMR
    if gender == "Male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # Female
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    tdee = bmr * activity_levels[activity_level]

    bmr_rounded = round(bmr)
    tdee_rounded = round(tdee)

    goals = (
        f"**Maintain weight:** {tdee_rounded} kcal/day\n"
        f"**Mild weight loss (0.25 kg/week):** {tdee_rounded - 250} kcal/day\n"
        f"**Weight loss (0.5 kg/week):** {tdee_rounded - 500} kcal/day\n"
        f"**Mild weight gain (0.25 kg/week):** {tdee_rounded + 250} kcal/day\n"
        f"**Weight gain (0.5 kg/week):** {tdee_rounded + 500} kcal/day\n"
    )
    return f"{bmr_rounded} kcal/day", f"{tdee_rounded} kcal/day", goals

# --- Food Tracker Logic ---
def add_food_to_log(food_item, manual_calories, current_total):
    calories_to_add = 0
    if food_item and food_item in food_calories:
        calories_to_add = food_calories[food_item]
    elif manual_calories > 0:
        calories_to_add = manual_calories

    new_total = current_total + calories_to_add
    return new_total, f"Daily Total: {new_total} kcal"

def reset_log():
    return 0, "Daily Total: 0 kcal"

def compare_calories(daily_total, tdee_input):
    if not tdee_input:
        return "Enter your TDEE from Tab 2 to see a comparison."

    try:
        tdee_value = float(str(tdee_input).split()[0])
        difference = daily_total - tdee_value
        if difference > 0:
            return f"You are {abs(round(difference))} kcal OVER your daily goal."
        elif difference < 0:
            return f"You are {abs(round(difference))} kcal UNDER your daily goal."
        else:
            return "You have met your daily goal exactly!"
    except (ValueError, IndexError):
        return "Invalid TDEE format. Please enter a number (e.g., '2000')."
