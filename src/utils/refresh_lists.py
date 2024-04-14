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
