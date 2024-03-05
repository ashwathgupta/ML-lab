import numpy as np

def left_rotate_array(arr, n):
    n = n % len(arr)  # Handle cases where n is greater than the length of the array
    return np.concatenate((arr[n:], arr[:n]))

def right_rotate_array(arr, n):
    n = n % len(arr)  # Handle cases where n is greater than the length of the array
    return np.concatenate((arr[-n:], arr[:-n]))

# Function to display menu options
def display_menu():
    print("1. Left rotate array")
    print("2. Right rotate array")
    print("3. Exit")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                arr = np.array(input("Enter space-separated elements of the array: ").split(), dtype=int)
                n = int(input("Enter the number of positions to left rotate: "))
                rotated_arr = left_rotate_array(arr, n)
                print("Original array:", arr)
                print("Left rotated array by", n, "positions:", rotated_arr)
            except ValueError:
                print("Invalid input! Please enter integers only.")
        elif choice == "2":
            try:
                arr = np.array(input("Enter space-separated elements of the array: ").split(), dtype=int)
                n = int(input("Enter the number of positions to right rotate: "))
                rotated_arr = right_rotate_array(arr, n)
                print("Original array:", arr)
                print("Right rotated array by", n, "positions:", rotated_arr)
            except ValueError:
                print("Invalid input! Please enter integers only.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
'''1. Left rotate array
2. Right rotate array
3. Exit
Enter your choice: 1
Enter space-separated elements of the array: 1 2 3 4 5
Enter the number of positions to left rotate: 2
Original array: [1 2 3 4 5]
Left rotated array by 2 positions: [3 4 5 1 2]

1. Left rotate array
2. Right rotate array
3. Exit
Enter your choice: 2
Enter space-separated elements of the array: 1 2 3 4 5
Enter the number of positions to right rotate: 2
Original array: [1 2 3 4 5]
Right rotated array by 2 positions: [4 5 1 2 3]
1. Left rotate array
2. Right rotate array
3. Exit
Enter your choice: 3

'''
