import dnd_dice
import pandas as pd
import numpy as np

class Character():
    """Create a class to store the character info"""
    def __init__(self):
        print('Welcome to the character creator!')
        self.set_race()
        self.set_subrace()

    def set_race(self):
        global races_df 
        races_df = pd.read_excel(r'./data/character/races.xlsx')
        print('What race would you like your charcter to be?')
        
        for counter, race in enumerate(races_df['RACE'].unique(), start=1):
            print(f'\t{counter}. {race}')
        
        while True:
            print("Enter the number next to the race here: ", end ='')
            race_number = input()
            try:
                race_number = int(race_number)
            except ValueError:
                pass
            if isinstance(race_number, int) and race_number >= 1 and race_number <= len(races_df['RACE'].unique()):
                break
            else:
                print('Unrecognized input, please try again.')
        
        race = races_df['RACE'].unique()[race_number - 1]
        
        self.race = race


    def set_subrace(self):
        subraces = races_df.loc[races_df['RACE']==self.race, 'SUBRACE'].unique()
        if len(subraces) == 1 and subraces[0] == self.race:
            self.subrace = subraces[0]
            return
        
        subraces = np.delete(subraces, np.where(subraces == self.race))
        print(f'\nYou have chosen {self.race}!', end = '\n\n')
        print('What subclass will your character be?')
        
        for counter, subrace in enumerate(subraces, start=1):
            print(f'\t{counter}. {subrace}')
        
        while True:
            print("Enter the number next to the subrace here: ", end ='')
            subrace_number = input()
            try:
                subrace_number = int(subrace_number)
            except ValueError:
                pass
            if isinstance(subrace_number, int) and subrace_number >= 1 and subrace_number <= len(races_df['RACE'].unique()):
                break
            else:
                print('Unrecognized input, please try again.')
        
        subrace = subraces[subrace_number - 1]
        
        self.subrace = subrace
        


if __name__ == '__main__':
    robert = Character()
    print(robert.race, robert.subrace)
