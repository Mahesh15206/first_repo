def add(x, y):
    return x + y

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    choice = input("Choose an operation: ")

    if choice == '1':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", add(a, b))
    elif choice == '2':
        print("Subtraction selected (Not implemented)")

if __name__ == "__main__":
    main()