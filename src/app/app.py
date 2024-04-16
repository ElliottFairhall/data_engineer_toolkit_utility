import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkhtmlview import HTMLLabel
from ttkthemes import ThemedTk

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
        self.root.title("Data Engineering Toolkit Utility")
        self.root.geometry('400x400')
        self.root.resizable(False, False)
        self.create_widgets()

    # Method to create widgets for the initial page
    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title label
        title_label = ttk.Label(self.frame, text="Snippets & Templates", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=(0, 20))

        # Buttons for different functionalities
        self.create_button("Pandas Snippets", self.open_functions_page)
        self.create_button("Numpy Snippets", self.open_numpy_page)
        self.create_button("Seaborn Snippets", self.open_seaborn_page)
        self.create_button("Markdown Templates", self.open_documentation_page)
        self.create_button("Confluence Templates", self.open_confluence_page)
        self.create_button("SQL Snippets", self.open_sql_page)

    def create_button(self, text, command):
        button = ttk.Button(self.frame, text=text, command=command)
        button.pack(pady=10)

    # Methods to open different pages
    def open_functions_page(self):
        self.root.destroy()
        root = ThemedTk(theme="equilux")
        app = PandasFunctionApp(root)
        root.mainloop()

    def open_documentation_page(self):
        self.root.destroy()
        root = ThemedTk(theme="equilux")
        app = DocumentFunctionApp(root)
        root.mainloop()

    def open_sql_page(self):
        self.root.destroy()
        root = ThemedTk(theme="equilux")
        app = SqlFunctionApp(root)
        root.mainloop()

    def open_confluence_page(self):
        self.root.destroy()
        root = ThemedTk(theme="equilux")
        app = ConfluenceFunctionApp(root)
        root.mainloop()

    def open_seaborn_page(self):
        self.root.destroy()
        root = ThemedTk(theme="equilux")
        app = SeabornFunctionApp(root)
        root.mainloop()
    
    def open_numpy_page(self):
        self.root.destroy()
        root = ThemedTk(theme="equilux")
        app = NumpyFunctionApp(root)
        root.mainloop()
    
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
        root = ThemedTk(theme="equilux")
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
        root = ThemedTk(theme="equilux")
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

