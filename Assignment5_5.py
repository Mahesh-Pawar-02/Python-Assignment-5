# Problem Statements : Write a recursive program which accept number from user and return its factorial. 

i = 1
Fact = 1

def Factorial(No):
    global i
    global Fact

    if(No >= 1):
        Fact = Fact * No
        No = No - 1
        Factorial(No)
    return Fact

def main():
    Value = int(input("Enter number : "))

    Ret = Factorial(Value)

    print("Factorial is : ", Ret)

if __name__ == "__main__":
    main()

# Test case : 1
# Input  : Enter number : 5
# Output : 120

# Test case : 2
# Input  : Enter number : 4
# Output : 24