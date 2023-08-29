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

if __name__ == '__main__':
    import numpy as np
    rolls = []
    single_attack = []
    ac = 15
    
    for i in range(100000):
        for i in range(4):
            attack_roll = Roll('1d20', 7)
            if attack_roll.base_total == 20:
                damage_1_roll = Roll('1d12')
                damage_2_roll = Roll('1d6')
                damage = damage_1_roll.total + damage_2_roll.total
            elif attack_roll.total >= ac:
                damage_1_roll = Roll('1d12')
                damage_2_roll = Roll('1d6')
                damage = damage_1_roll.total + damage_2_roll.total
            else:
                damage = 0
            single_attack.append(damage)
        single_attack_np = np.array(single_attack)
        rolls.append(single_attack_np.sum())
        single_attack = []

        

    rolls = np.array(rolls)
    print(rolls.max())
    print(rolls.min())
    print(rolls.mean())
    print(rolls.std())
    print(rolls.mean() + rolls.std())
    print(rolls.mean() - rolls.std())