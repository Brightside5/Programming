RATE = 0.008

try:
    #get the money saved every month
    monthly_saving_str = input()
    money = int(monthly_saving_str)
    
    total_money = money * 12
    #Calculate the interest
    interest = total_money * RATE
    #Calculate the total money
    final_money = total_money + interest

    print(total_money)
    print(f"£{final_money:.2f}")

except:
    print("Invalid amount")