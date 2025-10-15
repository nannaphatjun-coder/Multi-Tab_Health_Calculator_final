"""
This file defines the Gradio user interface for the health calculator.
"""
import gradio as gr
from data import food_calories, activity_levels
from calculations import calculate_bmi, calculate_tdee, add_food_to_log, reset_log, compare_calories

# --- Custom CSS for Styling ---
# It's better to move this to a separate styles.css file in a real project
# and load it with gr.Blocks(css="styles.css"). For simplicity here, we keep it.
custom_css = """
:root {
    --primary-hue: 318deg; /* For #582C4D */
    --primary-hue-dark: 318deg;
    --primary-hue-light: 318deg;
    --text-color: #ECE2D0;
    --body-background-fill: #BE92A2;
    --background-fill-primary: #D5B9B2;
    --background-fill-secondary: #D5B9B2;
    --button-primary-background-fill: #582C4D;
    --button-primary-background-fill-hover: #6a3a5c;
    --button-primary-text-color: #ECE2D0;
    --slider-color: #582C4D;
}
body {
    background-color: var(--body-background-fill);
    color: var(--text-color);
}
.gradio-container {
    background: var(--body-background-fill);
}
.gr-panel, .gr-box {
    background-color: var(--background-fill-primary) !important;
}
.gr-input {
    background-color: #ffffff; /* White background for better readability */
}
h1, h2, h3, label, p, .gr-button {
    color: var(--text-color) !important;
}
footer {
    display: none !important;
}
"""

def create_interface():
    """Builds and returns the Gradio app interface."""
    with gr.Blocks(css=custom_css, title="Health Calculator") as demo:
        gr.Markdown("# Modern Health & Fitness Calculator")

        # Shared state for TDEE and calorie log
        calorie_log_total = gr.State(0)

        with gr.Tabs():
            # --- Tab 1: BMI Calculator ---
            with gr.TabItem("BMI Calculator"):
                with gr.Row():
                    with gr.Column():
                        gr.Markdown("## Calculate Your Body Mass Index")
                        height_input = gr.Number(label="Height", value=170)
                        height_unit_input = gr.Radio(["cm", "inches"], label="Height Unit", value="cm")
                        weight_input = gr.Number(label="Weight", value=65)
                        weight_unit_input = gr.Radio(["kg", "lbs"], label="Weight Unit", value="kg")
                        bmi_btn = gr.Button("Calculate BMI")
                    with gr.Column():
                        gr.Markdown("## Your Result")
                        bmi_output_html = gr.HTML()

                # Hidden outputs
                bmi_output_value = gr.Textbox(label="BMI Value", visible=False)
                bmi_output_category = gr.Textbox(label="BMI Category", visible=False)

            # --- Tab 2: Daily Metabolic Rate Calculator ---
            with gr.TabItem("Daily Calorie Needs (BMR & TDEE)"):
                with gr.Row():
                    with gr.Column():
                        gr.Markdown("## Calculate Your Daily Energy Expenditure")
                        age_input = gr.Slider(2, 100, value=30, step=1, label="Age")
                        gender_input = gr.Radio(["Male", "Female"], label="Gender", value="Male")
                        bmr_height_input = gr.Number(label="Height (cm)", value=170)
                        bmr_weight_input = gr.Number(label="Weight (kg)", value=65)
                        activity_level_input = gr.Dropdown(
                            list(activity_levels.keys()),
                            label="Activity Level",
                            value="Lightly active (light exercise/sports 1-3 days/week)"
                        )
                        tdee_btn = gr.Button("Calculate Calorie Needs")
                    with gr.Column():
                        gr.Markdown("## Your Results")
                        bmr_output = gr.Textbox(label="Basal Metabolic Rate (BMR)")
                        tdee_output = gr.Textbox(label="Total Daily Energy Expenditure (TDEE)")
                        gr.Markdown("### Calorie Goals for Weight Management")
                        goals_output = gr.Markdown()

            # --- Tab 3: Food Tracker ---
            with gr.TabItem("Food Calorie Tracker"):
                with gr.Row():
                    with gr.Column(scale=2):
                        gr.Markdown("## Log Your Daily Food Intake")
                        tdee_input_for_tracker = gr.Number(label="Enter Your TDEE (from Tab 2)", info="This helps compare your intake to your goal.")
                        food_dropdown = gr.Dropdown(list(food_calories.keys()), label="Select a Food Item")
                        manual_calories_input = gr.Number(label="Or Enter Calories Manually", value=0)
                        add_food_btn = gr.Button("Add to Daily Log")
                        reset_log_btn = gr.Button("Reset Daily Log")
                    with gr.Column(scale=1):
                        gr.Markdown("## Today's Summary")
                        daily_total_display = gr.Label("Daily Total: 0 kcal")
                        comparison_output = gr.Textbox(label="Comparison to TDEE Goal", interactive=False)

        # --- Event Handlers ---
        bmi_btn.click(
            fn=calculate_bmi,
            inputs=[height_input, weight_input, height_unit_input, weight_unit_input],
            outputs=[bmi_output_value, bmi_output_category, bmi_output_html]
        )

        tdee_btn.click(
            fn=calculate_tdee,
            inputs=[age_input, gender_input, bmr_height_input, bmr_weight_input, activity_level_input],
            outputs=[bmr_output, tdee_output, goals_output]
        )

        add_food_btn.click(
            fn=add_food_to_log,
            inputs=[food_dropdown, manual_calories_input, calorie_log_total],
            outputs=[calorie_log_total, daily_total_display]
        ).then(
            fn=compare_calories,
            inputs=[calorie_log_total, tdee_input_for_tracker],
            outputs=[comparison_output]
        )

        tdee_input_for_tracker.change(
            fn=compare_calories,
            inputs=[calorie_log_total, tdee_input_for_tracker],
            outputs=[comparison_output]
        )

        reset_log_btn.click(
            fn=reset_log,
            inputs=[],
            outputs=[calorie_log_total, daily_total_display]
        ).then(
            fn=compare_calories,
            inputs=[calorie_log_total, tdee_input_for_tracker],
            outputs=[comparison_output]
        )
    return demo
