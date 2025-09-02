from listing import Listing

class ListingManager:
    def __init__(self):
        self.listings = []

    def add_listing(self, listing: Listing):
        self.listings.append(listing)

    def remove_listing(self, index: int):
        if 0 <= index < len(self.listings):
            return self.listings.pop(index)
        return None

    def get_listing(self, index: int):
        if 0 <= index < len(self.listings):
            return self.listings[index]
        return None

    def get_all_listings(self):
        return self.listings