# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self.brand = brand
        self.model = model
        self._storage = storage  # Encapsulation: Storage as a protected attribute
        self.battery_capacity = battery_capacity

    def get_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self._storage}GB, Battery: {self.battery_capacity}mAh"

    def charge(self):
        print(f"The {self.model} is charging... 🔋")

    def install_app(self, app_name):
        print(f"Installing {app_name} on the {self.model}... 📱")

    def get_storage(self):
        return f"Available storage: {self._storage}GB"

# Subclass: GamingSmartphone (inherits from Smartphone)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, gpu):
        super().__init__(brand, model, storage, battery_capacity)
        self.gpu = gpu

    def get_specs(self):
        base_specs = super().get_specs()
        return f"{base_specs}, GPU: {self.gpu}"

    def game_mode(self):
        print(f"Activating Game Mode on {self.model}... 🎮 Boosting GPU: {self.gpu}")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S25 Ultra", 256, 5000)
print(phone1.get_specs())
phone1.charge()
phone1.install_app("WhatsApp")

gaming_phone = GamingSmartphone("ASUS", "ROG Phone 5", 256, 6000, "Adreno 660")
print(gaming_phone.get_specs())
gaming_phone.game_mode()
gaming_phone.charge()




#Activity Two: Polymorphism
# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # This will be overridden in each subclass

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road... 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky... ✈️")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing on the water... 🚤")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Polymorphism: Each class defines move() differently
