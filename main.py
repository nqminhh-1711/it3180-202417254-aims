from aims import __version__
from aims.dvd import DigitalVideoDisc
from aims.cart import Cart

def main():
    print(f"AIMS-mini v{__version__}")
    cart = Cart()
    dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95)
    dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 124, 24.95)
    dvd3 = DigitalVideoDisc("Aladdin", "Animation", "John Musker", 90, 18.99)

    cart.add_digital_video_disc(dvd1)
    cart.add_digital_video_disc(dvd2)
    cart.add_digital_video_disc(dvd3)

    print(f"Total cost: {cart.total_cost():.2f} $")
    
    cart.print_cart()

if __name__ == "__main__":
    main()
