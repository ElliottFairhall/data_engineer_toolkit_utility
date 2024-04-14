import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkhtmlview import HTMLLabel

# Importing utility functions
from src.utils.copy_button import *
from src.utils.description_box import *
from src.utils.load_inital import *
from src.utils.refresh_lists import *
from src.utils.search_lists import *
from src.utils.yamls import *

# Class providing the initial screen of the application
class InitialPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Engineer")
        self.create_widgets()

    # Method to create widgets for the initial page
    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title label
        title_label = ttk.Label(self.frame, text="Data Engineering Toolkit", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=(0, 20))

        # Buttons for different functionalities
        functions_button = ttk.Button(self.frame, text="Pandas Snippets", command=self.open_functions_page)
        functions_button.pack(pady=10)
    
        numpy_button = ttk.Button(self.frame, text="Numpy Snippets", command=self.open_numpy_page)
        numpy_button.pack(pady=10)

        seaborn_button = ttk.Button(self.frame, text="Seaborn Snippets", command=self.open_seaborn_page)
        seaborn_button.pack(pady=10)

        documentation_button = ttk.Button(self.frame, text="Markdown Templates", command=self.open_documentation_page)
        documentation_button.pack(pady=10)
    
        confluence_button = ttk.Button(self.frame, text="Confluence Templates", command=self.open_confluence_page)
        confluence_button.pack(pady=10)

        sql_button = ttk.Button(self.frame, text="SQL Snippets", command=self.open_sql_page)
        sql_button.pack(pady=10)

    # Methods to open different pages
    def open_functions_page(self):
        self.root.destroy()
        root = tk.Tk()
        app = PandasFunctionApp(root)
        root.mainloop()

    def open_documentation_page(self):
        self.root.destroy()
        root = tk.Tk()
        app = DocumentFunctionApp(root)
        root.mainloop()

    def open_sql_page(self):
        messagebox.showinfo("SQL", "Placeholder: SQL page will be implemented here.")

    def open_confluence_page(self):
        messagebox.showinfo("Confluence Templates", "Placeholder: Confluence Templates page will be implemented here.")

    def open_seaborn_page(self):
        messagebox.showinfo("Seaborn", "Placeholder: Seaborn page will be implemented here.")
    
    def open_numpy_page(self):
        messagebox.showinfo("Numpy", "Placeholder: Numpy page will be implemented here.")
    
    def open_recipies_page(self):
        messagebox.showinfo("Recipies", "Placeholder: Recipies page will be implemented here.")

