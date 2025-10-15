"""
Main entry point for the Health & Fitness Calculator application.

This script imports the user interface, creates the Gradio app,
and launches it.
"""
from interface import create_interface

if __name__ == "__main__":
    # Create the Gradio interface from our interface definition
    demo = create_interface()
    
    # Launch the application
    demo.launch()
