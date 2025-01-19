"""
Kalia Dorgelo and Elizabeth Stahlbaum
10/25/2024
Python 3.12 version
This is Project 2: Halfing Chess. This project is a board game that has villains and heroes. The Heros and Villains
both get turns to move or attack or do nothing. The game ends when all Heroes are dead or there are no Villains to
continue fighting. The Heroes goal is to clear as many dungeons as possible.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Union, List
from enum import Enum
from random import randint
from coord import Coord


class CharacterDeath(Exception):
    """
    This class is the CharacterDeath exception that we will raise later in the code
    """

    def __init__(self, msg, char: Character):
        """
        This is the initial function for the Character Death Exception.

        Parameter:
            msg: This is the message that we will input when we raise this exception.
            char: This is the Character that has died.
        """
        self.message = msg
        char.temp_health = 0


class InvalidAttack(Exception):
    """
    This is just an exception that is raised, I beileve, in the unittest code for the teacher.
    """
    pass


class Player(Enum):
    """
    This is the class that helps define if the character is a Villain or Hero. To do this it inherits Enum.
    """
    VILLAIN = 0
    HERO = 1


class Character(ABC):
    """
    This is an abstract class that defines the attributes of a Character.
    """

    def __init__(self, player: Player):
        """
        This is the inital function for the Character class.

        Parameter:
            player: This is the player team of the Character.
        """
        self.__player = player
        self.__health = 5
        self.__temp_health = 5
        self.__attack = 3
        self.__defense = 3
        self.__move = 3
        self.__range = 1

    @property
    def player(self):
        """
        This function is the getter for the player. A property of a Character.

        Returns:
            The player that we had in our parameter.
        """
        return self.__player

    @player.setter
    def player(self, new_player):
        """
        This is the setter for the player and makes the current player hold the value of new_player.

        Parameter:
            new_player: This is the inptuted player that will become our new and improved player.

        Raises:
            TypeError: If the new_player is not a part of the Player class that inherited Enum.
        """
        if not isinstance(new_player, Player):
            raise TypeError
        self.__player = new_player

    @property
    def health(self):
        """
        This is the setter for the health attribute. A property of a Character.

        Returns:
            The current value of health.
        """
        return self.__health

    @health.setter
    def health(self, new_health):
        """
        This is the setter for Character's attribute health and will make the health hold the value of new_health.

        Parameter:
            new_health: This is the new value of health.

        Raises:
            TypeError: If new_health is not an integer.
            ValueError: If new_health is below 0 because then the character would just be dead.
        """
        if not isinstance(new_health, int):
            raise TypeError
        if new_health < 0:
            raise ValueError
        self.__health = new_health

    @property
    def temp_health(self):
        """
        This is the getter for the temp_health attribute. A property of a Character.

        Returns:
            The current value for temp_health.
        """
        return self.__temp_health

    @temp_health.setter
    def temp_health(self, new_temp_health):
        """
        This is the setter for the temp_health. This will assign temp_health to have the value of new_temp_health.

        Parameter:
            new_temp_health: This is the new value for temp_health.

        Raises:
            TypeError: If the new_temp_health is not an integer
            CharacterDeath: If the character's temp_health goes below 0.
        """
        if not isinstance(new_temp_health, int):
            raise TypeError
        if new_temp_health < 0:
            raise CharacterDeath("You died", self)
        self.__temp_health = new_temp_health

    @property
    def combat(self):
        """
        This is the getter for combat. A property of a Character.

        Returns:
            A list of the attack attribute as the first element and the defense attribute as the second element.
        """
        return [self.__attack, self.__defense]

    @combat.setter
    def combat(self, lst):
        """
        This is the setter for combat.

        Parameter:
            lst: This is an inputted list that holds the attack as the first element and defense as the second element.

        Raises:
            TypeError: If the input is not a list.
            ValueError: If attack or defense in the list is less than 0.
        """
        if not isinstance(lst, list):
            raise TypeError
        if lst[0] < 0 and lst[1] < 0:
            raise ValueError
        self.__attack = lst[0]
        self.__defense = lst[1]

    @property
    def range(self):
        """
        This is the getter function for the attribute range. A property of a Character.

        Returns:
            The current value of range.
        """
        return self.__range

    @range.setter
    def range(self, new_range):
        """
        This is the setter function for the attribute range.

        Parameter:
            new_range: This is the new value for range.

        Raises:
            TypeError: If the new_range is not an integer.
            ValueError: If the new_range is less than 0.
        """
        if not isinstance(new_range, int):
            raise TypeError
        if new_range < 0:
            raise ValueError
        self.__range = new_range

    @property
    def move(self):
        """
        This is the getter function for that attribute move. It is how many spaces a Character can move. This is a
        property of a Character.

        Returns:
            The current value of the move attribute.
        """
        return self.__move

    @move.setter
    def move(self, new_move):
        """
        This is the setter for the attribute move.

        Parameter:
            new_move: This is the new value for move.

        Raises:
            TypeError: If the new_move is not an integer.
            ValueError: If the new_move is less than 0.
        """
        if not isinstance(new_move, int):
            raise TypeError
        if new_move < 0:
            raise ValueError
        self.__move = new_move


    @abstractmethod
    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        """
        This function is an abstract method and makes sure that a Character can move to a specific location. It checks
        if the coordinates are in the board, if the from_coord is actually where the character is, and if there is
        someone in the spot where you are going to move to.

        Parameter:
            from_coord: The coordinate where the character is now.
            to_coord: The coordinate where the character wants to move to.
            board: The actual board itself.

        Returns:
            True or False depending on if all the conditions are met.
        """
        # This checks if the from_coord and to_coord are the exact same. If so, it returns False.
        if from_coord.x == to_coord.x and from_coord.y == to_coord.y:
            return False
        # This checks if the from_coord is in the board's boundaries.
        if from_coord.x < len(board) and from_coord.x >= 0 and from_coord.y < len(board[0]) and from_coord.y >= 0:
            # This checks if the to_coord is in the board's boundaries.
            if 0 <= to_coord.x < len(board) and len(board[0]) > to_coord.y >= 0:
                # This checks if from_coord is where the Character (or self) is.
                if board[from_coord.x][from_coord.y] == self:
                    # This checks if the to_coord on the board is empty.
                    if board[to_coord.x][to_coord.y] == None:
                        # If all the conditions are true, it returns true.
                        return True

    @abstractmethod
    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        """
        This function is an abstract method and checks if the character can actually attack at that spot. This checks
        if the coordinates are within the board's parameters, if the from_coord is actually where the character is, and
        if there is someone to actually attack where you want to attack.

        Parameter:
            from_coord: The coordinate where the character is.
            to_coord: The coordinate where the character wants to attack.
            board: The actual board itself.

        Returns:
            True or False depending on if the conditions are met.
        """
        # This checks if the from_coord and to_coord are the exact same. If so, it returns False.
        if from_coord.x == to_coord.x and from_coord.y == to_coord.y:
            return False
        # This checks if the from_coord is in the board's boundaries.
        if from_coord.x < len(board) and from_coord.x >= 0 and from_coord.y < len(board[0]) and from_coord.y >= 0:
            # This checks if the to_coord is in the board's boundaries.
            if 0 <= to_coord.x < len(board) and len(board[0]) > to_coord.y >= 0:
                # This checks if from_coord is where the Character (or self) is.
                if board[from_coord.x][from_coord.y] == self:
                    # This checks if the to_coord on the board is not empty.
                    if board[to_coord.x][to_coord.y] != None:
                        # If all the conditions are true, it returns true.
                        return True
        return False

    @abstractmethod
    def calculate_dice(self, target, attack=True, lst: list = [], *args, **kwargs) -> int:
        """
        This is the function that is an abstract method and that calculates how many rolls of a character that is
        attempting to attack or defend is successful or not.

        Parameter:
            target: This is unused in this function, but it will be used in child classes. This is the character we are
                trying to attack or defend from.
            attack: This is a boolean that determines if the self if attacking or defending. True if attacking. False if
                defending.
            lst: This is the value that hold 1-6 (how many numbers are on a die) in place of randomly generating numbers
            args: This is for child classes to add an argument.
            kwargs: This is for child classes to add an argument.

        Returns:
            How many successful rolls there are whether attacking or defending.
        """
        # The value to keep track of how many attack rolls are successful.
        offense = 0
        # The value to keep track of how many defense rolls are successful.
        protect = 0
        # Checks if the list that replaces the randomly generated numbers are empty.
        if len(lst) == 0:
            # If so, it checks if attack is True. If it is, then we are attacking.
            if attack == True:
                # This for loop itereates through the range of Character's attack plus 1.
                for i in range(self.__attack + 1):
                    # Checks if a randomly generated number is greater than 4.
                    if randint(1, 6) > 4:
                        # If so, one is added to offense because the roll is successful.
                        offense += 1
                return offense
            # If the attack is False, it means that we are defending.
            if not attack:
                # Then it iterates through the range of defense plus 1.
                for i in range(self.__defense + 1):
                    # Checks if the randomly generated value is greater than 3.
                    if randint(1, 6) > 3:
                        # If so, it adds one to the protection because the roll is successful.
                        protect += 1
                return protect
        # If the list has values 1 through 6, it goes through this.
        else:
            # If the attack is True, it means that we are attacking.
            if attack:
                # This itereates through the list of 1-6.
                for i in lst:
                    # This checks if the value in the list is greater than 4.
                    if i > 4:
                        # If so, the roll is successful and will add one to the offense.
                        offense += 1
                return offense
            # If attack is False, it means that we are defending.
            if not attack:
                # This iterates through the list of 1-6.
                for i in lst:
                    # If the element is greater than 3, then the attack is successful.
                    if i > 3:
                        # We add 1 to the protect value.
                        protect += 1
                return protect

    @abstractmethod
    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:  # target's current health - damage
        '''
        :param target: Character
        :param damage: int

        when a target is attacked we calculate how much to take from their temp_health
        This is where CharacterDeath can be raised
        '''
        try:
            target.temp_health = target.temp_health - damage
            print(f'{target} was dealt {damage} damage')
        #if exceeption is raised print message
        except CharacterDeath as e:
            print(e.message)

    def __str__(self) -> str:
        """
        This makes a string of the class name.

        Returns:
            The class name
        """
        return f'{Character.__name__}'
