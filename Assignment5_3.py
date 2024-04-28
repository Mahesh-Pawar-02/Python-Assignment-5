# Problem Statements : Write a recursive program which display below pattern. 

i = 1

def Display(No):
    global i
    if(No >= 1):
        print(No,end = "  ")
        No = No - 1
        Display(No)

def main():
    Value = int(input("Enter number : "))
    Display(Value)

if __name__ == "__main__":
    main()

# Test case : 1
# Input  : Enter number : 5
# Output : 5  4  3  2  1

# Test case : 2
# Input  : Enter number : 10
# Output : 10  9  8  7  6  5  4  3  2  1  