"""
This file contains static data used by the health calculator.
It holds the dictionaries for food calories and activity levels.
"""

# Dictionary of food items and their approximate calorie counts.
food_calories = {
    "Apple (1 medium)": 95,
    "Banana (1 medium)": 105,
    "Boiled Egg (1 large)": 70,
    "White Rice (1 cup cooked)": 200,
    "Brown Rice (1 cup cooked)": 215,
    "Chicken Breast (100g, cooked)": 165,
    "Beef (100g, cooked)": 250,
    "Salmon (100g, cooked)": 210,
    "Tofu (100g, firm)": 145,
    "Broccoli (1 cup cooked)": 55,
    "Carrot (1 medium)": 25,
    "Potato (1 medium, boiled)": 160,
    "Sweet Potato (1 medium, baked)": 100,
    "Almonds (28g / ~23 pcs)": 160,
    "Peanut Butter (1 tbsp)": 95,
    "Milk (1 cup, whole)": 150,
    "Yogurt (plain, 1 cup)": 100,
    "Cheddar Cheese (28g / 1 oz)": 115,
    "Bread (1 slice, white)": 80,
    "Pasta (1 cup cooked)": 220,
    "Pad Thai (Chicken)": 450,
    "Green Curry with Chicken and Rice": 600,
    "Tom Yum Goong": 250,
    "Massaman Curry with Beef and Rice": 700,
    "Pad Kra Pao with Rice and Egg": 600,
    "Som Tum": 150,
    "Khao Pad (Chicken Fried Rice)": 550,
    "Khao Soi": 650,
    "Larb (Chicken)": 250,
    "Panang Curry with Chicken and Rice": 600,
    "Satay (3 Chicken Skewers)": 200,
    "Thai Spring Rolls (2 pcs)": 250,
    "Moo Ping (2 Skewers)": 220,
    "Sticky Rice with Mango": 400,
    "Thai Coconut Ice Cream (1 scoop)": 300,
    "Yum Woon Sen (Glass Noodle Salad)": 200,
    "Gai Tod (Fried Chicken)": 300,
    "Khanom Krok (Coconut Pancakes, 4 pcs)": 250,
    "Pad See Ew (Stir-Fried Flat Noodles with Pork)": 550,
    "Gaeng Daeng (Red Curry with Chicken and Rice)": 600,
}

# Dictionary mapping activity levels to their corresponding multipliers for TDEE calculation.
activity_levels = {
    "Sedentary (little or no exercise)": 1.2,
    "Lightly active (light exercise/sports 1-3 days/week)": 1.375,
    "Moderately active (moderate exercise/sports 3-5 days/week)": 1.55,
    "Very active (hard exercise/sports 6-7 days a week)": 1.725,
    "Super active (very hard exercise/physical job)": 1.9,
}
