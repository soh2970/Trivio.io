# @author: Harjap

# The boss class
class Boss:

    # private variables to hold the bosses' hp and the current level
    # constructor to make a new boss with starting hp as 100.
    def __init__():
        bossHp = 100
        
    
    # Method to make the boss lose hp.
    # @param level, the boss losses a certain amount of hp depending on the current level
    def loseBossHP(level):
        if (level == 1):
            bossHp -= 4
    
        elif (level == 2):
            bossHp -= 6
        
        elif (level == 3):
            bossHp -= 10
        
        else:
            raise Exception('This level does not exist.')
    
    # Method to check if the boss of the game has been defeated.
    # @return boolean, true if defeated and false if not.
    def isBossDefeated():
        if( bossHp <= 0):
            return True
        
        else:
            return False