while True:
    print("Multiplication table for a given number.")
    print("Continue")
    print("Exit")
    action = input("Continue or Exit: ")

    if action == "Exit":
        print("Program closed.")
        break

    
    
    

    if action == "Continue":
        number = int(input("Enter a number: "))
        while number <= 1:
             print("Invalid number, enter a number greater than 1.")
             number = int(input("Enter a number: "))

        for multiplier in range(1, 13):
            result = number * multiplier
            print(f"{number} x {multiplier}: {result}")
        continue

    if action != "Continue" or action != "Exit":
        print("Invalid action. Enter action again.")
        action = input("Continue or Exit: ")

        
       
       
    
    
    

    





    


    

    
  

    
    

    
             
