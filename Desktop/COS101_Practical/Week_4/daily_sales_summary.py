days = int(input("Enter number of days: "))
while days <= 0:
    print("Invalid number of days. Enter a number of days greater than zero.")
    days = int(input("Enter number of days: "))

total_sales = 0
days_greater_than_10k = 0
days_less_than_10k = 0

for days in range(1, days + 1):
    sales_amount = float(input(f"Enter sales amount for day {days}: NGN "))
    while sales_amount <= 0:
        print("Enter sales amount greater than 0")
        sales_amount = float(input(f"Enter sales amount for day {days}: NGN "))
    total_sales += sales_amount

    average = total_sales/days
    
    if sales_amount >= 10000:
        days_greater_than_10k += 1
    else:
        days_less_than_10k += 1

print("DAILY SALES SUMMARY")
print(f"Total sales: NGN {total_sales:,.2f}")
print(f"Average daily sales: NGN {average:,.2f}")
print(f"Days with sales of at least NGN 10000: {days_greater_than_10k}")
print(f"Days with sales less than NGN 10000: {days_less_than_10k}")

    

    
