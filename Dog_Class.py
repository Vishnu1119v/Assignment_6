class Dog:
  def __init__(self,name,age,coat_color):
    self.name=name
    self.age=age
    self.coat_color=coat_color
  def description(self):
        print(f"The name of the dog is {self.name}")
        print(f"The dog's age is {self.age}")

  def get_info(self):
        print(f"The coat color of {self.name} is {self.coat_color}")

class JackRussellTerrier(Dog):
  def weight(self, weight=16):
    self.weight = weight
    print(f"The weight of {self.name} is {self.weight} pounds")
  def life_span(self, lifespan):
    self.lifespan = lifespan
    print(f"The lifespan of {self.name} is {self.lifespan} years")
class Bulldog(Dog):
  def __init__(self, name, age, coat_color):
    super().__init__(name, age, coat_color)
  def color(self,color):
    self.color = color
    print(f"The color of {self.name} is {self.color}")

  def bark(self, bark,gender):
    self.bark = bark
    self.gender=gender
    super().get_info()
    print(f"{self.name} is a {self.gender} and says {self.bark}")
teddy=Bulldog('teddy',7,'blue')
teddy.color('brown')
teddy.bark('bow bow','male')
print()
boomer=JackRussellTerrier('Boomer',3,'red')
boomer.weight()
boomer.life_span(30)