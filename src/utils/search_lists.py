import tkinter as tk
from src.utils.refresh_lists import refresh_function_list, refresh_document_list

# Function to search for templates based on user input
def search_templates(app):
    # Get the search query from the entry widget, remove leading/trailing whitespace, and convert to lowercase
    query = app.search_entry.get().strip().lower()
    if query:
        # Find matches in document keys based on the query
        matches = [doc for doc in app.documents.keys() if query in doc.lower()]
        # Clear the document list box
        app.document_listbox.delete(0, tk.END)
        # Insert matched documents into the document list box
        for doc in matches:
            app.document_listbox.insert(tk.END, doc)
    else:
        # If the search query is empty, refresh the document list
        refresh_document_list(app)

# Function to clear the document search box and refresh the document list
def clear_document_search(app):
    # Clear the search entry widget
    app.search_entry.delete(0, tk.END)
    # Refresh the document list
    refresh_document_list(app)

# Function to search for functions based on user input
def search_functions(app):
    # Get the search query from the entry widget, remove leading/trailing whitespace, and convert to lowercase
    query = app.search_entry.get().strip().lower()
    if query:
        # Find matches in function keys based on the query
        matches = [func for func in app.functions.keys() if query in func.lower()]
        # Clear the function list box
        app.function_listbox.delete(0, tk.END)
        # Insert matched functions into the function list box
        for func in matches:
            app.function_listbox.insert(tk.END, func)
    else:
        # If the search query is empty, refresh the function list
        refresh_function_list(app)

# Function to clear the function search box and refresh the function list
def clear_function_search(app):
    # Clear the search entry widget
    app.search_entry.delete(0, tk.END)
    # Refresh the function list
    refresh_function_list(app)
