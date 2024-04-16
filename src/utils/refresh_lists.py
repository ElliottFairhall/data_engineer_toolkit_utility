import tkinter as tk

# Function to refresh the function list within the function list box
def refresh_function_list(app):
    # Clear the function list box
    app.function_listbox.delete(0, tk.END)
    # Iterate through each function and insert it into the list box
    for func in app.functions:
        app.function_listbox.insert(tk.END, func)

# Function to refresh the document list within the document list box
def refresh_document_list(app):
    # Clear the document list box
    app.document_listbox.delete(0, tk.END)
    # Iterate through each document and insert it into the list box
    for doc in app.documents:
        app.document_listbox.insert(tk.END, doc)

# Function to refresh the SQL list within the SQL list box
def refresh_sql_list(app):
    # Clear the SQL list box
    app.sql_listbox.delete(0, tk.END)
    # Iterate through each SQL statement/code and insert it into the list box
    for doc in app.sqls:
        app.sql_listbox.insert(tk.END, doc)

# Function to refresh the Confluence document list within the document list box
def refresh_confluence_list(app):
    # Clear the Confluence document list box
    app.confluence_listbox.delete(0, tk.END)
    # Iterate through each Confluence document and insert it into the list box
    for doc in app.confluences:
        app.cofluence_listbox.insert(tk.END, doc)

# Function to refresh the Seaborn list within the Seaborn list box
def refresh_seaborn_list(app):
    # Clear the Seaborn list box
    app.seaborn_listbox.delete(0, tk.END)
    # Iterate through each Seaborn statement/code and insert it into the list box
    for doc in app.seaborns:
        app.seaborn_listbox.insert(tk.END, doc)

# Function to refresh the Seaborn list within the Seaborn list box
def refresh_seaborn_list(app):
    # Clear the Seaborn list box
    app.seaborn_listbox.delete(0, tk.END)
    # Iterate through each Seaborn statement/code and insert it into the list box
    for doc in app.seaborns:
        app.seaborn_listbox.insert(tk.END, doc)

# Function to refresh the Numpy list within the Seaborn list box
def refresh_numpy_list(app):
    # Clear the Numpy list box
    app.numpy_listbox.delete(0, tk.END)
    # Iterate through each Numpy statement/code and insert it into the list box
    for doc in app.numpys:
        app.numpy_listbox.insert(tk.END, doc)