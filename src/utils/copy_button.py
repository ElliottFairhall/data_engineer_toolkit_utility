import tkinter as tk
from tkinter import messagebox

# Function to copy code snippet to clipboard
def copy_code_to_clipboard(app):
    index = app.function_listbox.curselection()  # Get the index of the selected item in the listbox
    if index:
        try:
            # Get the name of the selected function
            func_name = app.function_listbox.get(index[0])
            # Check if the function name exists in the loaded functions
            if func_name in app.functions:
                # Get the code snippet associated with the selected function
                code = app.functions[func_name]["Code"]
                # Clear the clipboard and append the code snippet
                app.root.clipboard_clear()  # Use app.root for clipboard
                app.root.clipboard_append(code)
                # Show a success message
                messagebox.showinfo("Copied", f"Snippet for '{func_name}' copied to clipboard.")
            else:
                # Show an error message if the function is not found
                messagebox.showerror("Error", "Snippet not found in the loaded Snippets File.")
        except Exception as e:
            # Show an error message if an exception occurs
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        # Show an error message if no snippet is selected
        messagebox.showerror("Error", "Please select a snippet first.")

# Function to copy markdown template to clipboard
def copy_template_to_clipboard(app):
    index = app.document_listbox.curselection()  # Get the index of the selected item in the listbox
    if index:
        try:
            # Get the name of the selected document
            doc_name = app.document_listbox.get(index[0])
            # Check if the document name exists in the loaded documents
            if doc_name in app.documents:
                # Get the markdown template associated with the selected document
                document = app.documents[doc_name]["Preview"]
                # Clear the clipboard and append the markdown template
                app.root.clipboard_clear()  # Use app.root for clipboard
                app.root.clipboard_append(document)
                # Show a success message
                messagebox.showinfo("Copied", f"{doc_name} copied to clipboard.")
            else:
                # Show an error message if the template is not found
                messagebox.showerror("Error", "Markdown Template not found in the loaded templates.")
        except Exception as e:
            # Show an error message if an exception occurs
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        # Show an error message if no template is selected
        messagebox.showerror("Error", "Please select a markdown template first.")
