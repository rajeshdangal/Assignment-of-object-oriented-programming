from listing import Listing
from listing_manager import ListingManager
from property_manager import PropertyManager
from property import Property

def main():
    manager = ListingManager()

    for listing in Property.get_sample_listings():
        manager.add_listing(listing)

    property_manager = PropertyManager(manager)
    property_manager.run()

if __name__ == "__main__":
    main()