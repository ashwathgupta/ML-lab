def find_largest_smallest_builtin(t):
    largest_builtin = max(t)
    smallest_builtin = min(t)
    return largest_builtin, smallest_builtin

def find_largest_smallest(t):
    largest = t[0]
    smallest = t[0]
    for item in t:
        if item > largest:
            largest = item
        if item < smallest:
            smallest = item
    return largest, smallest

def main():
    while True:
        print("\nMenu:")
        print("1. Find largest and smallest item in tuple using built-in functions")
        print("2. Find largest and smallest item in tuple without using built-in functions")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                elements = input("Enter space-separated elements of the tuple: ").split()
                t = tuple(map(int, elements))
                largest_builtin, smallest_builtin = find_largest_smallest_builtin(t)
                print("Largest item using built-in functions:", largest_builtin)
                print("Smallest item using built-in functions:", smallest_builtin)
            except ValueError:
                print("Invalid input! Please enter integers only.")
        elif choice == "2":
            try:
                elements = input("Enter space-separated elements of the tuple: ").split()
                t = tuple(map(int, elements))
                largest, smallest = find_largest_smallest(t)
                print("Largest item without using built-in functions:", largest)
                print("Smallest item without using built-in functions:", smallest)
            except ValueError:
                print("Invalid input! Please enter integers only.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()




