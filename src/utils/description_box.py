
# Function to display code description based on user function selection
def show_code_description(self):
    # Get the index of the selected item in the function listbox
    index = self.function_listbox.curselection()
    if index:
        # Get the name of the selected function
        selected_func = self.function_listbox.get(index[0])
        # Update the description label with the description of the selected function
        self.description_label.config(text=self.functions[selected_func]["Description"])
    else:
        # Clear the description label if no function is selected
        self.description_label.config(text="")

# Function to display document preview based on user document selection
def show_document_description(self):
    # Get the index of the selected item in the document listbox
    index = self.document_listbox.curselection()
    if index:
        # Get the name of the selected document
        selected_doc = self.document_listbox.get(index[0])
        # Update the description label with the preview of the selected document
        self.description_label.config(text=self.documents[selected_doc]["Preview"])
    else:
        # Clear the description label if no document is selected
        self.description_label.config(text="")

# Function to display sql preview based on user sql selection
def show_sql_description(self):
    # Get the index of the selected item in the sql listbox
    index = self.sql_listbox.curselection()
    if index:
        # Get the name of the selected sql code
        selected_sql = self.sql_listbox.get(index[0])
        # Update the description label with the description of the selected seaborn sql code
        self.description_label.config(text=self.functions[selected_sql]["Description"])
    else:
        # Clear the description label if no code is selected
        self.description_label.config(text="")

    # Function to display confluence document preview based on user confluence document selection
def show_confluence_description(self):
    # Get the index of the selected item in the confluence document listbox
    index = self.confluence_listbox.curselection()
    if index:
        # Get the name of the selected confluence document
        selected_confluence = self.confluence_listbox.get(index[0])
        # Update the description label with the preview of the selected confluence document
        self.description_label.config(text=self.documents[selected_confluence]["Preview"])
    else:
        # Clear the description label if no confluence document is selected
        self.description_label.config(text="")

# Function to display seaborn preview based on user seaborn code selection
def show_seaborn_description(self):
    # Get the index of the selected item in the seaborn listbox
    index = self.seaborn_listbox.curselection()
    if index:
        # Get the name of the selected seaborn code
        selected_seaborn = self.seaborn_listbox.get(index[0])
        # Update the description label with the description of the selected seaform code
        self.description_label.config(text=self.functions[selected_seaborn]["Description"])
    else:
        # Clear the description label if no code is selected
        self.description_label.config(text="")

# Function to display numpy preview based on user numpy code selection
def show_numpy_description(self):
    # Get the index of the selected item in the numpy listbox
    index = self.numpy_listbox.curselection()
    if index:
        # Get the name of the selected numpy code
        selected_numpy = self.numpy_listbox.get(index[0])
        # Update the description label with the description of the selected numpy code
        self.description_label.config(text=self.functions[selected_numpy]["Description"])
    else:
        # Clear the description label if no code is selected
        self.description_label.config(text="")