# Class providing the Numpy snippets screen of the application
class NumpyFunctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Numpy Snippet Selector")
        self.numpys = load_initial_numpy_templates()
        self.create_widgets()
        self.root.bind("<Control-c>", lambda e: copy_numpy_code_to_clipboard(self))
        self.root.bind("<Control-q>", lambda e: self.root.quit())

    # Method to create widgets for the Numpy snippets page
    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Top Section - Title and Import Button
        title_label = ttk.Label(self.frame, text="Numpy Snippets", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="nsew")

        self.import_button = ttk.Button(self.frame, text="Import Snippets", command=lambda: import_numpy(self))
        self.import_button.grid(row=0, column=2, padx=(10, 0), pady=(0, 10), sticky="e")

        # Search Bar - Spans all columns
        self.search_entry = ttk.Entry(self.frame)
        self.search_entry.grid(row=1, column=0, columnspan=3, padx=5, pady=(5, 10), sticky="nsew")

        search_button = ttk.Button(self.frame, text="Search", command=lambda: self.search_numpy(self.search_entry.get()))
        search_button.grid(row=2, column=2, padx=5, pady=(5, 10))

        # Numpy Selector Box (Left) and Description (Right)
        self.numpy_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE, exportselection=0)
        for numpy in self.numpys:
            self.numpy_listbox.insert(tk.END, numpy)
        self.numpy_listbox.grid(row=3, column=0, rowspan=2, sticky="nsew", padx=(0, 10), pady=(0, 10))  # Spans 2 rows

        self.description_label = ttk.Label(self.frame, text="", justify=tk.LEFT)  # Left-justified text
        self.description_label.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew", padx=(10, 20), pady=(0, 10))  # Spans 2 rows, adjusted padding
        self.description_label.configure(text="Snippet Description")
        self.numpy_listbox.bind('<<ListboxSelect>>', lambda event: self.show_description())

        # Buttons
        self.clipboard_button = ttk.Button(self.frame, text="Copy to Clipboard", command=lambda: copy_numpy_code_to_clipboard(self))
        self.clipboard_button.grid(row=5, column=0, pady=(0, 10), sticky="w")

        self.back_button = ttk.Button(self.frame, text="Back", command=self.go_back)
        self.back_button.grid(row=6, column=0, pady=(0, 10), sticky="w")

    # Method to go back to the initial page
    def go_back(self):
        self.root.destroy()
        root = ThemedTk(theme="equilux")
        app = InitialPage(root)
        root.mainloop()

    # Method to display the description of the selected Numpy snippet
    def show_description(self):
        index = self.numpy_listbox.curselection()
        if index:
            numpy_name = self.numpy_listbox.get(index[0])
            description = self.numpys.get(numpy_name, {}).get('Description', "")
            self.description_label.config(text=description)

    # Methods for saving, searching, and clearing Numpy snippets
    def save_numpy_to_yaml(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
        if file_path:
            save_numpy_to_yaml(self.numpys, file_path)

    def search_numpy(self, query):
        matches = [numpy for numpy in self.numpys.keys() if query.lower() in numpy.lower()]
        self.numpy_listbox.delete(0, tk.END)
        for numpy in matches:
            self.numpy_listbox.insert(tk.END, numpy)

    def clear_numpy_search(self):
        self.clear_numpy_search()

# Class providing the SQL snippets screen of the application
class SqlFunctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQL Snippet Selector")
        self.sqls = load_initial_sql_templates()
        self.create_widgets()
        self.root.bind("<Control-c>", lambda e: copy_sql_to_clipboard(self))
        self.root.bind("<Control-q>", lambda e: self.root.quit())

    # Method to create widgets for the SQL snippets page
    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Top Section - Title and Import Button
        title_label = ttk.Label(self.frame, text="SQL Snippets", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="nsew")

        self.import_button = ttk.Button(self.frame, text="Import Snippets", command=lambda: import_sql(self))
        self.import_button.grid(row=0, column=2, padx=(10, 0), pady=(0, 10), sticky="e")

        # Search Bar - Spans all columns
        self.search_entry = ttk.Entry(self.frame)
        self.search_entry.grid(row=1, column=0, columnspan=3, padx=5, pady=(5, 10), sticky="nsew")

        search_button = ttk.Button(self.frame, text="Search", command=lambda: self.search_sql(self.search_entry.get()))
        search_button.grid(row=2, column=2, padx=5, pady=(5, 10))

        # SQL Selector Box (Left) and Description (Right)
        self.sql_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE, exportselection=0)
        for sql in self.sqls:
            self.sql_listbox.insert(tk.END, sql)
        self.sql_listbox.grid(row=3, column=0, rowspan=2, sticky="nsew", padx=(0, 10), pady=(0, 10))  # Spans 2 rows

        self.description_label = ttk.Label(self.frame, text="", justify=tk.LEFT)  # Left-justified text
        self.description_label.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew", padx=(10, 20), pady=(0, 10))  # Spans 2 rows, adjusted padding
        self.description_label.configure(text="Snippet Description")
        self.sql_listbox.bind('<<ListboxSelect>>', lambda event: self.show_description())

        # Buttons
        self.clipboard_button = ttk.Button(self.frame, text="Copy to Clipboard", command=lambda: copy_sql_to_clipboard(self))
        self.clipboard_button.grid(row=5, column=0, pady=(0, 10), sticky="w")

        self.back_button = ttk.Button(self.frame, text="Back", command=self.go_back)
        self.back_button.grid(row=6, column=0, pady=(0, 10), sticky="w")

    # Method to go back to the initial page
    def go_back(self):
        self.root.destroy()
        root = ThemedTk(theme="equilux")
        app = InitialPage(root)
        root.mainloop()

    # Method to display the description of the selected sql snippet
    def show_description(self):
        index = self.sql_listbox.curselection()
        if index:
            sql_name = self.sql_listbox.get(index[0])
            description = self.sqls.get(sql_name, {}).get('Description', "")
            self.description_label.config(text=description)

    # Methods for saving, searching, and clearing sql snippets
    def save_sql_to_yaml(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
        if file_path:
            save_sql_to_yaml(self.sqls, file_path)

    def search_sql(self, query):
        matches = [sql for sql in self.sqls.keys() if query.lower() in sql.lower()]
        self.sql_listbox.delete(0, tk.END)
        for sql in matches:
            self.sql_listbox.insert(tk.END, sql)

    def clear_sql_search(self):
        self.clear_sql_search()

# Class providing the Seaborn snippets screen of the application
class SeabornFunctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seaborn Snippet Selector")
        self.seaborns = load_initial_seaborn_templates()
        self.create_widgets()
        self.root.bind("<Control-c>", lambda e: copy_seaborn_code_to_clipboard(self))
        self.root.bind("<Control-q>", lambda e: self.root.quit())

    # Method to create widgets for the seaborn snippets page
    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Top Section - Title and Import Button
        title_label = ttk.Label(self.frame, text="Seaborn Snippets", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="nsew")

        self.import_button = ttk.Button(self.frame, text="Import Snippets", command=lambda: import_seaborn(self))
        self.import_button.grid(row=0, column=2, padx=(10, 0), pady=(0, 10), sticky="e")

        # Search Bar - Spans all columns
        self.search_entry = ttk.Entry(self.frame)
        self.search_entry.grid(row=1, column=0, columnspan=3, padx=5, pady=(5, 10), sticky="nsew")

        search_button = ttk.Button(self.frame, text="Search", command=lambda: self.search_seaborn(self.search_entry.get()))
        search_button.grid(row=2, column=2, padx=5, pady=(5, 10))

        # Seaborn Selector Box (Left) and Description (Right)
        self.seaborn_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE, exportselection=0)
        for seaborn in self.seaborns:
            self.seaborn_listbox.insert(tk.END, seaborn)
        self.seaborn_listbox.grid(row=3, column=0, rowspan=2, sticky="nsew", padx=(0, 10), pady=(0, 10))  # Spans 2 rows

        self.description_label = ttk.Label(self.frame, text="", justify=tk.LEFT)  # Left-justified text
        self.description_label.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew", padx=(10, 20), pady=(0, 10))  # Spans 2 rows, adjusted padding
        self.description_label.configure(text="Snippet Description")
        self.seaborn_listbox.bind('<<ListboxSelect>>', lambda event: self.show_description())

        # Buttons
        self.clipboard_button = ttk.Button(self.frame, text="Copy to Clipboard", command=lambda: copy_seaborn_code_to_clipboard(self))
        self.clipboard_button.grid(row=5, column=0, pady=(0, 10), sticky="w")

        self.back_button = ttk.Button(self.frame, text="Back", command=self.go_back)
        self.back_button.grid(row=6, column=0, pady=(0, 10), sticky="w")

    # Method to go back to the initial page
    def go_back(self):
        self.root.destroy()
        root = ThemedTk(theme="equilux")
        app = InitialPage(root)
        root.mainloop()

    # Method to display the description of the selected Seaborn snippet
    def show_description(self):
        index = self.seaborn_listbox.curselection()
        if index:
            seaborn_name = self.seaborn_listbox.get(index[0])
            description = self.seaborns.get(seaborn_name, {}).get('Description', "")
            self.description_label.config(text=description)

    # Methods for saving, searching, and clearing Seaborn snippets
    def save_seaborn_to_yaml(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
        if file_path:
            save_seaborn_to_yaml(self.seaborns, file_path)

    def search_seaborn(self, query):
        matches = [seaborn for seaborn in self.seaborns.keys() if query.lower() in seaborn.lower()]
        self.seaborn_listbox.delete(0, tk.END)
        for seaborn in matches:
            self.seaborn_listbox.insert(tk.END, seaborn)

    def clear_seaborn_search(self):
        self.clear_seaborn_search()

# Class providing the Confluence documentation screen of the application
class ConfluenceFunctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Confluence Template Selector")
        self.confluences = load_initial_confluence_templates()
        self.create_widgets()
        self.root.bind("<Control-c>", lambda e: copy_confluence_template_to_clipboard(self))
        self.root.bind("<Control-q>", lambda e: self.root.quit())

    # Method to create widgets for the Confluence documentation page
    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Top Section - Title and Import Button
        title_label = ttk.Label(self.frame, text="Confluence Templates", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="nsew")

        self.import_button = ttk.Button(self.frame, text="Import Templates", command=lambda: import_confluence(self))
        self.import_button.grid(row=0, column=2, padx=(10, 0), pady=(0, 10), sticky="e")

        # Search Bar - Spans all columns
        self.search_entry = ttk.Entry(self.frame)
        self.search_entry.grid(row=1, column=0, columnspan=3, padx=5, pady=(5, 10), sticky="nsew")

        search_button = ttk.Button(self.frame, text="Search", command=lambda: self.search_confluence(self.search_entry.get()))
        search_button.grid(row=2, column=2, padx=5, pady=(5, 10))  # Adjusted row for better alignment

        # Confluence document Selector Box (Left) and Description (Right)
        self.confluence_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE, exportselection=0)
        for name, details in self.confluences.items():
            self.confluence_listbox.insert(tk.END, name)
        self.confluence_listbox.grid(row=3, column=0, rowspan=2, sticky="nsew", padx=(0, 10), pady=(0, 10))  # Spans 2 rows

        self.description_label = ttk.Label(self.frame, text="", justify=tk.LEFT)  # Left-justified text
        self.description_label.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew", padx=(10, 20), pady=(0, 10))  # Spans 2 rows, adjusted padding
        self.description_label.configure(text="Markdown Template Description")
        self.confluence_listbox.bind('<<ListboxSelect>>', lambda event: self.show_description())

        # Buttons
        self.clipboard_button = ttk.Button(self.frame, text="Copy to Clipboard", command=lambda: copy_confluence_template_to_clipboard(self))
        self.clipboard_button.grid(row=5, column=0, pady=(0, 10), sticky="w")

        self.back_button = ttk.Button(self.frame, text="Back", command=self.go_back)
        self.back_button.grid(row=6, column=0, pady=(0, 10), sticky="w")

    # Method to go back to the initial page
    def go_back(self):
        self.root.destroy()
        root = ThemedTk(theme="equilux")
        app = InitialPage(root)
        root.mainloop()

    # Method to display the description of the selected Confluence document
    def show_description(self):
        index = self.confluence_listbox.curselection()
        if index:
            confluence_name = self.confluence_listbox.get(index[0])
            description = self.confluences[confluence_name].get('Description', "")
            self.description_label.config(text=description)

    # Methods for saving, searching, and clearing Confluence document lists
    def save_confluence_to_yaml(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
        if file_path:
            save_confluence_to_yaml(self.documents, file_path)

    def search_confluence(self, query):
        matches = [confluence for confluence in self.confluences.keys() if query.lower() in confluence.lower()]
        self.confluence_listbox.delete(0, tk.END)
        for doc in matches:
            self.confluence_listbox.insert(tk.END, doc)

    def clear_confluence_search(self):
        self.clear_confluence_search()

def main():
    root = ThemedTk(theme="equilux")
    app = InitialPage(root)
    root.mainloop()
