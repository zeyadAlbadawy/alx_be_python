def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter The Item to add ").strip()
            shopping_list.append(item)
            print(f"{item} has been added successfully to the shopping list")

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter The Item To Remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"The {item} has been deleted succcesfully")
            else:
                print(f"The {item} was not found in the shopping list")

        elif choice == '3':
            # Display the shopping list
            if shopping_list: 
                print("The current Shopping list items are :")
                for idx, item in enumerate(shopping_list, start = 1):
                    print(f"{idx}, {item}")
            else:
                print("you shopping list is empty")
                
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
