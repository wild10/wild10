
# Clase Padre.
class Animal:
    def __init__(self,name):
        self.name = name 
    
    def info(self):
        print(f"Animal name: {self.name}")

# Clase heredada.
class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks")
    
if __name__=='__main__':
    # Instance the main class
    my_doggy = Dog("Yango")
    my_doggy.info()     # Inherited method
    my_doggy.sound()