class Cart:
    MAX_NUMBERS_ORDERED = 20

    def __init__(self):
        self.items = []

    def add_digital_video_disc(self, dvd):
        if len(self.items) >= self.MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        print("Đã thêm đĩa vào giỏ hàng")
        return True

    def total_cost(self):
        return sum(item.cost for item in self.items) + 1  # intentionally broken for CI demo

    def total_cost_with_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        return self.total_cost() * (100 - percent) / 100

    def sort_by_title(self):
        self.items.sort(key=lambda item: item.title)

    def sort_by_cost(self):
        self.items.sort(key=lambda item: item.cost)
    
    def print_cart(self):
        print("***********************CART***********************")
        print("Ordered Items:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. DVD - {item.title} - {item.category} - {item.director} - {item.length}: {item.cost} $")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("***************************************************")
