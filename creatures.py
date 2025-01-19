"""
Kalia Dorgelo and Elizabeth Stahlbaum
10/25/2024
Python 3.12 version
This is Project 2: Halfing Chess. This project is a board game that has villains and heroes. The Heros and Villains
both get turns to move or attack or do nothing. The game ends when all Heroes are dead or there are no Villains to
continue fighting. The Heroes goal is to clear as many dungeons as possible.
"""
from character import *


class Villain(Character):
    """
    This is a class that inherits all the Character attributs and changes it according to the specifications of a
    villain. Which includes villains only being allowed to move forward, backwards, left, and right.
    """

    def __init__(self):
        """
        This is the initial function that defines that this is a Villain character. This also defines a board: 8 x 8.
        """
        super().__init__(Player.VILLAIN)
        self.__board = [[None for _ in range(8)]for _ in range(8)]

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]):
        """
        This is a function that checks if the Villain Character can move to a certain spot. There is a case for each
        direction that a villain can go (forward, backwards, left, and right).

        Parameters:
            from_coord: This is the coordinate that the Villain Character is initially at.
            to_coord: This is the coordinate that the Villain Character wants to move to.
            board: This is the list and dimentions of the board.

        Returns:
            True or False based on if the conditions are met.
        """
        # This is checking if the conditions form Character's is_valid_move is met.
        if super().is_valid_move(from_coord, to_coord, board):
            # It checks if we are moving vertically and if the move is valid based on the character's move attribute.
            if from_coord.x == to_coord.x and abs(from_coord.y - to_coord.y) <= self.move:
                # This checks if we are moving down.
                if from_coord.y < to_coord.y:
                    # This makes sure all the spaces in between and including the to_coord are empty.
                    for i in range(from_coord.y + 1, to_coord.y):
                        # This makes sure that the from_coord isn't where the Character is. If it is, we return True.
                        if from_coord.y + 1 == Character:
                            return True
                        # This makes sure the is_valid_move passes in the Character class for every space that we check.
                        elif not super().is_valid_move(from_coord, Coord(to_coord.x, i), board):
                            # If it doesn't pass, it returns False.
                            return False
                    # If everything passes, it returns True.
                    return True
                # This checks if we are moving up.
                elif from_coord.y > to_coord.y:
                    # This makes sure all the spaces in between and including the to_coord are empty.
                    for i in range(from_coord.y - 1, to_coord.y, -1):
                        # This makes sure the from_coordinate + 1 is not the Character.
                        if from_coord.y + 1 == Character:
                            # If it is the Character, we return True.
                            return True
                        # We check the is_valid_move from character for every space in the for loop.
                        elif not super().is_valid_move(from_coord, Coord(to_coord.x, i), board):
                            # If it doesn't pass, we return false.
                            return False
                    # If all of these pass, we return True.
                    return True
            # This checks if we are moving horizontally and if it's in the move range for each villain.
            elif from_coord.y == to_coord.y and abs(from_coord.x - to_coord.x) <= self.move:
                # This checks if we are moving to the left.
                if from_coord.x < to_coord.x:
                    # This makes sure all the spaces in between and including the to_coord are empty.
                    for i in range(from_coord.x + 1, to_coord.x):
                        # This checks if the from_coord's x + 1 is the Character. If so, we return True.
                        if from_coord.x + 1 == Character:
                            return True
                        # We check if the is_valid_move passes in Character for every space in the loop.
                        elif not super().is_valid_move(from_coord, Coord(i, to_coord.y), board):
                            # If not, we return False.
                            return False
                    # If all passes we return True.
                    return True
                # This checks if we are moving to the right.
                elif from_coord.x > to_coord.x:
                    # This makes sure all the spaces in between and including the to_coord are empty.
                    for i in range(from_coord.x - 1, to_coord.x, -1):
                        # This checks if the from_coord's x + 1 is the Character. If so, we return True.
                        if from_coord.x + 1 == Character:
                            return True
                        # If not, we check if is_valid_move passes in Character for every space in the loop.
                        elif not super().is_valid_move(from_coord, Coord(i, to_coord.y), board):
                            # If it didn't pass, we return False.
                            return False
                    # If everything passed, we return True.
                    return True
        # If is_valid_move in Character didn't pass the very first time we called it, we return False.
        return False

    def calculate_dice(self, target, attack=True, lst: list = [], *args, **kwargs) -> int:
        """
        This is the calculate dice function we are taking from the Villain class. There are no additional changes we
        make to it, so we just call super().

        Parameters:
            target: the person we are trying to attack.
            attack: If True, we are attacking. If False, we are defending.
            lst: A list of 1 - 6 to act like a die roll.

        Return:
             We just return whatever the Villain class returned for calculate dice because no mods were needed.
        """
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        """
        This is taking the attribute of Villain of deal_damage. There are no modifications to this, so we are just
        calling super().

        Parameters:
            target: The Character we are trying to attack
            damage: The amount of damage we did.

        Returns:
             We just return whatever the Villain class returned for deal damage because no mods were needed.
        """
        return super().deal_damage(target, damage)

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        """
        This is taking the attribute of Villain of is_valid_attack. There are no modifications to this, so we are just
        calling super().

        Parameters:
            from_coord: The coordinate where the character that you are is.
            to_coord: The coordinate of where the character you want to attack is.
            board: A list that is the parameter of the board and prints out to be the board.

        Returns:
            We just return whatever the Villain class returned for is_valid_attack because no mods were needed.
        """
        return super().is_valid_attack(from_coord, to_coord, board)


