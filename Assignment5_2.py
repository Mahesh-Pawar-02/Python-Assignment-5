# Problem Statements : Write a recursive program which display below pattern. 
i = 1

def Display(No):
    global i
    if(i <= No):
        print("i",end = "  ")
        i = i + 1
        Display(No)

def main():
    Value = int(input("Enter number : "))
    Display(Value)

if __name__ == "__main__":
    main()

# Test case : 1
# Input  : Enter number : 5
# Output : 1  2  3  4  5

# Test case : 2
# Input  : Enter number : 10
# Output : 1  2  3  4  5  6  7  8  9  10