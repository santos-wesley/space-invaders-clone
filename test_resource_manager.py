import unittest
import pygame
from resource_manager import load_image, load_sound

class TestResourceManager(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        """Set up Pygame before any tests run."""
        pygame.init()
        pygame.mixer.init()

    @classmethod
    def tearDownClass(cls):
        """Tear down Pygame after all tests have run."""
        pygame.quit()

    def test_load_valid_image(self):
        """Test loading a valid image file."""
        image_path = 'images/bg.jpg'  # Replace with a valid image path
        image = load_image(image_path)
        self.assertIsInstance(image, pygame.Surface)

    def test_load_invalid_image(self):
        """Test loading an invalid image file."""
        image_path = 'musics/won.wav'
        with self.assertRaises(pygame.error):
            load_image(image_path)

    def test_load_valid_sound(self):
        """Test loading a valid sound file."""
        sound_path = 'musics/won.wav'  
        sound = load_sound(sound_path)
        self.assertIsInstance(sound, pygame.mixer.Sound)

    def test_load_invalid_sound(self):
        """Test loading an invalid sound file."""
        sound_path = 'images/bg.jpg'
        with self.assertRaises(pygame.error):
            load_sound(sound_path)

if __name__ == '__main__':
    unittest.main()
