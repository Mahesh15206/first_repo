def subtract(x, y):
    return x - y

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    choice = input("Choose an operation: ")

    if choice == '1':
        print("Addition selected (Not implemented)")
    elif choice == '2':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", subtract(a, b))

if __name__ == "__main__":
    main()