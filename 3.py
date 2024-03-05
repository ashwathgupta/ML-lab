def print_tuple_items(t):
    print("Tuple items:", t)

def tuple_length(t):
    print("Tuple length:", len(t))

def main():
    while True:
        print("\nMenu:")
        print("1. Print tuple items")
        print("2. Print tuple length")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                elements = input("Enter space-separated elements of the tuple: ").split()
                t = tuple(elements)
                print_tuple_items(t)
            except ValueError:
                print("Invalid input! Please enter valid elements for the tuple.")
        elif choice == "2":
            try:
                elements = input("Enter space-separated elements of the tuple: ").split()
                t = tuple(elements)
                tuple_length(t)
            except ValueError:
                print("Invalid input! Please enter valid elements for the tuple.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
