"""
This file defines the Gradio user interface for the health calculator.
It builds the tabs, inputs, and outputs and connects them to the logic.
"""
import gradio as gr
from data import food_calories, activity_levels
from calculations import calculate_bmi, calculate_tdee, add_food_to_log, reset_log, compare_calories

# --- Custom CSS for Styling ---
custom_css = """
body, .gradio-container { background-color: #F0E8F1; }
.gr-panel, .gr-box { background-color: #FFFFFF !important; border-radius: 15px !important; }
h1, h2, h3, label, p, .gr-button { color: #4A235A !important; }
.gr-button { background-color: #D6B0E0 !important; border: none !important; }
.gr-button:hover { background-color: #BE92A2 !important; }
footer { display: none !important; }
"""

def create_interface():
    """Builds and returns the Gradio app interface."""
    with gr.Blocks(theme=gr.themes.Soft(primary_hue="purple", secondary_hue="purple"), css=custom_css, title="Health Calculator") as demo:
        gr.Markdown("# All-in-One Health & Fitness Calculator")

        # Shared state for TDEE and calorie log
        calorie_log_total = gr.State(0)

        with gr.Tabs():
            # --- Tab 1: BMI Calculator ---
            with gr.TabItem("BMI Calculator"):
                with gr.Row(equal_height=True):
                    with gr.Column(scale=1):
                        gr.Markdown("## Calculate Your BMI")
                        height_input = gr.Number(label="Height", value=170)
                        height_unit_input = gr.Radio(["cm", "inches"], label="Height Unit", value="cm")
                        weight_input = gr.Number(label="Weight", value=65)
                        weight_unit_input = gr.Radio(["kg", "lbs"], label="Weight Unit", value="kg")
                        bmi_btn = gr.Button("Calculate BMI", variant="primary")
                    with gr.Column(scale=1):
                        gr.Markdown("## Your Result")
                        bmi_output_html = gr.HTML(elem_id="bmi_result")
                # Hidden outputs
                bmi_output_value = gr.Textbox(visible=False)
                bmi_output_category = gr.Textbox(visible=False)

            # --- Tab 2: Daily Metabolic Rate Calculator ---
            with gr.TabItem("Daily Calorie Needs"):
                with gr.Row():
                    with gr.Column():
                        gr.Markdown("## Calculate Your Daily Energy Needs")
                        age_input = gr.Slider(2, 100, value=30, step=1, label="Age")
                        gender_input = gr.Radio(["Male", "Female"], label="Gender", value="Male")
                        bmr_height_input = gr.Number(label="Height (cm)", value=170)
                        bmr_weight_input = gr.Number(label="Weight (kg)", value=65)
                        activity_level_input = gr.Dropdown(list(activity_levels.keys()), label="Activity Level", value="Lightly active (light exercise/sports 1-3 days/week)")
                        tdee_btn = gr.Button("Calculate Calorie Needs", variant="primary")
                    with gr.Column():
                        gr.Markdown("## Your Results")
                        bmr_output = gr.Textbox(label="Resting Calories (BMR)", interactive=False)
                        tdee_output = gr.Textbox(label="Total Daily Calories (TDEE)", interactive=False)
                        gr.Markdown("### Calorie Goals for Weight Management")
                        goals_output = gr.Markdown()

            # --- Tab 3: Food Tracker ---
            with gr.TabItem("Food Calorie Tracker"):
                with gr.Row():
                    with gr.Column(scale=2):
                        gr.Markdown("## Log Your Daily Food Intake")
                        tdee_input_for_tracker = gr.Number(label="Enter Your TDEE Goal (from Tab 2)", info="Helps compare intake to your goal.")
                        food_dropdown = gr.Dropdown(list(food_calories.keys()), label="Select a Food Item")
                        manual_calories_input = gr.Number(label="Or Enter Calories Manually", value=0)
                        add_food_btn = gr.Button("Add to Daily Log", variant="primary")
                        reset_log_btn = gr.Button("Reset Daily Log")
                    with gr.Column(scale=1):
                        gr.Markdown("## Today's Summary")
                        daily_total_display = gr.Label("Daily Total: 0 kcal")
                        comparison_output = gr.Textbox(label="Comparison to Goal", interactive=False)

        # --- Event Handlers ---
        bmi_btn.click(fn=calculate_bmi, inputs=[height_input, weight_input, height_unit_input, weight_unit_input], outputs=[bmi_output_value, bmi_output_category, bmi_output_html])
        tdee_btn.click(fn=calculate_tdee, inputs=[age_input, gender_input, bmr_height_input, bmr_weight_input, activity_level_input], outputs=[bmr_output, tdee_output, goals_output])

        def add_and_compare(food, manual_cal, total, tdee_goal):
            new_total, display_text = add_food_to_log(food, manual_cal, total)
            comparison = compare_calories(new_total, tdee_goal)
            return new_total, display_text, comparison
        add_food_btn.click(fn=add_and_compare, inputs=[food_dropdown, manual_calories_input, calorie_log_total, tdee_input_for_tracker], outputs=[calorie_log_total, daily_total_display, comparison_output])

        def reset_and_compare(tdee_goal):
            new_total, display_text = reset_log()
            comparison = compare_calories(new_total, tdee_goal)
            return new_total, display_text, comparison
        reset_log_btn.click(fn=reset_and_compare, inputs=[tdee_input_for_tracker], outputs=[calorie_log_total, daily_total_display, comparison_output])
        
        tdee_input_for_tracker.change(fn=compare_calories, inputs=[calorie_log_total, tdee_input_for_tracker], outputs=[comparison_output])
    return demo
