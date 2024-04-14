import tkinter as tk

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
