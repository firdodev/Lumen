import os
import pygame

def LoadFont(filename, size):
    """
    Load a font from the Assets/Fonts directory.

    Parameters:
    - filename: Name of the font file (e.g. 'Poppins-Regular.ttf')
    - size: Size of the font

    Returns:
    - A pygame Font object
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(current_directory, '..', '..', '..', 'Assets', 'Fonts', filename)
    font = pygame.font.Font(font_path, size)
    return font
