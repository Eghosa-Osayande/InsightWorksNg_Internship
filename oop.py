

class SuperHero:
    name = "Super Hero"

    def __init__(self, names):
        self.name = names
    
    def print_name(self):
        print(self.name)
    
    def print_name_twice(self):
        self.print_name()
        self.print_name()
   
    def fly(self):
        print('Flying')

    def laser(self):
        print('Lasering') 


clark = SuperHero('Super Man')

clark.fly()