class Goblin(Villain):
    """
    This class takes in the attributes of the Villain class and modifies it to make a new type of Villain named Goblin.
    The modifications are the health/temp_health, and the attack/defense.
    """

    def __init__(self):
        """
        This is the initial function where we define that Goblin is a Villain and the health/temp_health are set to 3.
        While the attack and defense are set to 2.
        """
        super().__init__()
        self.health = 3
        self.temp_health = 3
        self.combat = [2, 2]

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]):
        """
        This function takes in what the Villain class has for is_valid_move, so the Goblin can only move horizontally
        and vertically.

        Parameters:
            from_coord: is the coordinate where the Character we are trying to move is from.
            to_coord: is the coordinate where the Character is trying to move to.
            board: is a list that is the parameters of the board, and prints out to be the board.

        Returns:
             We just return whatever the Villain class returned for is_valid_move because no mods were needed.
        """
        return super().is_valid_move(from_coord, to_coord, board)

    def calculate_dice(self, target, attack=True, lst: list = [], *args, **kwargs) -> int:
        """
        This is the calculate dice function we are taking from the Villain class. There are no additional changes we
        make to it, so we just call super().

        Parameters:
            target: the person we are trying to attack.
            attack: If True, we are attacking. If False, we are defending.
            lst: A list of 1 - 6 to act like a die roll.

        Return:
             We just return whatever the Villain class returned for calculate dice because no mods were needed.
        """
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        """
        This is taking the attribute of Villain of deal_damage. There are no modifications to this, so we are just
        calling super().

        Parameters:
            target: The Character we are trying to attack
            damage: The amount of damage we did.

        Returns:
             We just return whatever the Villain class returned for deal damage because no mods were needed.
        """
        return super().deal_damage(target, damage)

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        """
        This is taking the attribute of Villain of is_valid_attack. There are no modifications to this, so we are just
        calling super().

        Parameters:
            from_coord: The coordinate where the character that you are is.
            to_coord: The coordinate of where the character you want to attack is.
            board: A list that is the parameter of the board and prints out to be the board.

        Returns:
            We just return whatever the Villain class returned for is_valid_attack because no mods were needed.
        """
        return super().is_valid_attack(from_coord, to_coord, board)


