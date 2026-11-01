import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_add_dvd_until_full(self):
        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i}", "Animation", "Director", 90, 10.0)
            self.assertTrue(self.cart.add_digital_video_disc(dvd))
        dvd21 = DigitalVideoDisc("DVD 21", "Animation", "Director", 90, 10.0)
        self.assertFalse(self.cart.add_digital_video_disc(dvd21))

    def test_total_cost(self):
        dvd1 = DigitalVideoDisc("DVD 1", cost=10.0)
        dvd2 = DigitalVideoDisc("DVD 2", cost=20.0)
        self.cart.add_digital_video_disc(dvd1)
        self.cart.add_digital_video_disc(dvd2)
        self.assertEqual(self.cart.total_cost(), 30.0)

    def test_total_cost_with_discount(self):
        dvd = DigitalVideoDisc("DVD 1", cost=100.0)
        self.cart.add_digital_video_disc(dvd)
        self.assertEqual(self.cart.total_cost_with_discount(20), 80.0)

    def test_total_cost_with_discount_invalid_percent(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)

    def test_sort_by_title(self):
        dvd1 = DigitalVideoDisc("Zebra", cost=10.0)
        dvd2 = DigitalVideoDisc("Apple", cost=20.0)
        self.cart.add_digital_video_disc(dvd1)
        self.cart.add_digital_video_disc(dvd2)
        self.cart.sort_by_title()
        self.assertEqual(self.cart.items[0].title, "Apple")
        self.assertEqual(self.cart.items[1].title, "Zebra")

    def test_sort_by_cost(self):
        dvd1 = DigitalVideoDisc("Expensive", cost=50.0)
        dvd2 = DigitalVideoDisc("Cheap", cost=10.0)
        self.cart.add_digital_video_disc(dvd1)
        self.cart.add_digital_video_disc(dvd2)
        self.cart.sort_by_cost()
        self.assertEqual(self.cart.items[0].cost, 10.0)
        self.assertEqual(self.cart.items[1].cost, 50.0)

    def test_search_by_category(self):
        dvd = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95)
        results = search_by_category([dvd], "animation")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")

if __name__ == "__main__":
    unittest.main()
