
import math

class Circulo:
    def __init__ (self, radio):
        self.radio = radio
        
    def area(self):
        return math.pi*math.pow(self.radio,2)
    
    
circulo=Circulo
print(f"El área del circulo es {round(circulo.area(),2)}")
