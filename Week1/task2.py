RATE = 0.008

try:
    #get the money saved every month
    money = int(input("Please enter the money you want to save every month:"))
    total_money = money * 12
    #Calculate the interest
    interest = total_money * RATE
    #Calculate the total money
    final_money = total_money + interest

    print(f"The amount saved every year:{total_money}")
    print(f"The total money:{final_money}")

except:
    print("Invalid amount")