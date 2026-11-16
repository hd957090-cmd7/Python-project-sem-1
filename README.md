# Python-project-sem-1
                                                   Project Summary: Inventory + Sales Management System
1. Project Overview
    -This is a console-based Python application developed to manage store inventory and record customer sales. It uses CSV files (inventory.csv and sales.csv) for         persistent data storage and the Pandas library for efficient data handling and reporting.
2. Key Features Implemented
    -Auto ID Generation & Add Item: When adding a new product, the system automatically generates sequential unique IDs starting from I101 (I101, I102, etc.) and           stores the item details (ID, Name, Stock, Price) in inventory.csv.
    -CRUD Operations: Separate modular functions were implemented to Add, Update (stock and price), and Delete items from the inventory.
    -Sales Processing & Stock Validation: During a sale, the program verifies whether the Item ID exists and checks if sufficient stock is available. Upon a valid         sale, it deducts the sold quantity from the inventory, logs the transaction in sales.csv, and displays an "Item is now out of stock" alert if the stock reaches         zero.
    -Sales Report using groupby(): The reporting module uses Pandas' groupby() function to aggregate sales data and display total units sold, revenue per item,             overall total revenue, and the best-selling product.
3. Difficulties Faced & How They Were Solved 
    -Library Dependency Error (ModuleNotFoundError): Initially, the script failed to execute because the Pandas library was not installed in the Python environment.        This was resolved by installing the package via the terminal using pip install pandas.
    -Empty CSV File & Directory Path Issues: Running the script from a parent directory or having blank (0-byte) CSV files caused Pandas to throw file-reading             errors. This was fixed by using Python's os.path module to dynamically locate the script's exact folder and adding a file-size check (os.path.getsize() == 0) to       automatically initialize column headers whenever a file is missing or empty.
     -Handling Edge Cases & Invalid Inputs: To prevent the application from crashing when a user enters a non-existent Item ID (such as I999) or attempts to sell            more units than available in stock, conditional if-else validation checks were added before updating any records.
    -Data Aggregation for Reporting: Combining multiple sales transactions for the same product and matching Item IDs with product names from inventory.csv required         careful indexing and grouping using groupby().
4. Conclusion
    **This project successfully demonstrates core Python programming concepts—including functions, loops, dictionaries, and file handling—alongside data analysis using Pandas. All normal, boundary, and invalid input test cases execute smoothly with accurate outputs.**
