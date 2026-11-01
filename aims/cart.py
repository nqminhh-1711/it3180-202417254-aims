class Cart:
    MAX_NUMBERS_ORDERED = 20

    def __init__(self):
        self.items = []

    def add_digital_video_disc(self, disc):
        if len(self.items) >= self.MAX_NUMBERS_ORDERED:
            return False
        self.items.append(disc)
        return True

    def total_cost(self):
        return sum(item.cost for item in self.items)
    
    def print_cart(self):
        print("***********************CART***********************")
        print("Ordered Items:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. DVD - {item.title} - {item.category} - {item.director} - {item.length}: {item.cost} $")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("***************************************************")