class Skeleton(Villain):
    """
    This is a class that takes in the attributes of Villain and modifies them to make a new Villain named Skeleton.
    The modifications are to health/temp_health, move, and, attack/defense.
    """

    def __init__(self):
        """
        This is the initial function in the class for Skeleton. Take in all the attributes of the Villain function,
        while changing health/temp_health and move to 2, and attack to 2 and defense to 1.
        """
        super().__init__()
        self.health = 2
        self.temp_health = 2
        self.combat = [2, 1]
        self.move = 2

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]):
        """
        This function takes in what the Villain class has for is_valid_move, so the Skeleton can only move horizontally
        and vertically.

        Parameters:
            from_coord: is the coordinate where the Character we are trying to move is from.
            to_coord: is the coordinate where the Character is trying to move to.
            board: is a list that is the parameters of the board, and prints out to be the board.

        Returns:
             We just return whatever the Villain class returned for is_valid_move because no mods were needed.
        """
        return super().is_valid_move(from_coord, to_coord, board)

    def calculate_dice(self, target, attack=True, lst: list = [], *args, **kwargs) -> int:
        """
        This is the calculate dice function we are taking from the Villain class. There are no additional changes we
        make to it, so we just call super().

        Parameters:
            target: the person we are trying to attack.
            attack: If True, we are attacking. If False, we are defending.
            lst: A list of 1 - 6 to act like a die roll.

        Return:
             We just return whatever the Villain class returned for calculate dice because no mods were needed.
        """
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        """
        This is taking the attribute of Villain of deal_damage. There are no modifications to this, so we are just
        calling super().

        Parameters:
            target: The Character we are trying to attack
            damage: The amount of damage we did.

        Returns:
             We just return whatever the Villain class returned for deal damage because no mods were needed.
        """
        return super().deal_damage(target, damage)

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        """
        This is taking the attribute of Villain of is_valid_attack. There are no modifications to this, so we are just
        calling super().

        Parameters:
            from_coord: The coordinate where the character that you are is.
            to_coord: The coordinate of where the character you want to attack is.
            board: A list that is the parameter of the board and prints out to be the board.

        Returns:
            We just return whatever the Villain class returned for is_valid_attack because no mods were needed.
        """
        return super().is_valid_attack(from_coord, to_coord, board)


