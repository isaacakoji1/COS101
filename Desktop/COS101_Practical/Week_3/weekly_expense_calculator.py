student_name = input("Student Name: ")
budget = int(input("Enter a budget: NGN "))
if budget < 0:
    print("Budget cannot be negative. Enter a positive budget.")
    budget = int(input("Enter a budget: NGN "))
else:
    daily_transport_cost = int(input("Daily Transport Cost: NGN "))
    daily_feeding_cost = int(input("Daily Feeding Cost: NGN "))
    other_expenses = int(input("Other weekly expenses: NGN "))
    number_of_days = int(input("Number of days on campus: "))
    if daily_transport_cost < 0 or daily_feeding_cost < 0 or other_expenses < 0 or number_of_days < 0:
        print("Invalid input")
    else:
        transport_total = daily_transport_cost * number_of_days
        feeding_total = daily_feeding_cost * number_of_days
        weekly_total = transport_total + feeding_total + other_expenses
    
print("WEEKLY EXPENSE SUMMARY")
print(f"Student Name: {student_name}")
print(f"Transport total: NGN {transport_total:.2f}")
print(f"Feeding total: NGN {feeding_total:.2f}")
print(f"Other expenses: NGN {other_expenses:.2f}")
print(f"Weekly total: NGN {weekly_total:.2f}")
print(f"Budget: NGN {budget:.2f}")
if weekly_total == budget:
    budget_range = "Exactly on budget."
elif weekly_total > budget:
    budget_range = "Over budget."
    amount = weekly_total - budget
    print(f"Amount exceeded: NGN {amount:.2f}")
else:
    budget_range = "Within budget."
    amount = budget - weekly_total
    print(f"Amount remaining: NGN {amount:.2f}")


