class Car(object):
    def __init__(self, colour,reg):
        self.colour= colour
        self.reg =reg
        self.speed= 0
    def accelerate(self):
        self.speed += 1
        
    def brake(self):
        self.speed -= 1
        if  self.speed < 0:
            self.speed = 0

class SportsCar (Car):
    def accelerate(self):
        self.speed += 2

