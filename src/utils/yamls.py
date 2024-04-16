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

# Function to load SQL code from a YAML file
def load_sql_from_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", f"YAML file '{file_path}' not found.")
        return {}
    except yaml.YAMLError as e:
        messagebox.showerror("Error", f"Error loading YAML file '{file_path}': {e}")
        return {}

# Function to load Confluence code from a YAML file
def load_confluence_from_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", f"YAML file '{file_path}' not found.")
        return {}
    except yaml.YAMLError as e:
        messagebox.showerror("Error", f"Error loading YAML file '{file_path}': {e}")
        return {}

# Function to load Seaborn code from a YAML file
def load_seaborn_from_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", f"YAML file '{file_path}' not found.")
        return {}
    except yaml.YAMLError as e:
        messagebox.showerror("Error", f"Error loading YAML file '{file_path}': {e}")
        return {}

# Function to load Numpy code from a YAML file
def load_numpy_from_yaml(file_path):
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

# Function to save SQL to a YAML file
def save_sql_to_yaml(documents, file_path):
    try:
        with open(file_path, "w") as file:
            yaml.dump(documents, file)
        messagebox.showinfo("Success", f"SQL snippets saved to '{file_path}' successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving SQL snippets: {str(e)}")

# Function to save Confluence to a YAML file
def save_confluence_to_yaml(documents, file_path):
    try:
        with open(file_path, "w") as file:
            yaml.dump(documents, file)
        messagebox.showinfo("Success", f"Confluence templates saved to '{file_path}' successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving Confluence templates: {str(e)}")

# Function to save Seaform to a YAML file
def save_seaborn_to_yaml(documents, file_path):
    try:
        with open(file_path, "w") as file:
            yaml.dump(documents, file)
        messagebox.showinfo("Success", f"Seaborn snippets saved to '{file_path}' successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving Seaborn snippets: {str(e)}")

# Function to save Numpy to a YAML file
def save_numpy_to_yaml(documents, file_path):
    try:
        with open(file_path, "w") as file:
            yaml.dump(documents, file)
        messagebox.showinfo("Success", f"Numpy snippets saved to '{file_path}' successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving Numpy snippets: {str(e)}")

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
            messagebox.showinfo("Success", "Markdown Templates imported successfully.")
        else:
            messagebox.showwarning("Warning", "No Markdown documents were found in the selected YAML file.")

# Function to import SQL snippets from a YAML file
def import_sql(app):
    file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml")])
    if file_path:
        new_sql = load_sql_from_yaml(file_path)
        if new_sql:
            app.sqls.update(new_sql)
            messagebox.showinfo("Success", "SQL snippets imported successfully.")
        else:
            messagebox.showwarning("Warning", "No SQL snippets were found in the selected YAML file.")

# Function to import Confluence templates from a YAML file
def import_confluence(app):
    file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml")])
    if file_path:
        new_confluence = load_confluence_from_yaml(file_path)
        if new_confluence:
            app.confluences.update(new_confluence)
            messagebox.showinfo("Success", "Confluence Templates imported successfully.")
        else:
            messagebox.showwarning("Warning", "No Confluence Templates were found in the selected YAML file.")

# Function to import Seaborn snippets from a YAML file
def import_seaborn(app):
    file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml")])
    if file_path:
        new_seaborn = load_seaborn_from_yaml(file_path)
        if new_seaborn:
            app.seaborns.update(new_seaborn)
            messagebox.showinfo("Success", "Seaborn snippets imported successfully.")
        else:
            messagebox.showwarning("Warning", "No Seaborn snippets were found in the selected YAML file.")

# Function to import Numpy snippets from a YAML file
def import_numpy(app):
    file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml")])
    if file_path:
        new_numpy = load_numpy_from_yaml(file_path)
        if new_numpy:
            app.numpys.update(new_numpy)
            messagebox.showinfo("Success", "Numpy snippets imported successfully.")
        else:
            messagebox.showwarning("Warning", "No Numpy snippets were found in the selected YAML file.")

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

# Function to export sql snippets to a YAML file
def export_sql(app):
    file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
    if file_path:
        save_sql_to_yaml(app.functions, file_path)

# Function to export Confluence templates to a YAML file
def export_confluence(app):
    file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
    if file_path:
        save_confluence_to_yaml(app.functions, file_path)

# Function to export Seaborn snippets to a YAML file
def export_seaborn(app):
    file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
    if file_path:
        save_seaborn_to_yaml(app.functions, file_path)

# Function to export Numpy snippets to a YAML file
def export_numpy(app):
    file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
    if file_path:
        save_numpy_to_yaml(app.functions, file_path)