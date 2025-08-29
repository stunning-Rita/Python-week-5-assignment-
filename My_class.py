# Base class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def make_call(self, number):
        print(f"{self.model} is calling {number}... 📞")

    def charge(self, hours):
        self.battery_life += hours
        print(f"{self.model} charged for {hours} hours. Battery life now: {self.battery_life}h 🔋")

# Inheritance example: a specific brand
class ApplePhone(Smartphone):
    def __init__(self, model, battery_life, face_id_enabled=True):
        super().__init__("Apple", model, battery_life)
        self.face_id_enabled = face_id_enabled

    # Polymorphism: override make_call
    def make_call(self, number):
        print(f"{self.model} (Apple) is FaceTiming {number}... 📱")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", 24)
phone2 = ApplePhone("iPhone 15", 20)

phone1.make_call("123-456-7890")
phone2.make_call("987-654-3210")
phone2.charge(5)
