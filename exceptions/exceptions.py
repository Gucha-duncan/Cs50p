

try:
    x = int(input("Enter the value of x: "))
    
    
except ValueError:
    print("Enter an integer only!")
    
else:
    print(f"The entered value of x is : {x}")