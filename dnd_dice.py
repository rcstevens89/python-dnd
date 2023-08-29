from random import randint

class Roll:
    def __init__(self, dice_notation, modifier:int = 0):
        self.dice_notation = dice_notation
        self.modifier = modifier
        rolls, faces = dice_notation.split('d')
        self.rolls = int(rolls)
        self.faces = int(faces)
        self.dice = [randint(1, self.faces) for i in range(self.rolls)]
        self.base_total = sum(self.dice) 
        self.total = self.base_total + self.modifier
        
    def __str__(self):
        roll_str = f'Rolling {self.rolls}d{self.faces}!\n'
        for num, die in enumerate(self.dice):
            if (num + 1) % 20 == 0:
                roll_str = roll_str + f'{die},\n'
            else:
                roll_str = roll_str + f"{die},{' ' * ((len(str(self.faces)) + 1) - len(str(die)))}"
        roll_str = roll_str + '\n'    
        roll_str = roll_str + f'You rolled a {self.base_total}\n'
        if self.modifier != 0:
            roll_str = roll_str + f"With a modfier of {'+' if self.modifier > 0 else ''}{self.modifier} "
            roll_str = roll_str + f"your total is {self.total}"
        return roll_str
    
    def with_disadv(self):
        self.dice.sort()
        self.base_total = self.dice[0]
        self.total = self.base_total + self.modifier
        return self
    
    def with_adv(self):
        self.dice.sort()
        self.base_total = self.dice[-1]
        self.total = self.base_total + self.modifier
        return self
