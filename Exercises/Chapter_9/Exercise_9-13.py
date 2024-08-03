import random

class Dice:
    def __init__(self, sides: int) -> None:
        self.sides = sides
    
    def roll_dice(self) -> None:
        print(random.randint(1, self.sides))


six_sided_dice = Dice(6)
for i in range(0, 10):
    six_sided_dice.roll_dice()

ten_sided_dice = Dice(10)
for i in range(0, 10):
    ten_sided_dice.roll_dice()

twenty_sided_dice = Dice(20)
for i in range(0, 10):
    twenty_sided_dice.roll_dice()