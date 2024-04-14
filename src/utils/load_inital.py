import tkinter as tk
import yaml
from tkinter import messagebox

# Function to load initial functions from YAML file
def load_initial_functions():
    try:
        # Attempt to open and read the initial functions YAML file
        with open("data/initial_functions.yaml", "r") as file:
            return yaml.safe_load(file)  # Safely load YAML content
    except FileNotFoundError:
        # Show an error message if the file is not found
        messagebox.showerror("Error", "Initial functions YAML file not found.")
        return {}
    except yaml.YAMLError as e:
        # Show an error message if there's an error loading the YAML file
        messagebox.showerror("Error", f"Error loading initial functions YAML file: {e}")
        return {}

# Function to load initial templates from YAML file
def load_initial_templates():
    try:
        # Attempt to open and read the initial document templates YAML file
        with open("data/initial_document_templates.yaml", "r") as file:
            return yaml.safe_load(file)  # Safely load YAML content
    except FileNotFoundError:
        # Show an error message if the file is not found
        messagebox.showerror("Error", "Initial Document Templates YAML file not found.")
        return {}
    except yaml.YAMLError as e:
        # Show an error message if there's an error loading the YAML file
        messagebox.showerror("Error", f"Error loading Initial Document Templates YAML file: {e}")
        return {}
