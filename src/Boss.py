# @author: Harjap

# The boss class
class Boss:
    """
    Represents the boss enemy in the game, maintaining the boss's health points (HP) and
    handling the reduction of HP based on the level's difficulty when the player answers
    correctly.

    Attributes:
        bossHp (int): The health points of the boss, initialized to 100.

    Methods:
        __init__(self):
            Initializes a new Boss instance with default HP.

        loseBossHP(self, level):
            Reduces the boss's HP based on the current level's difficulty.
            The HP reduction varies: -4 HP for level 1, -6 HP for level 2, and -10 HP for level 3.

        isBossDefeated(self):
            Checks if the boss's HP has dropped to 0 or below, indicating defeat.
            Returns True if the boss is defeated, False otherwise.
    """
    bossHp = 100
    # private variables to hold the bosses' hp and the current level
    # constructor to make a new boss with starting hp as 100.
    def __init__(self):
        self.bossHp = 100
        pass
        
    
    # Method to make the boss lose hp.
    # @param level, the boss losses a certain amount of hp depending on the current level
    def loseBossHP(self, level):
        if (level == 1):
            self.bossHp -= 4
    
        elif (level == 2):
            self.bossHp -= 6
        
        elif (level == 3):
            self.bossHp -= 10
        
        else:
            raise Exception('This level does not exist.')
    
    # Method to check if the boss of the game has been defeated.
    # @return boolean, true if defeated and false if not.
    def isBossDefeated(self):
        if (self.bossHp <= 0):
            return True
        
        else:
            return False