class Necromancer(Villain):
    """
    This class takes on the attributes of Villain and makes modifications to them to make a new Villain named
    Necromancer. These modifications include to attack/defense, range, and adding a new attribute called raise dead.
    """

    def __init__(self):
        """
         This is the initial function to the Necromancer class which takes in all the inital function attributes of
         Villain and changes attack to 1, defense to 2, and range to 3.
        """
        super().__init__()
        self.combat = [1, 2]
        self.range = 3

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]):
        """
        This function takes in what the Villain class has for is_valid_move, so the Skeleton can only move horizontally
        and vertically.

        Parameters:
            from_coord: is the coordinate where the Character we are trying to move is from.
            to_coord: is the coordinate where the Character is trying to move to.
            board: is a list that is the parameters of the board, and prints out to be the board.

        Returns:
             We just return whatever the Villain class returned for is_valid_move because no mods were needed.
        """
        return super().is_valid_move(from_coord, to_coord, board)

    def calculate_dice(self, target, attack=True, lst: list = [], *args, **kwargs) -> int:
        """
        This is the calculate dice function we are taking from the Villain class. There are no additional changes we
        make to it, so we just call super().

        Parameters:
            target: the person we are trying to attack.
            attack: If True, we are attacking. If False, we are defending.
            lst: A list of 1 - 6 to act like a die roll.

        Return:
             We just return whatever the Villain class returned for calculate dice because no mods were needed.
        """
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        """
        This is taking the attribute of Villain of deal_damage. There are no modifications to this, so we are just
        calling super().

        Parameters:
            target: The Character we are trying to attack
            damage: The amount of damage we did.

        Returns:
             We just return whatever the Villain class returned for deal damage because no mods were needed.
        """
        return super().deal_damage(target, damage)

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        """
        This is taking the attribute of Villain of is_valid_attack. There are no modifications to this, so we are just
        calling super().

        Parameters:
            from_coord: The coordinate where the character that you are is.
            to_coord: The coordinate of where the character you want to attack is.
            board: A list that is the parameter of the board and prints out to be the board.

        Returns:
            We just return whatever the Villain class returned for is_valid_attack because no mods were needed.
        """
        return super().is_valid_attack(from_coord, to_coord, board)

    def raise_dead(self, target: Character, from_coord, to_coord, board: List[List[Union[None, Character]]]):
        """
        This function addes the attribute raise_dead to Necromancer. This allows the Necromancer to take a dead
        person near them, doesn't matter if it's a Villain or Hero, and makes it come back to life with half it's health
        and changes it to a Villain if it is not already.

        Parameter:
            target: This is the Character we are trying to bring back to life.
            from_coord: This is the coordinate where we are.
            to_coord: This is the coordinate to where the target is.
            board: This is a list that is the parameters of the board, and prints out like a board.

        Returns:
            The newly raised-from-the-dead target.
        """
        # This checks if the target is within the range of the Necromancer.
        if abs(from_coord.x - to_coord.x) <= self.range and abs(from_coord.y - to_coord.y) <= self.range:
            # This checks if the target is already a Villain.
            if target == Player.VILLAIN:
                # This makes sure that the target's temp_health is at or below 0.
                if target.temp_health <= 0:
                    # If meets all the above conditions, it makes target's temp_health become half full.
                    target.temp_health = target.health // 2
            # This checks if the target is a Hero.
            elif target != Player.VILLAIN:
                # We change the player from the Hero to the Villain
                target.player = Player.VILLAIN
                # This makes sure the target's temp_health is at or below 0.
                if target.temp_health <= 0:
                    # If all the conditions are met, then we make target's temp_health half full.
                    target.temp_health = target.health // 2
        # We return the target.
        return target

class Hero(Character):
    '''
    takes in all attibutes and functions of Character with no moldifications
    '''
    def __init__(self):
        # same as parent
        super().__init__(Player.HERO)

    # call abstract methods
    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]):
        #same as Parent
        return super().is_valid_move(from_coord, to_coord, board)

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]):
        # same as Parent
        return super().is_valid_attack(from_coord, to_coord, board)

    def calculate_dice(self, target = None, attack=True, lst=[], *args, **kwargs):
        # same as Parent
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:  # target's current health - damage
        # same as Parent
        return super().deal_damage(target, damage)


class Warrior(Hero):
    # call super()
    def __init__(self):
        '''same as parent except for the following modifications'''
        super().__init__()
        self.health = 7
        self.temp_health = 7
        self.combat = [2, 4]

    def calculate_dice(self, target=None, attack=True, lst: list = [], gob: list = [], *args, **kwargs):
        '''#everything is the same as parent except if target is a goblin'''
        # gob is a list hold two values 1-6 for testing purpose
        if len(lst) > 0:
            if isinstance(target, Goblin):
                tot = 0
                #if gob is empty roll two more die and determine if it did damage
                if len(gob) == 0:
                    gob[0].append(randint(1, 6))
                    gob[0].append(randint(1, 6))
                    for i in gob:
                        if gob[i] > 4:
                            tot += 2
                if attack:
                    #calculate_dice like normal but add those extra gob points
                    return super().calculate_dice(target, attack, lst) + tot
                else:
                    return super().calculate_dice(target, attack, lst)

            else:
                return super().calculate_dice(target, attack, lst)
        else:
            return super().calculate_dice(target, attack, lst)

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        # same as parent
        return super().is_valid_attack(from_coord, to_coord, board)

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        # same as parent
        return super().is_valid_attack(from_coord, to_coord, board)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        # same as parent
        return super().deal_damage(target, damage, *args, **kwargs)


