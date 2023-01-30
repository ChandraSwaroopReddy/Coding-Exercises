try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    
    percent = value / total_value * 100
    
    print("That is", percent, "%")

except ValueError:
    print("You need to enter a number. Run the program again.")
    
except ZeroDivisionError:
    print("Your total value cannot be zero.")
    