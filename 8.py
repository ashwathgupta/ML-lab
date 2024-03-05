class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, root):
        if root:
            self._inorder_recursive(root.left)
            print(root.key, end=" ")
            self._inorder_recursive(root.right)

if __name__ == "__main__":
    bst = BinarySearchTree()

    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Search")
        print("3. Inorder Traversal")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key to insert: "))
            bst.insert(key)
            print("Key", key, "inserted into the tree.")
        elif choice == 2:
            key = int(input("Enter key to search: "))
            if bst.search(key):
                print("Key", key, "found in the tree.")
            else:
                print("Key", key, "not found in the tree.")
        elif choice == 3:
            print("Inorder Traversal:")
            bst.inorder_traversal()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
