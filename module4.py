def main():
    # Step 1: Prompt the user for input N (positive integer)
    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    # Step 2: Read N numbers one by one
    numbers = []
    for i in range(N):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    # Step 3: Ask the user for input X (integer)
    while True:
        try:
            X = int(input("Enter an integer X to search: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Step 4: Check if X is in the list and print the 1-based index or -1 if not found
    try:
        index = numbers.index(X)
        print(index + 1)  # Convert 0-based index to 1-based
    except ValueError:
        print("-1")

if __name__ == "__main__":
    main()