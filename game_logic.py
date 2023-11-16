import pygame
import math
def is_collision(x_1: int, y_1: int, x_2: int, y_2: int, desired_distance: int) -> bool:
    """
    Determines whether two objects are within a specified distance of each other,
    indicating a collision.

    Args:
        x_1 (int): The x-coordinate of object 1.
        y_1 (int): The y-coordinate of object 1.
        x_2 (int): The x-coordinate of object 2.
        y_2 (int): The y-coordinate of object 2.
        desired_distance (int): The threshold distance to consider as a collision.

    Returns:
        bool: Returns True if the distance between the two objects is less than
              the desired distance, indicating a collision. Otherwise, returns False.
    """
    distance = math.sqrt(math.pow(x_1-x_2, 2) + math.pow(y_1-y_2, 2))
    if distance < desired_distance:
        return True
    return False

def is_collision(x_1: int, y_1: int, x_2: int, y_2: int, desired_distance: int) -> bool:
    distance = math.sqrt(math.pow(x_1-x_2, 2) + math.pow(y_1-y_2, 2))
    return distance <= desired_distance  # Use <= for 'less than or equal to'

def player(screen: pygame.Surface, image: pygame.Surface, player_x_size: int, player_y_size: int) -> None:
    """
    Renders the player character on the screen at the specified position.

    Args:
        image (pygame.Surface): The image representing the player character.
        player_x_size (int): The x-coordinate where the player image will be placed.
        player_y_size (int): The y-coordinate where the player image will be placed.

    Note:
        This function assumes that 'screen' is a globally accessible pygame display
        surface where the image will be drawn.
    """
    screen.blit(image, (player_x_size, player_y_size))


def alien(screen: pygame.Surface, image: pygame.Surface, alien_x_size: int, alien_y_size: int) -> None:
    screen.blit(image, (alien_x_size, alien_y_size))


def bullet(image: pygame.Surface, bullet_x_size: int, bullet_y_size: int) -> None:
    """
    Renders a bullet character on the screen at the specified position.

    Args:
        image (pygame.Surface): The image representing the bullet character.
        bullet_x_size (int): The x-coordinate for placing the bullet image.
        bullet_y_size (int): The y-coordinate for placing the bullet image.

    Note:
        This function positions the bullet image slightly offset from the given coordinates
        for a more visually appealing placement.
    """
    screen.blit(image, (bullet_x_size + 16, bullet_y_size + 10))


def bomb(image: pygame.Surface, bomb_x_size: int, bomb_y_size: int) -> None:
    """
    Displays a bomb animation on the screen, typically used when a bullet collides with an alien.

    Args:
        image (pygame.Surface): The image representing the bomb animation.
        bomb_x_size (int): The x-coordinate for placing the bomb animation.
        bomb_y_size (int): The y-coordinate for placing the bomb animation.
    """
    screen.blit(image, (bomb_x_size, bomb_y_size))