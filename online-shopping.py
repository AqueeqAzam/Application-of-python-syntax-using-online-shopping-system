# Importing modules (Element: Import Statement)
import datetime

# Defining classes (Element: Class Definition)
import datetime

# Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.products = []
        self.discount = 0  # Store discount percentage

    def add_product(self, name, price, quantity):
        for product in self.products:
            if product.name == name:  # If product already exists, update quantity
                product.quantity += quantity
                return
        self.products.append(Product(name, price, quantity))

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"{product_name} removed from cart.")
                return
        print("Product not found in cart!")

    def view_cart(self):
        if not self.products:
            print("Your shopping cart is empty.")
            return
        print("\nShopping Cart:")
        for product in self.products:
            print(f"{product.name} x {product.quantity} = ${product.price * product.quantity:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

    def calculate_total(self):
        total = sum(product.price * product.quantity for product in self.products)
        total -= total * self.discount  # Apply discount if any
        return total

    def apply_discount(self, discount_code):
        discounts = {"10OFF": 0.1, "20OFF": 0.2}
        if discount_code in discounts:
            self.discount = discounts[discount_code]
            print(f"Discount applied: {self.discount * 100}%")
        else:
            print("Invalid discount code!")

    def generate_receipt(self):
        if not self.products:
            print("No products in cart. Cannot generate receipt.")
            return
        print("\n--- Shopping Receipt ---")
        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for product in self.products:
            print(f"{product.name} x {product.quantity} = ${product.price * product.quantity:.2f}")
        print(f"Discount Applied: {self.discount * 100}%")
        print(f"Total: ${self.calculate_total():.2f}")
        print("------------------------")

# Main function
def main():
    cart = ShoppingCart()

    while True:
        print("\nOnline Shopping Cart System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Calculate Total")
        print("5. Apply Discount")
        print("6. Generate Receipt")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            cart.add_product(name, price, quantity)
            print(f"{quantity} {name}(s) added to cart.")

        elif choice == "2":
            product_name = input("Enter product name to remove: ")
            cart.remove_product(product_name)

        elif choice == "3":
            cart.view_cart()

        elif choice == "4":
            print(f"Total: ${cart.calculate_total():.2f}")

        elif choice == "5":
            discount_code = input("Enter discount code: ")
            cart.apply_discount(discount_code)

        elif choice == "6":
            cart.generate_receipt()

        elif choice == "7":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
