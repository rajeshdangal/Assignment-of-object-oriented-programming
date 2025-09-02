from listing import Listing

class PropertyManager:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        while True:
            print("\nHouse Listing System")
            print("1. Print all listings")
            print("2. Print a selected listing's info")
            print("3. Purchase a house")
            print("4. Create a listing")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.print_all_listings()
            elif choice == '2':
                self.print_listing_info()
            elif choice == '3':
                self.purchase_house()
            elif choice == '4':
                self.create_listing()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def print_all_listings(self):
        listings = self.manager.get_all_listings()
        if not listings:
            print("No listings available.")
            return
        for i, listing in enumerate(listings):
            print(f"[{i}] {listing.address} - ${listing.price:,.2f}")
        input("Press Any Key to continue...")

    def print_listing_info(self):
        index = input("Enter the index of the listing to view: ")
        if not index.isdigit():
            print("Invalid input.")
            return
        listing = self.manager.get_listing(int(index))
        if listing:
            print(listing)
        else:
            print("Listing not found.")
        input("Press Any Key to continue...")

    def purchase_house(self):
        while True:
            index = input("Enter the index of the listing to purchase (or 'q' to cancel): ")
            if index.lower() == 'q':
                print("Purchase cancelled.")
                break
            if not index.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            purchased = self.manager.remove_listing(int(index))
            if purchased:
                print(f"You have purchased the house at {purchased.address} for ${purchased.price:,.2f}")
                input("\nPress Enter to return to the menu...")
                break
            else:
                print("Listing not found. Please try again.")


    def create_listing(self):
        address = input("Enter the address: ")
        price = input("Enter the price: ")
        bedrooms = input("Enter the number of bedrooms: ")
        bathrooms = input("Enter the number of bathrooms: ")
        square_feet = input("Enter the square footage: ")

        try:
            listing = Listing(
                address,
                float(price),
                int(bedrooms),
                int(bathrooms),
                float(square_feet)
            )
            self.manager.add_listing(listing)
            print("Listing created successfully.")
        except ValueError:
            print("Invalid input. Could not create listing.")