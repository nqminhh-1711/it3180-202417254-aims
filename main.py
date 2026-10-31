from dvd import DigitalVideoDisc
from cart import Cart

def main():
    cart = Cart()
    dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95)
    dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 124, 24.95)
    dvd3 = DigitalVideoDisc("Aladdin", "Animation", "John Musker", 90, 18.99)

    cart.add_digital_video_disc(dvd1)
    cart.add_digital_video_disc(dvd2)
    cart.add_digital_video_disc(dvd3)

    print(f"Total cost: {cart.total_cost():.2f} $")

if __name__ == "__main__":
    main()
    
"Thêm thử ghi chú"