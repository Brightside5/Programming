# You've been asked to analyse a set of sales data which you can find in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

# for a challenge - add a menu so the user picks which piece of data to show

# Additional hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows
import csv

try:
    with open("sales.csv", "r") as infile:
        rawdata = csv.reader(infile)
        next(rawdata)  # Skip header
        
        # Initialize variables
        max_sale = 0
        max_date = ""
        total_sales = 0
        count = 0
        product_units = {}
        
        for row in rawdata:
            date, product, sales_amount_str, units_sold_str, region = row
            sales_amount = int(sales_amount_str)
            units_sold = int(units_sold_str)
            
            # Update max sale day
            if sales_amount > max_sale:
                max_sale = sales_amount
                max_date = date
            
            # Accumulate for average
            total_sales += sales_amount
            count += 1
            
            # Update product units sold
            if product not in product_units:
                product_units[product] = 0
            product_units[product] += units_sold
        
        # Calculate average
        average_sale = total_sales / count if count > 0 else 0
        
        # Find most sold widget
        if product_units:
            most_sold_product = max(product_units, key=product_units.get)
            most_units = product_units[most_sold_product]
        else:
            most_sold_product = "None"
            most_units = 0
        
        # Menu loop
        while True:
            print("\n请选择要查看的数据：")
            print("1. 最大销售日")
            print("2. 平均销售金额")
            print("3. 最畅销的产品")
            print("4. 退出")
            choice = input("输入选择 (1-4): \n")
            
            if choice == "1":
                print(f"最大销售日是 {max_date}，销售金额为 {max_sale} 元。")
            elif choice == "2":
                print(f"平均销售金额为 {average_sale:.2f} 元。")
            elif choice == "3":
                print(f"最畅销的产品是 {most_sold_product}，销售了 {most_units} 个单位。")
            elif choice == "4":
                print("退出程序。")
                break
            else:
                print("无效选择，请重新输入。")

except FileNotFoundError:
    print("The file doesn't exist")
except Exception as e:
    print(f"Error:{e}")