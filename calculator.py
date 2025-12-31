def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtract")
    choice = input("Choose an operation: ")

    if choice == '1':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", add(a, b))
    elif choice == '2':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", subtract(a, b))

if __name__ == "__main__":
    main()