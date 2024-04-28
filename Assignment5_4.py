# Problem Statements : Write a recursive program which accept number from user and return summation of its digits.

def SumDigit(No):
    Sum = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
    return Sum

def main():
    Value = int(input("Enter number : "))

    Ret = SumDigit(Value)

    print("Summation of its Digits: ", Ret)

if __name__ == "__main__":
    main()

# Test case : 1
# Input  : Enter number : 879
# Output : 24

# Test case : 2
# Input  : Enter number : 9322
# Output : 16