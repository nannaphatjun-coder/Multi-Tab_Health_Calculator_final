# Multi-Tab Health & Fitness Calculator

A user-friendly, all-in-one web application designed to help you track and manage key aspects of your health and fitness journey. This tool is built using Python and the Gradio library to provide a clean, interactive, multi-tab interface.

An interactive health application for calculating BMI and tracking daily calories, created by Nannaphat Juntasaro 6813373 and Prawichta Saesow 6813378.



## ✨ Features

This application is organized into three distinct tabs for ease of use:

### 1.  BMI Calculator
* **Calculate Your Body Mass Index (BMI):** Quickly determine your BMI based on your height and weight.
* **Unit Flexibility:** Supports both metric (cm, kg) and imperial (inches, lbs) units.
* **Visual Feedback:** Displays your BMI value along with a clear, color-coded category (Underweight, Normal weight, Overweight, Obese) for an immediate understanding of your result.

### 2. Daily Calorie Needs (BMR & TDEE)
* **Estimate Your Metabolism:** Calculates your Basal Metabolic Rate (BMR), the number of calories your body needs at rest.
* **Personalized Energy Calculation:** Determines your Total Daily Energy Expenditure (TDEE) by factoring in your age, gender, height, weight, and daily activity level.
* **Set Your Goals:** Provides tailored daily calorie suggestions for different weight management goals, including mild weight loss, significant weight loss, maintenance, and weight gain.

### 3. Food Calorie Tracker
* **Log Your Meals:** Easily track your daily calorie intake.
* **Pre-populated Food List:** Select from a dropdown menu of common foods and popular Thai dishes with pre-calculated calorie counts.
* **Manual Entry:** Flexibility to manually enter the calorie amount for items not on the list.
* **Goal Comparison:** Enter your TDEE from the second tab to see a real-time comparison of your calorie consumption against your daily goal.

## 🛠️ Technologies Used

* **Backend:** Python
* **Web UI:** Gradio

## 🚀 Getting Started

To run this application on your local machine, follow these simple steps.

### Prerequisites

Make sure you have Python 3 installed on your system.

### Installation

1.  Clone this repository or download the source code files.
2.  Install the necessary Python library:
    ```bash
    pip install gradio
    ```

### Running the Application

1.  Navigate to the directory where your script is located.
2.  Run the application from your terminal:
    ```bash
    python your_file_name.py
    ```
3.  The application will start, and a local URL (e.g., `http://127.0.0.1:7860`) will be displayed in the terminal. Open this URL in your web browser to use the calculator.

## 📝 Code Overview

The script is structured into three main parts:

1.  **Data Dictionaries:**
    * `food_calories`: A dictionary containing a wide range of food items and their corresponding calorie values.
    * `activity_levels`: A dictionary that maps descriptive activity levels to their multiplier values for TDEE calculation.
2.  **Calculation Logic:**
    * Separate Python functions are defined for each calculation: `calculate_bmi`, `calculate_tdee`, and the food tracker functions (`add_food_to_log`, `reset_log`, `compare_calories`).
3.  **Gradio Interface:**
    * The main `gr.Blocks()` section defines the entire user interface, including the tabs, input fields (sliders, radio buttons, dropdowns), buttons, and output displays. It also handles all event listeners that connect the UI components to the backend logic.
