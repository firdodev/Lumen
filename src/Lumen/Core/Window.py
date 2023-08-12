import pygame
from Lumen.Graphics import AudioVisualizer

class Window:
    def __init__(self, title="Default Title", width=300, height=200):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.visualizer = AudioVisualizer.AudioVisualizer(self.screen)

    def show(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.visualizer.update_visualization()
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
