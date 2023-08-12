import pygame
from Lumen.Graphics import AudioVisualizer

class Window:
    def __init__(self, title="Lumen", width=300, height=200):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.max_radius = max(self.center_x, self.center_y)

        self.visualizer = AudioVisualizer.AudioVisualizer(self.screen)

        # Create a Surface for the gradient
        self.gradient_surface = pygame.Surface((self.width, self.height))
        self.draw_radial_gradient()

    def get_radial_gradient_color(self, x, y, inner_color, outer_color):
        dx = x - self.center_x
        dy = y - self.center_y
        distance = (dx**2 + dy**2)**0.5
        t = distance / self.max_radius

        r = int(inner_color[0] * (1 - t) + outer_color[0] * t)
        g = int(inner_color[1] * (1 - t) + outer_color[1] * t)
        b = int(inner_color[2] * (1 - t) + outer_color[2] * t)

        # Clamp the values to [0, 255]
        r = max(0, min(r, 255))
        g = max(0, min(g, 255))
        b = max(0, min(b, 255))

        return (r, g, b)

    def draw_radial_gradient(self):
        inner_color = (10, 10, 40)
        outer_color = (0, 0, 0)

        for y in range(self.height):
            for x in range(self.width):
                self.gradient_surface.set_at((x, y), self.get_radial_gradient_color(x, y, inner_color, outer_color))

    def show(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Blit the gradient surface instead of regenerating the gradient
            self.screen.blit(self.gradient_surface, (0, 0))
            self.visualizer.update_visualization()
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
