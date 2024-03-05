def create_array(size):
    return [0] * size

def display_array(arr):
    print("Array:", arr)

def insert_element(arr, index, element):
    arr.insert(index, element)
    print("Element", element, "inserted at index", index)

def delete_element(arr, index):
    if index < 0 or index >= len(arr):
        print("Invalid index")
        return
    deleted_element = arr.pop(index)
    print("Deleted element:", deleted_element)

def update_element(arr, index, new_element):
    if index < 0 or index >= len(arr):
        print("Invalid index")
        return
    arr[index] = new_element
    print("Element at index", index, "updated to", new_element)

if __name__ == "__main__":
    size = int(input("Enter the size of the array: "))
    arr = create_array(size)

    while True:
        print("\nArray Operations:")
        print("1. Display Array")
        print("2. Insert Element")
        print("3. Delete Element")
        print("4. Update Element")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_array(arr)
        elif choice == 2:
            index = int(input("Enter the index to insert at: "))
            element = int(input("Enter the element to insert: "))
            insert_element(arr, index, element)
        elif choice == 3:
            index = int(input("Enter the index to delete: "))
            delete_element(arr, index)
        elif choice == 4:
            index = int(input("Enter the index to update: "))
            new_element = int(input("Enter the new element: "))
            update_element(arr, index, new_element)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
