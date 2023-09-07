#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter as tk
from tkinter import messagebox

class CarDealershipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Dealership Management System")
        # Rest of your code...

        # Initialize data structures for inventory, sales, customers, and reports
        self.inventory = []
        self.sales = []
        self.customers = []  # List to store customer information
        self.reports = []  # List to store sales reports

        # Create and configure widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels
        label = tk.Label(self.root, text="Car Dealership Management System", font=("Helvetica", 16))
        label.pack(pady=20)

        # Buttons
        add_car_button = tk.Button(self.root, text="Add Car to Inventory", command=self.add_car)
        view_inventory_button = tk.Button(self.root, text="View Inventory", command=self.view_inventory)
        sell_car_button = tk.Button(self.root, text="Sell Car", command=self.sell_car)
        search_button = tk.Button(self.root, text="Search Inventory", command=self.search_inventory)
        add_customer_button = tk.Button(self.root, text="Add Customer", command=self.add_customer)
        view_customers_button = tk.Button(self.root, text="View Customers", command=self.view_customers)
        generate_report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)

        add_car_button.pack()
        view_inventory_button.pack()
        sell_car_button.pack()
        search_button.pack()
        add_customer_button.pack()
        view_customers_button.pack()
        generate_report_button.pack()
        exit_button.pack()

    def add_car(self):
        # Create a new window for adding a car
        add_car_window = tk.Toplevel(self.root)
        add_car_window.title("Add Car to Inventory")

        # Labels and Entry fields for car details
        label_make = tk.Label(add_car_window, text="Make:")
        label_make.pack()
        entry_make = tk.Entry(add_car_window)
        entry_make.pack()

        label_model = tk.Label(add_car_window, text="Model:")
        label_model.pack()
        entry_model = tk.Entry(add_car_window)
        entry_model.pack()

        label_year = tk.Label(add_car_window, text="Year:")
        label_year.pack()
        entry_year = tk.Entry(add_car_window)
        entry_year.pack()

        label_price = tk.Label(add_car_window, text="Price(In Dollars):")
        label_price.pack()
        entry_price = tk.Entry(add_car_window)
        entry_price.pack()

        # Function to save the car details to the inventory
        def save_car_details():
            make = entry_make.get()
            model = entry_model.get()
            year = entry_year.get()
            price_str = entry_price.get()

            if make and model and year and price_str:
                try:
                    price = float(price_str)  # Convert price to float
                    car = {"Make": make, "Model": model, "Year": year, "Price": price}
                    self.inventory.append(car)
                    messagebox.showinfo("Success", "Car added to inventory successfully.")
                    add_car_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid price.")
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

        # Create a "Save" button
        save_button = tk.Button(add_car_window, text="Save", command=save_car_details)
        save_button.pack()

    def view_inventory(self):
        # Create a new window to display the inventory
        view_inventory_window = tk.Toplevel(self.root)
        view_inventory_window.title("Inventory")

        # Create a text widget to display the inventory
        inventory_text = tk.Text(view_inventory_window, wrap=tk.WORD)
        inventory_text.pack()

        # Insert the inventory data into the text widget
        for car in self.inventory:
            inventory_text.insert(tk.END, "Make: " + car['Make'] + "\n")
            inventory_text.insert(tk.END, "Model: " + car['Model'] + "\n")
            inventory_text.insert(tk.END, "Year: " + car['Year'] + "\n")
            inventory_text.insert(tk.END, "Price: " + str(car['Price']) + "\n\n")

        # Disable text widget to make it read-only
        inventory_text.config(state=tk.DISABLED)

    def sell_car(self):
        # Create a new window for selling a car
        sell_car_window = tk.Toplevel(self.root)
        sell_car_window.title("Sell Car")

        # Create a listbox to display the inventory
        inventory_listbox = tk.Listbox(sell_car_window)
        inventory_listbox.pack()

        # Populate the listbox with inventory data
        for car in self.inventory:
            inventory_listbox.insert(tk.END, car['Make'] + " " + car['Model'] + " (" + car['Year'] + ")")

        # Function to handle the "Sell" button click
        def sell_selected_car():
            selected_index = inventory_listbox.curselection()
            if not selected_index:
                return  # No car selected, exit function

            selected_index = int(selected_index[0])

            if selected_index < len(self.inventory):
                sold_car = self.inventory.pop(selected_index)
                self.sales.append(sold_car)
                messagebox.showinfo("Success", "Sold: " + sold_car['Make'] + " " + sold_car['Model'] + " (" + sold_car['Year'] + ")")
                sell_car_window.destroy()

        # Create a "Sell" button
        sell_button = tk.Button(sell_car_window, text="Sell", command=sell_selected_car)
        sell_button.pack()

    def search_inventory(self):
        # Create a new window for searching the inventory
        search_inventory_window = tk.Toplevel(self.root)
        search_inventory_window.title("Search Inventory")

        # Labels and Entry fields for search criteria
        label_make = tk.Label(search_inventory_window, text="Search by Make:")
        label_make.pack()
        entry_make = tk.Entry(search_inventory_window)
        entry_make.pack()

        label_model = tk.Label(search_inventory_window, text="Search by Model:")
        label_model.pack()
        entry_model = tk.Entry(search_inventory_window)
        entry_model.pack()

        label_year = tk.Label(search_inventory_window, text="Search by Year:")
        label_year.pack()
        entry_year = tk.Entry(search_inventory_window)
        entry_year.pack()

        # Function to perform the search
        def perform_search():
            make = entry_make.get()
            model = entry_model.get()
            year = entry_year.get()

            results = []
            for car in self.inventory:
                if (not make or make.lower() in car['Make'].lower()) and \
                   (not model or model.lower() in car['Model'].lower()) and \
                   (not year or year == car['Year']):
                    results.append(car)

            # Display the search results
            self.display_search_results(search_inventory_window, results)

        # Create a "Search" button
        search_button = tk.Button(search_inventory_window, text="Search", command=perform_search)
        search_button.pack()

    def add_customer(self):
        # Create a new window for adding a customer
        add_customer_window = tk.Toplevel(self.root)
        add_customer_window.title("Add Customer")

        # Labels and Entry fields for customer details
        label_name = tk.Label(add_customer_window, text="Name:")
        label_name.pack()
        entry_name = tk.Entry(add_customer_window)
        entry_name.pack()

        label_email = tk.Label(add_customer_window, text="Email:")
        label_email.pack()
        entry_email = tk.Entry(add_customer_window)
        entry_email.pack()

        # Function to save customer details
        def save_customer_details():
            name = entry_name.get()
            email = entry_email.get()

            if name and email:
                customer = {"Name": name, "Email": email}
                self.customers.append(customer)
                messagebox.showinfo("Success", "Customer added successfully.")
                add_customer_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

        # Create a "Save" button
        save_button = tk.Button(add_customer_window, text="Save", command=save_customer_details)
        save_button.pack()

    def view_customers(self):
        # Create a new window to display customer information
        view_customers_window = tk.Toplevel(self.root)
        view_customers_window.title("Customer Information")

        # Create a text widget to display customer data
        customers_text = tk.Text(view_customers_window, wrap=tk.WORD)
        customers_text.pack()

        # Insert customer data into the text widget
        for customer in self.customers:
            customers_text.insert(tk.END, "Name: " + customer['Name'] + "\n")
            customers_text.insert(tk.END, "Email: " + customer['Email'] + "\n\n")

        # Disable text widget to make it read-only
        customers_text.config(state=tk.DISABLED)

    def generate_report(self):
        # Create a new window for generating a report
        report_window = tk.Toplevel(self.root)
        report_window.title("Generate Report")

        # Function to generate a sales report
        def generate_sales_report():
            report_text.config(state=tk.NORMAL)  # Enable text widget for editing
            report_text.delete(1.0, tk.END)  # Clear existing text

            total_sales = 0
            for sale in self.sales:
                total_sales += float(sale['Price'])  # Convert price to float

            report_text.insert(tk.END, "Total Sales: $" + "{:.2f}".format(total_sales) + "\n")
            report_text.insert(tk.END, "Number of Cars Sold: " + str(len(self.sales)) + "\n")
            report_text.insert(tk.END, "Car Sales Details:\n\n")

            for sale in self.sales:
                report_text.insert(tk.END, "Make: " + sale['Make'] + "\n")
                report_text.insert(tk.END, "Model: " + sale['Model'] + "\n")
                report_text.insert(tk.END, "Year: " + sale['Year'] + "\n")
                report_text.insert(tk.END, "Price: $" + "{:.2f}".format(float(sale['Price'])) + "\n\n")

            report_text.config(state=tk.DISABLED)  # Disable text widget for editing

        # Create a "Generate Report" button
        generate_report_button = tk.Button(report_window, text="Generate Sales Report", command=generate_sales_report)
        generate_report_button.pack()

        # Create a text widget to display the report
        report_text = tk.Text(report_window, wrap=tk.WORD)
        report_text.pack()

        # Disable text widget initially
        report_text.config(state=tk.DISABLED)

    def display_search_results(self, parent, results):
        # Create a new window to display search results
        results_window = tk.Toplevel(parent)
        results_window.title("Search Results")

        # Create a text widget to display the search results
        results_text = tk.Text(results_window, wrap=tk.WORD)
        results_text.pack()

        if results:
            # Insert the search results into the text widget
            for car in results:
                results_text.insert(tk.END, "Make: " + car['Make'] + "\n")
                results_text.insert(tk.END, "Model: " + car['Model'] + "\n")
                results_text.insert(tk.END, "Year: " + car['Year'] + "\n")
                results_text.insert(tk.END, "Price: " + str(car['Price']) + "\n\n")

            # Disable text widget to make it read-only
            results_text.config(state=tk.DISABLED)
        else:
            # Display a message if no results found
            results_text.insert(tk.END, "No matching cars found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarDealershipApp(root)
    root.mainloop()


# In[ ]:




