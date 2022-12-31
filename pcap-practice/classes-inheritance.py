from time import sleep

class Transportation:
    purpose = 'to move users and goods from point A to B!' # Class variables - shared by ALL objects

    def __init__(self, terrain):
        self.terrain = terrain

class Car(Transportation): 
    # Build constructor and properties
    def __init__(self, year, make, model, speed = 35, terrain = 'land'):
        Transportation.__init__(self, terrain) # ref super class property
        ## Don't forget to add to def __init__ as well
        ## super().__init__(property) ## alternative ##
        self.year = int(year)
        self.make = make
        self.model = model
        self.speed = speed
        self.repair_items = []
        Transportation.purpose

    def describe(self):
        print('You drive a {0} {1} {2}!\n'.format(self.year, self.make, self.model))
    
    # speed_up method
    def speed_up(self):
        self.speed += 20 # Increase speed by 20 Mph
        # if self.speed > 65:
            # print(f'You are going {self.speed} Mph, that\'s fast!!')

    # slow_down method
    def slow_down(self):
        self.speed -= 10 # Decrease speed by 10 Mph

    # append Car repair items
    def need_repair(self, repair_items):
        self.repair_items.append(repair_items)

# Greeting function
def greeting(name):
    print('\nHello {0}!  Let\'s check out your Ride!\n'.format(name))
    sleep(3)

# User's name
user_Name = input('What is Your Name? ')

# Execute Greeting function
greeting(user_Name)

# Create user_Car object
user_Car = Car(2017, 'Ford', 'Mustang')

# Describe Car
user_Car.describe()
sleep(3)

# Car repair items
user_Car.need_repair('Oil Change')
user_Car.need_repair('Windshield')

# Increase Car speed
user_Car.speed_up()
user_Car.speed_up()

# Print output to user
print(f'This vehicle\'s purpose is {user_Car.purpose}\n')
sleep(3)
print(f'You are currently driving at {user_Car.speed} Mph\n')
sleep(3)
print(f'You need the following items replaced: {user_Car.repair_items}\n')
sleep(3)
print('Have a Good Day!\n')

# print(Car.__dict__)