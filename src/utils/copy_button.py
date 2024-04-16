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

# Function to copy sql code to clipboard
def copy_sql_to_clipboard(app):
    index = app.sql_listbox.curselection()  # Get the index of the selected item in the listbox
    if index:
        try:
            # Get the name of the selected sql code
            sql_name = app.sql_listbox.get(index[0])
            # Check if the sql code name exists in the loaded sql templates
            if sql_name in app.sqls:
                # Get the sql code associated with the selected sql template
                sql = app.sqls[sql_name]["Code"]
                # Clear the clipboard and append the sql code
                app.root.clipboard_clear()  # Use app.root for clipboard
                app.root.clipboard_append(sql)
                # Show a success message
                messagebox.showinfo("Copied", f"{sql_name} code copied to clipboard.")
            else:
                # Show an error message if the sql code is not found
                messagebox.showerror("Error", "sql code not found in the loaded templates.")
        except Exception as e:
            # Show an error message if an exception occurs
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        # Show an error message if no sql code is selected
        messagebox.showerror("Error", "Please select a sql statement first.")

# Function to copy confluence template to clipboard
def copy_confluence_template_to_clipboard(app):
    index = app.confluence_listbox.curselection()  # Get the index of the selected item in the listbox
    if index:
        try:
            # Get the name of the selected confluence document
            confluence_name = app.confluence_listbox.get(index[0])
            # Check if the confluence document name exists in the loaded documents
            if confluence_name in app.confluences:
                # Get the confluence template associated with the selected document
                confluence = app.confluences[confluence_name]["Content"]
                # Clear the clipboard and append the confluence template
                app.root.clipboard_clear()  # Use app.root for clipboard
                app.root.clipboard_append(confluence)
                # Show a success message
                messagebox.showinfo("Copied", f"{confluence_name} copied to clipboard.")
            else:
                # Show an error message if the confluence template is not found
                messagebox.showerror("Error", "Confluence Template not found in the loaded templates.")
        except Exception as e:
            # Show an error message if an exception occurs
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        # Show an error message if no confluence template is selected
        messagebox.showerror("Error", "Please select a Confluence template first.")

# Function to copy seaborn code snippet to clipboard
def copy_seaborn_code_to_clipboard(app):
    index = app.seaborn_listbox.curselection()  # Get the index of the selected item in the listbox
    if index:
        try:
            # Get the name of the selected seaborn function
            seaborn_name = app.seaborn_listbox.get(index[0])
            # Check if the seaborn function name exists in the loaded Seaborn snippets
            if seaborn_name in app.seaborns:
                # Get the seaborn code snippet associated with the selected function
                code = app.seaborns[seaborn_name]["Code"]
                # Clear the clipboard and append the seaborn code snippet
                app.root.clipboard_clear()  # Use app.root for clipboard
                app.root.clipboard_append(code)
                # Show a success message
                messagebox.showinfo("Copied", f"Snippet for '{seaborn_name}' copied to clipboard.")
            else:
                # Show an error message if the seaborn function is not found
                messagebox.showerror("Error", "Seaborn Snippet not found in the loaded Snippets File.")
        except Exception as e:
            # Show an error message if an exception occurs
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        # Show an error message if no seaborn snippet is selected
        messagebox.showerror("Error", "Please select a snippet first.")

# Function to copy numpy code snippet to clipboard
def copy_numpy_code_to_clipboard(app):
    index = app.numpy_listbox.curselection()  # Get the index of the selected item in the listbox
    if index:
        try:
            # Get the name of the selected numpy function
            numpy_name = app.numpy_listbox.get(index[0])
            # Check if the numpy function name exists in the loaded numpy snippets
            if numpy_name in app.numpys:
                # Get the numpy code snippet associated with the selected function
                code = app.numpys[numpy_name]["Code"]
                # Clear the clipboard and append the numpy code snippet
                app.root.clipboard_clear()  # Use app.root for clipboard
                app.root.clipboard_append(code)
                # Show a success message
                messagebox.showinfo("Copied", f"Snippet for '{numpy_name}' copied to clipboard.")
            else:
                # Show an error message if the numpy function is not found
                messagebox.showerror("Error", "Numpy Snippet not found in the loaded Snippets File.")
        except Exception as e:
            # Show an error message if an exception occurs
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        # Show an error message if no seaborn snippet is selected
        messagebox.showerror("Error", "Please select a snippet first.")