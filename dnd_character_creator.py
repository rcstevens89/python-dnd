import dnd_dice
import pandas as pd
import numpy as np
import os
import time

class Character():
    """Create a class to store the character info"""
    def __init__(self):
        print('Welcome to the character creator!')
        time.sleep(1)
        
        self.set_race()
        time.sleep(1)
        
        self.set_subrace()
        time.sleep(1)

        self.set_race_stats()

    def set_race(self):
        # setting the working dir
        dir, file = os.path.split(__file__)
        os.chdir(dir)
        
        global races_df 
        races_df = pd.read_excel(r'./data/character/races.xlsx')
        print('\nWhat race would you like your charcter to be?')
        
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

    
    def set_race_stats(self):
        """Confirming selection for race and subrace and setting stats based on the race"""
        race_stats = races_df[(races_df['RACE'] == self.race) & (races_df['SUBRACE'] == self.subrace)].reset_index(drop=True)
        if self.race != self.subrace:
            print(f'\nYou have chosen {self.subrace} {self.race} for your character!')
        else:
            print(f'\nYou have chosen {self.race} for your character!')
        
        stat_names = ['Race',           'Subrace',          'Size',             'Speed',        'Strength',     
                      'Dexterity',      'Constitution',     'Intellegence',     'Wisdom',       'Charisma',     
                      'Special',        'Languages',	    'Extra',            'Book'
                      ]
        
        print('\nYour creature\'s stats will be:')
        for title, col in zip(stat_names, race_stats.columns):
            if title == 'Size':
                if race_stats['SIZE'][0] == 'M':
                    print('\tSize: Medium')
                elif race_stats['SIZE'][0] == 'S':
                    print('\tSize: Small')
                elif race_stats['SIZE'][0] == 'L':
                    print('\tSize: Large')
                else:
                    print(f"\tSize: {race_stats['SIZE']}")
            elif title in ['Race', 'Subrace', 'Book']:
                continue
            elif (~race_stats[col].isna().values.any()):
                print(f'\t{title}: {race_stats[col][0]}')

        print("\nWould you like to save these settings for your character? (y/n) ", end ='')
        race_input = input()

        if race_input.lower() == 'y':
            self.size = race_stats['SIZE'][0]
            self.speed = race_stats['SPEED'][0]
            self.strength           
        
        


if __name__ == '__main__':
    # print(__file__)
    robert = Character()
    
