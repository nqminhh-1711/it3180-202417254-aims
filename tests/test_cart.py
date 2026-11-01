import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

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

if __name__ == "__main__":
    unittest.main()
