import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
            if you=='g':
                return False
            elif you=='s':
                return True
