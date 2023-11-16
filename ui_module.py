import pygame

def start_button(screen_var: pygame.display, position: tuple, text: str, color: tuple, size: int):
    """
    Creates and renders a button with text on the given screen. This button is designed 
    with an outlined border and a solid background.

    Args:
        screen_var (pygame.display): The screen object where the button will be displayed.
        position (tuple): The (x, y) coordinates for the top-left corner of the button.
        text (str): The text to be displayed on the button.
        color (tuple): The RGB color value for the button text, given as (R, G, B).
        size (int): The font size of the button text.

    Returns:
        pygame.Rect: A rectangle object representing the area of the screen updated by the button.
    """
    font = pygame.font.Font('freesansbold.ttf', size)
    text_render = font.render(text, True, color)
    _, _, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen_var, (200, 200, 200), (x, y), (x + w, y), 5)
    pygame.draw.line(screen_var, (200, 200, 200), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen_var, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen_var, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen_var, (100, 100, 100), (x, y, w, h))
    return screen_var.blit(text_render, (x, y))

def button(screen_var: pygame.display, position: tuple, text: str, color: tuple):
    """
    Creates and displays a simple button with text on the specified screen. This function
    is similar to 'start_button' but uses a predefined font for the button text.

    Args:
        screen_var (pygame.display): The screen object where the button will be displayed.
        position (tuple): The (x, y) coordinates for the top-left corner of the button.
        text (str): The text to be displayed on the button.
        color (tuple): The RGB color value for the button text, given as (R, G, B).

    Returns:
        pygame.Rect: A rectangle object representing the area of the screen updated by the button.
    """
    font = BUTTON_FONT
    text_render = font.render(text, True, color)
    _, _, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen_var, (200, 200, 200), (x, y), (x + w, y), 5)
    pygame.draw.line(screen_var, (200, 200, 200), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen_var, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen_var, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen_var, (100, 100, 100), (x, y, w, h))
    return screen_var.blit(text_render, (x, y))
def show_score(screen, font, score_value):
    """
    Displays the current score on the screen. The score represents the number of aliens
    eliminated by the player.
    """
    font_render = font.render(f'Score: {score_value}', True, (255, 255, 255))
    screen.blit(font_render, (60, 10))


def show_bullet_use(screen, font, bullet_use):
    """
    Displays the number of bullets used by the player on the screen.
    """
    font_render = font.render(f'Fire: {bullet_use}', True, (255, 255, 255))
    screen.blit(font_render, (350, 10))


def show_alien_die(screen, font, alien_die):
    """
    Displays the count of aliens killed by the player on the screen.
    """
    font_render = font.render(f'Kill: {alien_die}', True, (255, 255, 255))
    screen.blit(font_render, (620, 10))

def show_text(text: str, x: int, y: int) -> None:
    """
    Displays a specified text message on the screen, typically used for game over messages
    when the player's character collides with an alien.

    Args:
        text (str): The message to be displayed.
        x (int): The x-coordinate for the text's position.
        y (int): The y-coordinate for the text's position.

    Note:
        This function draws a background rectangle behind the text for enhanced visibility.
    """
    font_render = GAME_OVER_FONT.render(text, True, (230, 230, 230))
    _, _, w, h = font_render.get_rect()
    pygame.draw.rect(screen, (50, 50, 50), (x, y, w, h - 7))
    screen.blit(font_render, (x, y))
