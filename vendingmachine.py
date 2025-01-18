class Product:
    # Represents a product in the vending machine with name, category, price, and stock.
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def is_available(self):
        # Checks if the product is available in stock.
        return self.stock > 0

    def dispense(self):
        # Dispenses the product if available and reduces the stock by 1.
        if self.is_available():
            self.stock -= 1
            return True
        return False


class VendingMachine:
    # Represents the vending machine containing products and handles user interactions.
    def __init__(self):
        # Initializes the vending machine with a list of products.
        self.products = {
            "1": Product("Coffee", "Hot Beverages", 1.50, 10),
            "2": Product("Tea", "Hot Beverages", 1.20, 8),
            "3": Product("Hot Chocolate", "Hot Beverages", 1.70, 7),
            "4": Product("Water", "Cold Beverages", 1.00, 15),
            "5": Product("Juice", "Cold Beverages", 1.50, 10),
            "6": Product("Coca Cola", "Cold Beverages", 1.80, 12),
            "7": Product("Rootbeer", "Cold Beverages", 1.80, 8),
            "8": Product("Sprite", "Cold Beverages", 1.80, 9),
            "9": Product("Chips", "Snacks", 1.30, 5),
            "10": Product("Gummies", "Snacks", 1.20, 6),
            "11": Product("Chocolate", "Snacks", 1.80, 7),
            "12": Product("Apple", "Snacks", 1.00, 10),
        }

    def display_menu(self):
        # Displays the vending machine menu, categorized by product type.
        print("\n--- Vending Machine Menu ---")
        categories = {}
        for code, product in self.products.items():
            if product.category not in categories:
                categories[product.category] = []
            categories[product.category].append((code, product))

        for category, items in categories.items():
            print(f"\n{category}:")
            for code, product in items:
                availability = "(Out of Stock)" if not product.is_available() else ""
                print(f" {code}: {product.name} - ${product.price:.2f} {availability}")

    def get_change(self, amount_paid, price):
        # Calculates and returns the change to be given to the user.
        return round(amount_paid - price, 2)

    def suggest_purchase(self, selected_product):
        # Suggests other products in the same category to the user.
        suggestions = [
            p.name
            for p in self.products.values()
            if p.category == selected_product.category and p.name != selected_product.name and p.is_available()
        ]
        if suggestions:
            print(f"Suggestion: Why not try {suggestions[0]} as well?")

    def handle_purchase(self):
        # Handles a single purchase transaction.
        self.display_menu()
        choice = input("\nEnter the code of the item you want to purchase: ")

        if choice not in self.products:
            # Handles invalid product code selection.
            print("Invalid selection. Please try again.")
            return

        product = self.products[choice]

        if not product.is_available():
            # Informs the user if the selected product is out of stock.
            print(f"Sorry, {product.name} is out of stock.")
            return

        try:
            # Prompts the user to insert money for the selected product.
            amount_paid = float(input(f"Please insert ${product.price:.2f}: "))
        except ValueError:
            # Handles invalid monetary input.
            print("Invalid amount entered. Transaction cancelled.")
            return

        if amount_paid < product.price:
            # Checks if the user has inserted sufficient funds.
            print(f"Insufficient funds. Please insert at least ${product.price:.2f}.")
            return

        if product.dispense():
            # Dispenses the product and calculates the change.
            change = self.get_change(amount_paid, product.price)
            print(f"Dispensing {product.name}...")
            print(f"Transaction complete. Your change is ${change:.2f}.")
            self.suggest_purchase(product)
        else:
            # Handles cases where the product could not be dispensed.
            print(f"Sorry, {product.name} could not be dispensed.")

    def start(self):
        # Starts the vending machine, allowing the user to make purchases.
        while True:
            print("\nHello!! Luigi's Vending Machine, what do you have in mind?")
            self.handle_purchase()
            cont = input("Would you like to buy another item? (yes/no): ").strip().lower()
            if cont != "yes":
                # Exits the vending machine if the user chooses not to continue.
                print("Thank you for using Luigi's Vending Machine. Goodbye!")
                break


if __name__ == "__main__":
    # Creates an instance of the VendingMachine class and starts it.
    vending_machine = VendingMachine()
    vending_machine.start()