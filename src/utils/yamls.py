from tkinter import filedialog, messagebox
import yaml

# Function to load functions from a YAML file
def load_functions_from_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", f"YAML file '{file_path}' not found.")
        return {}
    except yaml.YAMLError as e:
        messagebox.showerror("Error", f"Error loading YAML file '{file_path}': {e}")
        return {}

# Function to load documents from a YAML file
def load_documents_from_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", f"YAML file '{file_path}' not found.")
        return {}
    except yaml.YAMLError as e:
        messagebox.showerror("Error", f"Error loading YAML file '{file_path}': {e}")
        return {}

# Function to save functions to a YAML file
def save_functions_to_yaml(functions, file_path):
    try:
        with open(file_path, "w") as file:
            yaml.dump(functions, file)
        messagebox.showinfo("Success", f"Functions saved to '{file_path}' successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving functions: {str(e)}")

# Function to save documents to a YAML file
def save_documents_to_yaml(documents, file_path):
    try:
        with open(file_path, "w") as file:
            yaml.dump(documents, file)
        messagebox.showinfo("Success", f"Documents saved to '{file_path}' successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving documents: {str(e)}")

# Function to import functions from a YAML file
def import_functions(app):
    file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml")])
    if file_path:
        new_functions = load_functions_from_yaml(file_path)
        if new_functions:
            app.functions.update(new_functions)
            messagebox.showinfo("Success", "Functions imported successfully.")
            # Update UI or perform other actions as needed
        else:
            messagebox.showwarning("Warning", "No functions were found in the selected YAML file.")

# Function to import documents from a YAML file
def import_templates(app):
    file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml")])
    if file_path:
        new_documents = load_documents_from_yaml(file_path)
        if new_documents:
            app.documents.update(new_documents)
            messagebox.showinfo("Success", "Document Templates imported successfully.")
        else:
            messagebox.showwarning("Warning", "No documents were found in the selected YAML file.")

# Function to export functions to a YAML file
def export_functions(app):
    file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
    if file_path:
        save_functions_to_yaml(app.functions, file_path)

# Function to export documents to a YAML file
def export_documents(app):
    file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
    if file_path:
        save_documents_to_yaml(app.documents, file_path)
