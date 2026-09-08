import time

class Barista():
  def __init__(self, name):
    self.name = name

  def make_coffee():
    print(f"{self.name} is making coffee")

  def run():
    while True:
      self.make_coffee()
      time.sleep(.5)

barista1 = Barista("John")
barista2 = Barista("Alice")

barista1.run()
barista2.run()