class Mage(Hero):
    def __init__(self):
        '''same as parent but with the following modifications'''
        super().__init__()
        self.combat = [2, 2]
        self.move = 2
        self.range = 3

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        # same as parent
        return super().is_valid_attack(from_coord, to_coord, board)

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        # same as parent
        return super().is_valid_attack(from_coord, to_coord, board)

    def calculate_dice(self, target=None, attack=True, lst=[], *args, **kwargs):
        # same as parent
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        ''' All Mage attacks automatically deal an additional 1 damage to target'''
        target.temp_health = target.temp_health - (damage + 1)
        #still have to raise exception if damage kills Character
        if CharacterDeath:
            print(CharacterDeath)
        print(f'{target} was dealt {damage} damage')


class Paladin(Hero):
    '''
    add attribute __heal and property and setter heal
    variables that change: health and temp_health
    functions that change: revive
    '''
    def __init__(self):
        '''same as parent + following modifications'''
        super().__init__()
        self.__heal = True
        self.health = 6
        self.temp_health = 6

    '''new property(readable and writable) that allows Paladin to raise another Hero from the dead'''

    @property
    def heal(self) -> bool:
            return self.__heal

    @heal.setter
    def heal(self, new_heal):
        if not isinstance(new_heal, bool):
            raise TypeError
        else:
            self.__heal = new_heal

    def revive(self, target: Character, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]):
        '''
        :param target: Character we are healing
        :param from_coord: Coord
        :param to_coord: Coord of target
        :param board: List[List[Union[None, Character]]]
        :return: None

        if heal is used once you can not use it again
        heal resets the target's temp_health to half of the value of health rounded down if they are in range
        '''
        if self.heal == True:
            if abs(from_coord.x - to_coord.x) <= self.range and abs(from_coord.y - to_coord.y) <= self.range:
                target.temp_health = target.health // 2
                self.heal = False


    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]):
        # same as parent
        return super().is_valid_move(from_coord, to_coord, board)

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]):
        # same as parent
        return super().is_valid_attack(from_coord, to_coord, board)

    def calculate_dice(self, target = None, attack=True, lst=[], *args, **kwargs):
        # same as parent
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:  # target's current health - damage
        #same as parent
        return super().deal_damage(target, damage)


class Ranger(Hero):
    '''
    variables that change: range
    functions that change: deal_damge
    '''
    def __init__(self):
        '''same as parent + following changes'''
        super().__init__()
        self.range = 3

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]):
        # same as parent
        return super().is_valid_move(from_coord, to_coord, board)

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]):
        # same as parent
        return super().is_valid_attack(from_coord, to_coord, board)

    def calculate_dice(self, target = None, attack=True, lst=[], *args, **kwargs):
        # same as parent
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:  # target's current health - damage
        '''
        :param target: Character that we have attacked
        :param damage: int
        :param args: empty for now
        :param kwargs: empty for now
        :return: None

        Ranger deals 1 less damage to any Skeleton
        If damage goes below 0, set temp_health to 0
        '''
        #Ranger deals 1 less damage then it does to everyone else
        #if damage becomes less then 0, auto death to the target
        if isinstance(target, Skeleton):
            if damage < 1:
                target.temp_health = 0
            else:
                target.temp_health = target.temp_health - (damage - 1)
            print(f'{target} was dealt {damage-1} damage')
        else:
            # if damage becomes less than 0, auto death to the target
            if damage < 0:
                target.temp_health = 0
            else:
                #deal regular damage
                target.temp_health = target.temp_health - damage
            print(f'{target} was dealt {damage} damage')
        # if damage becomes less than 0, auto death to the target
        if damage < 0:
            self.temp_health = 0
        if CharacterDeath:
            print(CharacterDeath)
