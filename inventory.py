class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
            print(f"Updated {name}: new quantity is {self.items[name]}.")
        else:
            self.items[name] = quantity
            print(f"Added {name} with quantity {quantity}.")

    def get_item(self, name):
        if name in self.items:
            return f"{name}: {self.items[name]}"
        else:
            return f"{name} not found in inventory."

    def total_quantity(self):
        total = sum(self.items.values())
        return f"Total quantity of all items: {total}"


def main():
    inventory = Inventory()

    while True:
        print("\nInventory System")
        print("1. Add Item")
        print("2. Get Item Information")
        print("3. Total Quantity of Items")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            inventory.add_item(name, quantity)

        elif choice == '2':
            name = input("Enter item name to retrieve: ")
            print(inventory.get_item(name))

        elif choice == '3':
            print(inventory.total_quantity())

        elif choice == '4':
            print("Exiting the inventory system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()