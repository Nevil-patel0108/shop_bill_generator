# Shop bill program with GST
# This program takes items from the user, asks for the bill type,
# adds GST (CGST + SGST) and prints the final bill.

total_amount = 0   # stores the total of all items (before GST)
items = []         # list to store details of every item

# ---------- taking items from user ----------
while True:
    item = input("Enter item name: ")

    # keep asking until user enters a valid quantity
    while True:
        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                # quantity must be at least 1
                print("Quantity should be more than 0")
                continue
            break  # valid quantity, come out of this loop
        except ValueError:
            # runs when user types text like "abc" instead of a number
            print("Please enter a number")

    # keep asking until user enters a valid price
    while True:
        try:
            price = float(input("Enter price per item: "))
            if price < 0:
                # price can be 0 but not negative
                print("Price can't be negative")
                continue
            break  # valid price, come out of this loop
        except ValueError:
            # runs when user types something that is not a number
            print("Please enter a valid price")

    total = qty * price          # total for this one item
    total_amount += total        # add it to the overall bill amount
    items.append((item, qty, price, total))  # save item details

    # ask if user wants to add another item
    choice = input("Do you want to add more items? (yes/no): ").lower().strip()
    if choice != "yes" and choice != "y":
        break  # stop taking items

# ---------- choosing the bill type ----------
# showing the bill types with their GST rates
print("\n1. Hotel (3%)")
print("2. Electronics (18%)")
print("3. Grocery (5%)")
print("4. Clothing (12%)")
print("5. Stationery (18%)")
print("6. Medical (5%)")

rate = 0  # GST rate will be set according to user's choice
while True:
    try:
        gst_choice = int(input("Choose bill variant (1-6): "))
    except ValueError:
        # user typed text instead of a number
        print("Please enter a number between 1 and 6")
        continue

    # set the GST rate based on the chosen bill type
    if gst_choice == 1:
        print("You have chosen hotel bill")
        rate = 0.03
    elif gst_choice == 2:
        print("You have chosen electronics bill")
        rate = 0.18
    elif gst_choice == 3:
        print("You have chosen grocery bill")
        rate = 0.05
    elif gst_choice == 4:
        print("You have chosen clothing bill")
        rate = 0.12
    elif gst_choice == 5:
        print("You have chosen stationery bill")
        rate = 0.18
    elif gst_choice == 6:
        print("You have chosen medical bill")
        rate = 0.05
    else:
        # number is outside 1-6, ask again
        print("Invalid choice, try again")
        continue
    break  # valid choice, stop asking

# ---------- calculating gst ----------
GST = total_amount * rate      # total GST amount
CGST = GST / 2                 # central GST is half of total GST
SGST = GST / 2                 # state GST is the other half
grand_total = total_amount + GST  # final amount to pay

# ---------- printing the bill ----------
print("\n      *** SHOP BILL ***")
print("-" * 46)
# table heading (< means left align, > means right align)
print(f"{'Item':<18}{'Qty':>6}{'Price':>10}{'Total':>12}")
print("-" * 46)

# print every item in a row
for i in items:
    name = i[0]
    # cut the name if it is too long, so the table doesn't break
    if len(name) > 17:
        name = name[:14] + "..."
    print(f"{name:<18}{i[1]:>6}{i[2]:>10.2f}{i[3]:>12.2f}")

print("-" * 46)
# .2f means show only 2 digits after the decimal point
print(f"Subtotal : {total_amount:.2f}")
print(f"CGST     : {CGST:.2f}")
print(f"SGST     : {SGST:.2f}")
print("-" * 46)
print(f"Total Bill = {grand_total:.2f}")
print("-" * 46)
print("THANK YOU FOR VISITING OUR SHOP!")
