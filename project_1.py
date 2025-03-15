print("Hello, welcome to your very own virtual multi-purpose calculator machine!")
print("1. Simple Interest")
print("2. Compound interest")
print("3. Annuity Plan")

collector = int(input("What would you like to calculate: "))

if collector == 1:
    print("You have selected Simple Interest")
    P = float(input("Enter the value of your principle: "))
    R = float(input("Enter the value of the rate used: "))
    T = float(input("Enter the value of the time: "))
    A = P * (1 + (R/100.0) * T)
    print(f"Simple interest Amount: N{A:.2f}")

elif collector == 2:
    print("You have selected Compound Interest")
    P = float(input("Enter the value of your principle: "))
    R = float(input("Enter the value of the rate used: "))
    n = float(input("Enter the value for n: "))
    t = float(input("Enter the value for t: "))
    A = P * ( 1 + R/n) ** (n*t)
    print(f"Compound Interest is: N{A:.2f}")

elif collector == 3:
    print("You have selected Annuity Plan")
    P = float(input("Enter the value of your principle: "))
    M = float(input("Enter the value for M: "))
    T = float(input("Enter the value of the time: "))
    R = float(input("Enter the value of the rate used: "))
    n = float(input("Enter the value for n: "))
    t = float(input("Enter the value for t: "))
    A = (P * M * T) * ((1 + R/n) ** (n*t) - 1/ (R/n))
    print(f"Annuity Plan is: N{A:.2f}")

else:
    print("Invalid selection. Please select 1, 2 or 3")

