#ShoppingListMaker

def add_item(shopping_list):
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the list.")

def remove_item(shopping_list):
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")

def print_list(shopping_list):
    print("Your shopping list:")
    for item in shopping_list:
        print(f"- {item}")

def shopping_list_maker():
    shopping_list = []
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Print list")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Exiting shopping list maker.")
            break
        else:
            print("Invalid choice. Please try again.")

shopping_list_maker()
