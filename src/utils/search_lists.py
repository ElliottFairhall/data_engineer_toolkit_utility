import tkinter as tk
from src.utils.refresh_lists import *

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

# Function to search for sql templates based on user input
def search_sql_templates(app):
    # Get the search query from the entry widget, remove leading/trailing whitespace, and convert to lowercase
    query = app.search_entry.get().strip().lower()
    if query:
        # Find matches in document keys based on the query
        matches = [sql for sql in app.sqls.keys() if query in sql.lower()]
        # Clear the SQL list box
        app.sql_listbox.delete(0, tk.END)
        # Insert matched SQL code into the SQL code list box
        for sql in matches:
            app.sql_listbox.insert(tk.END, sql)
    else:
        # If the search query is empty, refresh the sql list
        refresh_sql_list(app)

# Function to clear the SQL search box and refresh the SQL list
def clear_sql_search(app):
    # Clear the search entry widget
    app.search_entry.delete(0, tk.END)
    # Refresh the SQL code list
    refresh_sql_list(app)

# Function to search for confluence document templates based on user input
def search_confluence_templates(app):
    # Get the search query from the entry widget, remove leading/trailing whitespace, and convert to lowercase
    query = app.search_entry.get().strip().lower()
    if query:
        # Find matches in document keys based on the query
        matches = [confluence for confluence in app.confluences.keys() if query in confluence.lower()]
        # Clear the Confluence list box
        app.confluence_listbox.delete(0, tk.END)
        # Insert matched Confluence template into the SQL code list box
        for confluence in matches:
            app.confluence_listbox.insert(tk.END, confluence)
    else:
        # If the search query is empty, refresh the Confluence list
        refresh_confluence_list(app)

# Function to clear the Confluence search box and refresh the Confluence template list
def clear_confluence_search(app):
    # Clear the search entry widget
    app.search_entry.delete(0, tk.END)
    # Refresh the Confluence list
    refresh_confluence_list(app)

# Function to search for Seaborn templates based on user input
def search_seaborn_templates(app):
    # Get the search query from the entry widget, remove leading/trailing whitespace, and convert to lowercase
    query = app.search_entry.get().strip().lower()
    if query:
        # Find matches in document keys based on the query
        matches = [seaborn for seaborn in app.seaborns.keys() if query in seaborn.lower()]
        # Clear the Seaborn list box
        app.seaborn_listbox.delete(0, tk.END)
        # Insert matched Seaborn template into the SQL code list box
        for seaborn in matches:
            app.seaborn_listox.insert(tk.END, seaborn)
    else:
        # If the search query is empty, refresh the Seaborn list
        refresh_seaborn_list(app)

# Function to clear the Seaborn search box and refresh the Seaborn template list
def clear_seaborn_search(app):
    # Clear the search entry widget
    app.search_entry.delete(0, tk.END)
    # Refresh the Seaborn list
    refresh_seaborn_list(app)

# Function to search for Numpy templates based on user input
def search_numpy_templates(app):
    # Get the search query from the entry widget, remove leading/trailing whitespace, and convert to lowercase
    query = app.search_entry.get().strip().lower()
    if query:
        # Find matches in Numpy keys based on the query
        matches = [numpy for numpy in app.numpys.keys() if query in numpy.lower()]
        # Clear the Numpy list box
        app.numpy_listbox.delete(0, tk.END)
        # Insert matched Numpy template into the Numpy code list box
        for numpy in matches:
            app.numpy_listbox.insert(tk.END, numpy)
    else:
        # If the search query is empty, refresh the Numpy list
        refresh_numpy_list(app)

# Function to clear the Numpy search box and refresh the Numpy template list
def clear_numpy_search(app):
    # Clear the search entry widget
    app.search_entry.delete(0, tk.END)
    # Refresh the Numpy list
    refresh_numpy_list(app)