Car Class:

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

    def update_color(self, new_color):
        self.color = new_color
Main Program:

def main():
    # Task 2: Instantiate multiple Car objects
    car1 = Car("Toyota", "Camry", 2020, "Silver")
    car2 = Car("Honda", "Civic", 2018, "Black")

    # Display their details
    print("Car 1 Details:")
    car1.display_details()
    print("\nCar 2 Details:")
    car2.display_details()

    # Update one object's color
    car1.update_color("Blue")

    # Display the updated details
    print("\nUpdated Car 1 Details:")
    car1.display_details()

    # Task 3: Prompt user to input car details
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    color = input("Enter car color: ")

    # Create a Car object
    user_car = Car(make, model, year, color)
# Display the car's information
    print("\nUser Car Details:")
    user_car.display_details()

if __name__ == "__main__":
    main()


''' CODE EXPLANATION

- We define a Car class with attributes
 (make, model, year, color) and methods 
(display_details, update_color).

- In the main function, we instantiate 
multiple Car objects (car1, car2)
 and display their details using the display_details method.
We update one object's color using the update_color
 method and display the updated details.

- We prompt the user to input car details,
 create a new Car object with the user's input,
 and display the car's information using the display_details method.'''