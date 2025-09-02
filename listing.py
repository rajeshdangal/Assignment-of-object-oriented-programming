class Listing:
    def __init__(self, address: str, price: float, bedrooms: int, bathrooms: int, square_feet: float):
        self.address = address
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.square_feet = square_feet

    def __str__(self):
        return (f"Address: {self.address}\n"
                f"Price: ${self.price:,.2f}\n"
                f"Bedrooms: {self.bedrooms}\n"
                f"Bathrooms: {self.bathrooms}\n"
                f"Square Feet: {self.square_feet:,.0f}")