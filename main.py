# main.py

# This file contains a menu-driven application to perform basic data structure operations.
# Students are expected to implement missing features or enhance existing ones.

def display_menu():
    print("\nData Structure Task App")
    print("1. Stack Operations")
    print("2. Queue Operations")
    print("3. Dictionary Operations")
    print("4. Exit")

def stack_operations():
    stack = []
    print("\n-- Stack Operations --")
    while True:
        print("1. Push\n2. Pop\n3. Display\n4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter item to push: ")
            stack.append(item)
        elif choice == "2":
            if stack:
                print("Popped item:", stack.pop())
            else:
                print("Stack is empty.")
        elif choice == "3":
            print("Stack content:", stack)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def queue_operations():
    queue = []
    # TODO: Implement queue using list or collections.deque
    print("\n-- Queue Operations --")
    while True:
        print("1. enqueue\n2. dequeue\n3. Display\n4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter item to enqueue: ")
            queue.append(item)
        elif choice == "2":
            if stack:
                print("dequeued item:", queue.pop(0))
            else:
                print("queue is empty.")
        elif choice == "3":
            print("queue content:", queue)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def dictionary_operations():
    dict = {}
    print("\n-- Dictionary Operations --")
    while True:
        print("1. insert\n2. delete\n3. Display\n4. search\n5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter item : ")
            key = input("Enter key : ")
            dict[key] = item
        elif choice == "2":
            key = input("Enter key to delete: ")
            if key in dict:
                del dict[key]
                print(f"Deleted key: {key}")
            else:
                print("Key not found.")
        elif choice == "3":
            if dict:
                print("Dictionary contents:")
                for key, value in dict.items():
                    print(f"{key}: {value}")
            else:
                print("Dictionary is empty.")
        elif choice == "4":
            key = input("Enter key to search: ")
            if key in dict:
                print(f"Found: {key} => {dict[key]}")
            else:
                print("Key not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            stack_operations()
        elif choice == "2":
            queue_operations()
        elif choice == "3":
            dictionary_operations()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
