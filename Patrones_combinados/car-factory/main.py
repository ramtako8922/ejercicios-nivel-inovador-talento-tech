import car
if __name__ == "__main__":
    car_shop1 = car.CarShop()
    car_shop2 = car.CarShop()

    # Both car_shop1 and car_shop2 are the same instance
    print(car_shop1 is car_shop2)

    # Set the car factory for car_shop1
    car_shop1.set_car_factory(car.SportCarFactory())

    # Manufacture a car using car_shop1
    car1 = car_shop1.manufacture_car()
    car1.start()

    # Set the car factory for car_shop2
    car_shop2.set_car_factory(car.FlyingCarFactory())

    # Manufacture a car using car_shop2
    car2 = car_shop2.manufacture_car()
    car2.start()
