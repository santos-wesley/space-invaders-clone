import pygame

def load_image(image_path):
    """
    Loads an image from disk.

    Args:
    image_path (str): The path to the image file.

    Returns:
    pygame.Surface: The loaded image.
    """
    return pygame.image.load(image_path)

def load_sound(sound_path):
    """
    Loads a sound from disk.

    Args:
    sound_path (str): The path to the sound file.

    Returns:
    pygame.mixer.Sound: The loaded sound.
    """
    return pygame.mixer.Sound(sound_path)