# Class providing the pandas function screen of the application
class PandasFunctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pandas Snippet Selector")
        self.functions = load_initial_functions()
        self.create_widgets()
        self.root.bind("<Control-c>", lambda e: copy_code_to_clipboard(self))
        self.root.bind("<Control-q>", lambda e: self.root.quit())

    # Method to create widgets for the Pandas function page
    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Top Section - Title and Import Button
        title_label = ttk.Label(self.frame, text="Pandas Snippets", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="nsew")

        self.import_button = ttk.Button(self.frame, text="Import Snippets", command=lambda: import_functions(self))
        self.import_button.grid(row=0, column=2, padx=(10, 0), pady=(0, 10), sticky="e")

        # Search Bar - Spans all columns
        self.search_entry = ttk.Entry(self.frame)
        self.search_entry.grid(row=1, column=0, columnspan=3, padx=5, pady=(5, 10), sticky="nsew")

        search_button = ttk.Button(self.frame, text="Search", command=lambda: self.search_functions(self.search_entry.get()))
        search_button.grid(row=2, column=2, padx=5, pady=(5, 10))

        # Function Selector Box (Left) and Description (Right)
        self.function_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE, exportselection=0)
        for func in self.functions:
            self.function_listbox.insert(tk.END, func)
        self.function_listbox.grid(row=3, column=0, rowspan=2, sticky="nsew", padx=(0, 10), pady=(0, 10))  # Spans 2 rows

        self.description_label = ttk.Label(self.frame, text="", justify=tk.LEFT)  # Left-justified text
        self.description_label.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew", padx=(10, 20), pady=(0, 10))  # Spans 2 rows, adjusted padding
        self.description_label.configure(text="Snippet Description")
        self.function_listbox.bind('<<ListboxSelect>>', lambda event: self.show_description())

        # Buttons
        self.clipboard_button = ttk.Button(self.frame, text="Copy to Clipboard", command=lambda: copy_code_to_clipboard(self))
        self.clipboard_button.grid(row=5, column=0, pady=(0, 10), sticky="w")

        self.back_button = ttk.Button(self.frame, text="Back", command=self.go_back)
        self.back_button.grid(row=6, column=0, pady=(0, 10), sticky="w")

    # Method to go back to the initial page
    def go_back(self):
        self.root.destroy()
        root = tk.Tk()
        app = InitialPage(root)
        root.mainloop()

    # Method to display the description of the selected function
    def show_description(self):
        index = self.function_listbox.curselection()
        if index:
            func_name = self.function_listbox.get(index[0])
            description = self.functions.get(func_name, {}).get('Description', "")
            self.description_label.config(text=description)

    # Methods for saving, searching, and clearing function lists
    def save_functions_to_yaml(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
        if file_path:
            save_functions_to_yaml(self.functions, file_path)

    def search_functions(self, query):
        matches = [func for func in self.functions.keys() if query.lower() in func.lower()]
        self.function_listbox.delete(0, tk.END)
        for func in matches:
            self.function_listbox.insert(tk.END, func)

    def clear_function_search(self):
        self.refresh_function_list()

# Class providing the documentation screen of the application
class DocumentFunctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Selector")
        self.documents = load_initial_templates()
        self.create_widgets()
        self.root.bind("<Control-c>", lambda e: copy_template_to_clipboard(self))
        self.root.bind("<Control-q>", lambda e: self.root.quit())

    # Method to create widgets for the documentation page
    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Top Section - Title and Import Button
        title_label = ttk.Label(self.frame, text="Markdown Templates", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="nsew")

        self.import_button = ttk.Button(self.frame, text="Import Templates", command=lambda: import_templates(self))
        self.import_button.grid(row=0, column=2, padx=(10, 0), pady=(0, 10), sticky="e")

        # Search Bar - Spans all columns
        self.search_entry = ttk.Entry(self.frame)
        self.search_entry.grid(row=1, column=0, columnspan=3, padx=5, pady=(5, 10), sticky="nsew")

        search_button = ttk.Button(self.frame, text="Search", command=lambda: self.search_documents(self.search_entry.get()))
        search_button.grid(row=2, column=2, padx=5, pady=(5, 10))  # Adjusted row for better alignment

        # Document Selector Box (Left) and Description (Right)
        self.document_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE, exportselection=0)
        for name, details in self.documents.items():
            self.document_listbox.insert(tk.END, name)
        self.document_listbox.grid(row=3, column=0, rowspan=2, sticky="nsew", padx=(0, 10), pady=(0, 10))  # Spans 2 rows

        self.description_label = ttk.Label(self.frame, text="", justify=tk.LEFT)  # Left-justified text
        self.description_label.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew", padx=(10, 20), pady=(0, 10))  # Spans 2 rows, adjusted padding
        self.description_label.configure(text="Markdown Template Description")
        self.document_listbox.bind('<<ListboxSelect>>', lambda event: self.show_description())

        # Buttons
        self.clipboard_button = ttk.Button(self.frame, text="Copy to Clipboard", command=lambda: copy_template_to_clipboard(self))
        self.clipboard_button.grid(row=5, column=0, pady=(0, 10), sticky="w")

        self.back_button = ttk.Button(self.frame, text="Back", command=self.go_back)
        self.back_button.grid(row=6, column=0, pady=(0, 10), sticky="w")

    # Method to go back to the initial page
    def go_back(self):
        self.root.destroy()
        root = tk.Tk()
        app = InitialPage(root)
        root.mainloop()

    # Method to display the description of the selected document
    def show_description(self):
        index = self.document_listbox.curselection()
        if index:
            doc_name = self.document_listbox.get(index[0])
            description = self.documents[doc_name].get('Description', "")
            self.description_label.config(text=description)

    # Methods for saving, searching, and clearing document lists
    def save_documents_to_yaml(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
        if file_path:
            save_documents_to_yaml(self.documents, file_path)

    def search_documents(self, query):
        matches = [doc for doc in self.documents.keys() if query.lower() in doc.lower()]
        self.document_listbox.delete(0, tk.END)
        for doc in matches:
            self.document_listbox.insert(tk.END, doc)

    def clear_document_search(self):
        self.refresh_document_list()

def main():
    root = tk.Tk()
    app = InitialPage(root)
    root.mainloop()
