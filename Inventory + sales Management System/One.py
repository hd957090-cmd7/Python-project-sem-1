import os
import pandas as pd

# File names
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INV_FILE = os.path.join(BASE_DIR,"inventory.csv")
SALES_FILE = os.path.join(BASE_DIR,"sales.csv")

if not os.path.exists(INV_FILE) or os.path.getsize(INV_FILE) == 0:
  df_inv = pd.DataFrame(columns=["ID", "Name", "Stock", "Price"])
  df_inv.to_csv(INV_FILE, index=False)

if not os.path.exists(SALES_FILE):
  df_sales = pd.DataFrame(columns=["ID", "Quantity", "Amount"])
  df_sales.to_csv(SALES_FILE, index=False)


# 1. Add Item Function
def add_item():
  df = pd.read_csv(INV_FILE)

  name = input("Enter item name: ")
  stock = int(input("Enter stock quantity: "))
  price = int(input("Enter price: "))

  # ID generate
  if len(df) == 0:
    new_id = "I101"
  else:
    last_id = df["ID"].iloc[-1]  # Jaise 'I101'
    num = int(last_id[1:]) + 1  # 101 + 1 = 102
    new_id = "I" + str(num)

  # Make Dictionary and add in dataframe 
  new_row = {"ID": new_id, "Name": name, "Stock": stock, "Price": price}
  df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
  df.to_csv(INV_FILE, index=False)

  print("\nItem added.")
  print(f"ID: {new_id} | {name} | Stock: {stock} | Price: {price}")


# 2. Sell Item Function
def sell_item():
  df_inv = pd.read_csv(INV_FILE)
  df_sales = pd.read_csv(SALES_FILE)

  item_id = input("Enter Item ID to sell: ").upper()

  if item_id not in df_inv["ID"].values:
    print(f"Item ID {item_id} not found.")
    return

  qty = int(input("Enter quantity to sell: "))

  # Item details
  idx = df_inv[df_inv["ID"] == item_id].index[0]
  name = df_inv.loc[idx, "Name"]
  current_stock = int(df_inv.loc[idx, "Stock"])
  price = int(df_inv.loc[idx, "Price"])

  # Stock check 
  if qty > current_stock:
    print(f"Not enough stock. Available: {current_stock}")
    return

  new_stock = current_stock - qty
  df_inv.loc[idx, "Stock"] = new_stock
  df_inv.to_csv(INV_FILE, index=False)

  # Sale record in sales.csv
  amount = qty * price
  new_sale = {"ID": item_id, "Quantity": qty, "Amount": amount}
  df_sales = pd.concat([df_sales, pd.DataFrame([new_sale])], ignore_index=True)
  df_sales.to_csv(SALES_FILE, index=False)

  print(f"\nSale recorded: {name} x{qty} = {amount}")
  if new_stock == 0:
    print("Stock left: 0 | Item is now out of stock.")
  else:
    print(f"Stock left: {new_stock}")


# 3. Update Item Function
def update_item():
  df = pd.read_csv(INV_FILE)
  item_id = input("Enter Item ID to update: ").upper()

  if item_id not in df["ID"].values:
    print(f"Item ID {item_id} not found.")
    return

  idx = df[df["ID"] == item_id].index[0]
  new_stock = int(input("Enter new stock: "))
  new_price = int(input("Enter new price: "))

  df.loc[idx, "Stock"] = new_stock
  df.loc[idx, "Price"] = new_price
  df.to_csv(INV_FILE, index=False)

  print("Item updated successfully!")


# 4. Delete Item Function
def delete_item():
  df = pd.read_csv(INV_FILE)
  item_id = input("Enter Item ID to delete: ").upper()

  if item_id not in df["ID"].values:
    print(f"Item ID {item_id} not found.")
    return

  df = df[df["ID"] != item_id]
  df.to_csv(INV_FILE, index=False)

  print(f"Item {item_id} deleted successfully!")


# 5. Sales Report Function (Using groupby)
def sales_report():
  df_inv = pd.read_csv(INV_FILE)
  df_sales = pd.read_csv(SALES_FILE)

  if len(df_sales) == 0:
    print("No sales recorded yet.")
    return

  grouped = (
      df_sales.groupby("ID")[["Quantity", "Amount"]].sum().reset_index()
  )

  print("\n--- SALES REPORT ---")
  total_revenue = 0
  best_seller_name = ""
  max_units = 0

  for i in range(len(grouped)):
    item_id = grouped.loc[i, "ID"]
    units = int(grouped.loc[i, "Quantity"])
    rev = int(grouped.loc[i, "Amount"])

    item_row = df_inv[df_inv["ID"] == item_id]
    if len(item_row) > 0:
      name = item_row["Name"].values[0]
    else:
      name = item_id

    print(f"{name}: {units} units | Revenue: {rev}")

    total_revenue += rev
    if units > max_units:
      max_units = units
      best_seller_name = name

  print(f"Total revenue: {total_revenue}")
  print(f"Best seller: {best_seller_name} ({max_units} units)")


# Main Menu Loop
while True:
  print("\n--- INVENTORY & SALES MENU ---")
  print("1. Add item")
  print("2. Sell")
  print("3. Update")
  print("4. Delete")
  print("5. Sales report")
  print("6. Exit")

  choice = input("Enter your choice (1-6): ")

  if choice == "1":
    add_item()
  elif choice == "2":
    sell_item()
  elif choice == "3":
    update_item()
  elif choice == "4":
    delete_item()
  elif choice == "5":
    sales_report()
  elif choice == "6":
    print("Exiting program. Goodbye!")
    break
  else:
    print("Invalid choice! Please enter 1 to 6.")