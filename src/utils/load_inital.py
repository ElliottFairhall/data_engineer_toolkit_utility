import tkinter as tk
import yaml
from tkinter import messagebox

# Function to load initial Pandas functions from YAML file
def load_initial_functions():
    try:
        # Attempt to open and read the initial Pandas functions YAML file
        with open("data/initial_functions.yaml", "r") as file:
            return yaml.safe_load(file)  # Safely load YAML content
    except FileNotFoundError:
        # Show an error message if the file is not found
        messagebox.showerror("Error", "Initial functions YAML file not found.")
        return {}
    except yaml.YAMLError as e:
        # Show an error message if there's an error loading the YAML file
        messagebox.showerror("Error", f"Error loading initial Pandas functions YAML file: {e}")
        return {}

# Function to load initial markdown templates from YAML file
def load_initial_templates():
    try:
        # Attempt to open and read the initial markdown document templates YAML file
        with open("data/initial_document_templates.yaml", "r") as file:
            return yaml.safe_load(file)  # Safely load YAML content
    except FileNotFoundError:
        # Show an error message if the file is not found
        messagebox.showerror("Error", "Initial Markdown Document Templates YAML file not found.")
        return {}
    except yaml.YAMLError as e:
        # Show an error message if there's an error loading the YAML file
        messagebox.showerror("Error", f"Error loading Initial Makrdown Document Templates YAML file: {e}")
        return {}

# Function to load initial SQL templates from YAML file
def load_initial_sql_templates():
    try:
        # Attempt to open and read the initial SQL document templates YAML file
        with open("data/inital_sql_snippets.yaml", "r") as file:
            return yaml.safe_load(file)  # Safely load YAML content
    except FileNotFoundError:
        # Show an error message if the file is not found
        messagebox.showerror("Error", "Initial SQL Templates YAML file not found.")
        return {}
    except yaml.YAMLError as e:
        # Show an error message if there's an error loading the YAML file
        messagebox.showerror("Error", f"Error loading Initial SQL Templates YAML file: {e}")
        return {}
    
# Function to load initial Confluence templates from YAML file
def load_initial_confluence_templates():
    try:
        # Attempt to open and read the initial Confluence document templates YAML file
        with open("data/inital_confluence_templates.yaml", "r") as file:
            return yaml.safe_load(file)  # Safely load YAML content
    except FileNotFoundError:
        # Show an error message if the file is not found
        messagebox.showerror("Error", "Initial Confluence Templates YAML file not found.")
        return {}
    except yaml.YAMLError as e:
        # Show an error message if there's an error loading the YAML file
        messagebox.showerror("Error", f"Error loading Initial Confluence Templates YAML file: {e}")
        return {}

# Function to load initial Seaborn templates from YAML file
def load_initial_seaborn_templates():
    try:
        # Attempt to open and read the initial Seaborn document templates YAML file
        with open("data/inital_seaborn_snippets.yaml", "r") as file:
            return yaml.safe_load(file)  # Safely load YAML content
    except FileNotFoundError:
        # Show an error message if the file is not found
        messagebox.showerror("Error", "Initial Seaborn Templates YAML file not found.")
        return {}
    except yaml.YAMLError as e:
        # Show an error message if there's an error loading the YAML file
        messagebox.showerror("Error", f"Error loading Initial Seaborn Templates YAML file: {e}")
        return {}

# Function to load initial Numpy templates from YAML file
def load_initial_numpy_templates():
    try:
        # Attempt to open and read the initial Seaborn document templates YAML file
        with open("data/inital_numpy_snippets.yaml", "r") as file:
            return yaml.safe_load(file)  # Safely load YAML content
    except FileNotFoundError:
        # Show an error message if the file is not found
        messagebox.showerror("Error", "Initial Numpy Templates YAML file not found.")
        return {}
    except yaml.YAMLError as e:
        # Show an error message if there's an error loading the YAML file
        messagebox.showerror("Error", f"Error loading Initial Numpy Templates YAML file: {e}")
        return {}