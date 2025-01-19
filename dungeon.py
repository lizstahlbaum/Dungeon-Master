"""
Kalia Dorgelo and Elizabeth Stahlbaum
10/25/2024
Python 3.12 version
This is Project 2: Halfing Chess. This project is a board game that has villains and heroes. The Heros and Villains
both get turns to move or attack or do nothing. The game ends when all Heroes are dead or there are no Villains to
continue fighting. The Heroes goal is to clear as many dungeons as possible.
"""
import random
from typing import Type

from coord import *
from character import *
from creatures import *
import math


class Dungeon():
    """
    This class makes all the characters come together and make it an actual game. This places all the characters on
    the board, makes sure that if we move from board to board, the board the Villains are all empty. Also, it determines
    if the Villains or the Heroes have won.
    """

    def __init__(self, height: int, width: int, villains: List[Villain]=[]):
        """
        This is the initial function of the Dungeon class that defines the attributes of the Dungeon class.

        Parameters:
            height: The height of the board
            width: The width of the board
            villains: A list of all the villains on the board.

        Raises:
            TypeError: If height or width is not an integer
            ValueError: If the height or width is not between 4 and 12.
        """
        if not isinstance(height, int):
            raise TypeError
        if height < 4 or height > 12:
            raise ValueError
        if not isinstance(width, int):
            raise TypeError
        if width < 4 or width > 12:
            raise ValueError
        self.__height = height
        self.__width = width
        self.__board = [[None for _ in range(self.__height)]for _ in range(self.__width)]
        self.__player = Player.HERO
        self.__heroes = [Warrior(), Mage(), Paladin(), Ranger()]
        # Checks if the list of villains is empty. If so, it calls generate villains.
        if len(villains) < 1:
            self.generate_villains()
        else:
            # If the list of villains has something in it then we just assign self.villains to villains.
            self.villains = villains

    @property
    def height(self):
        """
        This is a property of Dungeon and the getter of height.

        Returns:
            The value of height.
        """
        return self.__height

    @property
    def width(self):
        """
        This is a property of Dungeon and the getter of width.

        Returns:
            The value of width.
        """
        return self.__width

    @property
    def board(self):
        """
        This is a property of Dungeon and the getter of board.

        Raises:
            TypeError: if self.__board is not a list.

        Returns:
            The value of board.
        """
        if not isinstance(self.__board, list):
            raise TypeError
        return self.__board

    @board.setter
    def board(self, new_board):
        """
        This is the setter for board.

        Parameter:
            new_board: This is the dimentions of the new board that is going to become board.

        Raises:
            TypeError: If new_board is not a list.
        """
        if not isinstance(new_board, list):
            raise TypeError
        # Assigns the value of new_board to the board.
        self.__board = new_board

    @property
    def player(self):
        """
        This is a property of Dungeon and is the getter for player.

        Returns:
            The value of self.__player.
        """
        return self.__player

    @property
    def heroes(self):
        """
        This is a property of Dungeon and is the getter for heroes.

        Raises:
            TypeError: If self.__heroes is not a list

        Returns:
            The value of self.__heroes
        """
        if not isinstance(self.__heroes, list):
            raise TypeError
        return self.__heroes

    @heroes.setter
    def heroes(self, new_heroes):
        """
        This is the setter for heroes that takes in a new_heroes and assigns it to heroes.

        Parameters:
            new_heroes: This is the new_heroes that will become self.__heroes.

        Raises:
            TypeError: If new_heroes is not a list.
        """
        if not isinstance(new_heroes, list):
            raise TypeError
        # Assigns the value of new_heroes the heroes.
        self.__heroes = new_heroes

    @property
    def villains(self):
        """
        This is a property of Dungeon and the getter for villains.

        Raises:
            TypeError if self.__villains is not a list and if the values in villains are not Villains.

        Returns:
            The value of self.__villains.
        """
        if not isinstance(self.__villains, list):
            raise TypeError
        # Goes through the list of villains.
        for i in range(len(self.__villains)):
            # If the element is not a villain, then raises a TypeError.
            if not isinstance(self.__villains[i], Villain):
                raise TypeError
        return self.__villains

    @villains.setter
    def villains(self, new_vill):
        """
        This is the setter for the property Villains.

        Parameter:
            new_vill: This is the new list of villains that will become villains.

        Raises:
            TypeError: If new_vill is not a list or if new_vill's elements are not Villains
        """
        if not isinstance(new_vill, list):
            raise TypeError
        # Goes through the list of new_vill.
        for i in range(len(new_vill)):
            # Checks if the element is a Villain. If it not, then we raise a TypeError.
            if not isinstance(new_vill[i], Villain):
                raise TypeError
        # Assigns new_vill the new list of villains.
        self.__villains = new_vill

    def generate_villains(self):
        """
        This is a function for the villains property to genreate a list of villains if the villains list is empty.

        Returns:
            Nothing, at the end it makes the villains property equal to the newly generated list of villains.
        """
        # This checks if height is greater than width.
        if self.__height >= self.__width:
            # This generates a random number between 1 and the height to know the number of villains there will be.
            num_vill = random.randint(1, self.__height)
        else:
            # If width is greater than height, we generate a random number between 1 and width.
            num_vill = random.randint(1, self.__width)
        # This makes a new list that the villains are going to be in.
        new_villains = []
        # This goes through the number of villains there will be in the list.
        for i in range(num_vill):
            # This generates a random number between 1 and 10 for each time the for loop runs.
            rand = random.randint(1, 10)
            # If the number is between 1 and 5 it will add a goblin to the list.
            if rand <= 5:
                new_villains.append(Goblin())
            # If the number is between 6 and 8, it will add Skeleton to the list.
            elif rand <= 8:
                new_villains.append(Skeleton())
            # Checking if the number is 9 or 10.
            elif rand <= 10:
                # Sets x to False to see if there is a Necromancer in the list.
                x = False
                # Goes through the newly formed list of villains.
                for i in new_villains:
                    # If there is a necromancer in the list, we change x to True.
                    if isinstance(i, Necromancer):
                        x = True
                # We check if x is True, if so, we add a skeleton to the list.
                if x == True:
                    new_villains.append(Skeleton())
                # If not, we add a necromancer to the list.
                elif x == False:
                    new_villains.append(Necromancer())
        # We make the value newly formed list of villains assigned to the private villains.
        self.__villains = new_villains

    def is_valid_move(self, coords: List[Coord]) -> bool:
        """
        This is a function to check if each villain's move is valid.

        Parameter:
            coords: This is a list of coordinates. The first one being the from_coord and the second one as the to_coord

        Returns:
            True or False depending on if all conditions are met.
        """
        # This checks if from_coord has something in it. (The self).
        print(coords[0].x, coords[0].y)
        if self.board[coords[0].x][coords[0].y] != None:
            print("not none")
            # Makes the from_character the from_coord.
            from_char = self.board[coords[0].x][coords[0].y]
            # Makes the character at the from_coord character(for reasons below)
            character = self.character_at(coords[0].x, coords[0].y)
        # Checks if the length of coords is greater than two, which makes it a hero moving.
        if len(coords) > 2:
            # To check if every coordinate has is in range.
            move_char = character.move
            # Goes throught the range of 1 and the length of coords.
            for i in range(1, len(coords)):
                # Checks if this is a valid move.
                if from_char.is_valid_move(coords[0], coords[i], self.__board):
                    # Checks if the move is in the range for the character.
                    if abs(coords[i].x - coords[i - 1].x) <= character.move and abs(coords[i].y - coords[i - 1].y) <= character.move:
                        # This checks if the x coords are the same.
                        if (coords[i].x - coords[i - 1].x) == 0:
                            # This subtracts it from the moves that the character can take.
                            move_char -= abs(coords[i].y - coords[i - 1].y)
                        # This checks if the y's are the same.
                        if (coords[i].y - coords[i - 1].y) == 0:
                            # Subtracts the x coord's difference from the amount of moves that the character can do.
                            move_char -= abs(coords[i].x - coords[i - 1].x)
                        # if both are different then we are going diagonal
                        elif coords[i].x != coords[i - 1].x and coords[i].y != coords[i - 1].y:
                            # We check if the x's are in range.
                            if abs(coords[i].x - coords[i - 1].x) <= character.move:
                                # We subtract the absolute value from the move_char
                                move_char -= abs(coords[i].x - coords[i - 1].x)
                        else:
                            # If none of the conditions are met, return False
                            return False
            # Checks if move_char is less than 0. If so, returns False. Otherwise, returns True.
            if move_char < 0:
                return False
            else:
                return True
        # If the length of coords is exactly 2, it means it's a hero or a villain.
        if len(coords) == 2:
            # This returns if it is a valid move for the character.
            if from_char.is_valid_move(coords[0], coords[1], self.__board):
                if abs(coords[1].x - coords[0].x) <= character.range and abs(coords[1].y - coords[0].y) <= character.range:
                    return True
            return False


        def is_valid_attack(self, coords: List[Coord]) -> bool:
        """
        This is a function that checks if any character has a valid attack.

        Parameter:
            coords: This is a list of coordinates. The first one being the from_coord and the second being the to_coord.

        Returns:
            True or False depending on if the conditions are met.
        """
        # If there are more than 2 coordinates in here then we raise the ValueError.
        if len(coords) > 2:
            raise ValueError
        # Checks if the from_coord has something there.
        if self.board[coords[0].x][coords[0].y] is not None:
            # Makes the from_chararacter the first element in the list.
            from_char = self.board[coords[0].x][coords[0].y]
            # Assigns the character, the character at the from_coordinates.
            character = self.character_at(coords[0].x, coords[0].y)
        else:
            return False
        # Checks if the length of coords is exactly 2, it could be either a hero or a villain.
        if len(coords) == 2:
            # Checks if the is_valid_attak works for the character and returns that answer.
            if from_char.is_valid_attack(coords[0], coords[1], self.__board):
                if abs(coords[1].x - coords[0].x) <= character.range and abs(coords[1].y - coords[0].y) <= character.range:
                    return True
            return False

    def character_at(self, x: int, y: int) -> Type[Character]:
        """
        This is a function to check what is at a certain space on the board.

        Parameter:
            x: the integer of the x coordinate
            y: the interger of the y coordinate

        Raises:
            TypeError: If x or y are not intergers
            ValueError: If x or y is below 0.

        Returns:
            Whatever is at that spot on the board.
        """
        if not isinstance(x, int):
            raise TypeError
        if not isinstance(y, int):
            raise TypeError
        if x < 0:
            raise ValueError
        if y < 0:
            raise ValueError
        return self.board[x][y]

    def set_character_at(self, target: Character, x: int, y: int):
        """
        This is to put a character at a certain place on the board.

        Parameters:
            target: The character that we are placing down.
            x: The integer of the x coordinate
            y: the interger of the y coordinate

        Returns:
            The target on the board.
        """
        # Makes the target equal the board's coordinates of x an y.
        self.board[x][y] = target
        return target

    def move(self, from_coord: Coord, to_coord: Coord):
        """
        This is a function that moves the character at the from_coord to the to_coord.

        Parameters:
            from_coord: This is where the character is on the board that we want to move.
            to_coord: This is where the character you want to move will go.

        Raises:
            ValueError: if it is not a valid move

        Returns:
            None because we are just moving a character from one place to another.
        """
        if not self.is_valid_move([from_coord, to_coord]):
            raise ValueError
        # Checking if the from_cood has something there.
        if self.character_at(from_coord.x, from_coord.y) is not None:
            # Makes the to_coord have the from_character there.
            self.board[to_coord.x][to_coord.y] = self.board[from_coord.x][from_coord.y]
            # Makes the original from_coord have nothing in it.
            self.board[from_coord.x][from_coord.y] = None

        def attack(self, from_coords: Coord, to_coords: Coord):
        '''
        :param from_coords: Coord
        :param to_coords: Coord
        :return: None

        check for valid_attack
        calculate deal_damage
            If the amount of damage is less than or equal to 0 print out a string in the following format
            -> "{DEFENDER} to no damage from {ATTACKER}"
        '''
        #assign defender to whoever is at to_coords
        defender = self.character_at(to_coords.x, to_coords.y)
        #assign attacker to whoever is at from_coords
        attacker = self.character_at(from_coords.x, from_coords.y)

        #step 1: ensure its a valid attack
        if self.is_valid_attack([from_coords, to_coords]):
            #step 2: sensure there are actual characters in each spot then calculate damage
            if defender != None and attacker != None:
                damage = attacker.calculate_dice(defender, attack=True) - defender.calculate_dice(attacker,attack=False)
                #deal damage
                attacker.deal_damage(defender, damage)
                #print message if no damage is done
                if damage <= 0:
                    print(f'{defender} took no damage from {attacker}')

    def set_next_player(self):
        """
        This makes sure that each turn is flipped from villain to hero or vise versa.

        Returns:
            None, we are only changing turns.
        """
        # Checks if the current player is a Villain.
        if self.__player == Player.VILLAIN:
            # Makes it Hero's turn
            self.__player = Player.HERO
        else:
            # Makes it a Villain's turn if a hero's turn was last.
            self.__player = Player.VILLAIN

    def print_board(self):
        """
        This function was given to us. This is how we print the board.

        Returns:
            None, but prints the board.
        """
        st = ' \t'
        st += '_____' * len(self.board)
        st += '\n'
        for i in range(len(self.__board)):
            st += f'{i}\t'
            for j in range(len(self.__board[i])):
                if self.board[i][j] is None:
                    st += '|___|'
                else:
                    st += f'|{self.board[i][j].__class__.__name__[:3]}|'
            st += '\n'
        st += '\t'
        for i in range(len(self.board[0])):
            st += f'  {i}  '
        print(st)

        def is_dungeon_clear(self) -> bool:
        '''
        :return: bool

        Returns True if all villains have a temp_health less than or equal to 0. Otherwise it returns False.
        '''
        #assume true if at least 1 hero is alive...
        val = True
        for j in self.heroes:
            if j.temp_health > 0:
                val = True
            else:
                val = False
        #... and at least 1 villian is still alive
        for i in self.villains:
            if i.temp_health > 0:
                val = False

        return val

    def adventurer_defeat(self) -> bool:
        '''
        :return: bool

        Returns True if all heroes have a temp_health less than or equal to 0. Otherwise it returns False.
        '''
        #assume true till at least 1 villian is dead...
        val = True
        for j in self.villains:
            if j.temp_health > 0:
                val = True
            else:
                val = False
        #... or at least 1 hero is still alive
        for i in self.heroes:
            if i.temp_health > 0:
                val = False

        return val

    def place_heroes(self):
        '''
        :return: None

        place Warrior left of the middle on the second to last row
        place Paladin to the right of Warrior
        place Mage below Warrior
        place Ranger to the right of Mage
        '''
        # ensure all heroes exist on board
        if len(self.heroes) < 4:
            raise ValueError
        for i in self.__heroes:
            if not isinstance(i, Hero):
                raise TypeError
            if isinstance(i, Warrior):
                self.set_character_at(self.heroes[0],  len(self.board)-2, math.ceil(len(self.board) / 2) - 1, )
            if isinstance(i, Paladin):
                self.set_character_at(self.heroes[2],  len(self.board)-2, math.ceil(len(self.board) / 2))
            if isinstance(i, Mage):
                self.set_character_at(self.heroes[1], len(self.board)-1, math.ceil(len(self.board) / 2) - 1)
            if isinstance(i, Ranger):
                self.set_character_at(self.heroes[3],  len(self.board)-1, math.ceil(len(self.board) / 2))

    def place_villains(self):
        '''
        place villians at a random x(not the first two rows) and a random y
        '''

        for i in self.__villains:
            ran_x = randint(2, len(self.board)-1)
            ran_y = randint(0, len(self.board)-3)
            self.set_character_at(i, ran_x, ran_y)



        def generate_new_board(self, height: int= -1, width: int=-1):
        '''
        :param height: int
        :param width: int
        :return: None

        if no height and/or width are given generate new random ones between 4 and 12
        generate new villians and place them and heroes
        '''
        
        #if no height given make a random one
        if height < 1:
            height = randint(1,10)
        # if no width given make a random one
        if width < 1:
            width = randint(1,10)
        #create new board
        self.__board = [[None for _ in range(height)]for _ in range(width)]
        #empty out og villian list
        self.__villains = []
        #generate new villians
        self.generate_villains()
        #place new villians
        self.place_villains()
        #replace og heroes
        self.place_heroes()

if __name__ == "__main__":
    pass
