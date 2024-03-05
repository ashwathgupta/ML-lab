def list_to_string(lst):
    return ' '.join(map(str, lst))

def list_to_tuple(lst):
    return tuple(lst)

def main():
    while True:
        print("\nMenu:")
        print("1. Convert list to string")
        print("2. Convert list to tuple")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                elements = input("Enter space-separated elements of the list: ").split()
                lst = list(map(int, elements))
                string_rep = list_to_string(lst)
                print("List converted to string:", string_rep)
            except ValueError:
                print("Invalid input! Please enter valid elements for the list.")
        elif choice == "2":
            try:
                elements = input("Enter space-separated elements of the list: ").split()
                lst = list(map(int, elements))
                tuple_rep = list_to_tuple(lst)
                print("List converted to tuple:", tuple_rep)
            except ValueError:
                print("Invalid input! Please enter valid elements for the list.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
'''Menu:
1. Convert list to string
2. Convert list to tuple
3. Exit
Enter your choice: 1
Enter space-separated elements of the list: 1 2 3 4 5
List converted to string: 1 2 3 4 5

Menu:
1. Convert list to string
2. Convert list to tuple
3. Exit
Enter your choice: 2
Enter space-separated elements of the list: 1 2 3 4 5
List converted to tuple: (1, 2, 3, 4, 5)

Menu:
1. Convert list to string
2. Convert list to tuple
3. Exit
Enter your choice: 3
Exiting the program.
'''