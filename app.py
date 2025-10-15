"""
Main entry point for the Health & Fitness Calculator application.

This script imports the user interface from interface.py, creates the 
Gradio app, and launches it. This file does not need to be edited.
"""
from interface import create_interface

# This is the main execution block
if __name__ == "__main__":
    # Create the Gradio interface from our interface definition
    demo = create_interface()
    
    # Launch the application
    # Set share=False if you only want to run it locally.
    demo.launch()
