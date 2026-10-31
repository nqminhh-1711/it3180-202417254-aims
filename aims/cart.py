class Cart:
    MAX_NUMBERS_ORDERED = 20

    def __init__(self):
        self.items = []

    def add_digital_video_disc(self, disc):
        if len(self.items) > self.MAX_NUMBERS_ORDERED:
            return False
        self.items.append(disc)
        return True

    def total_cost(self):
        return sum(item.cost for item in self.items)
