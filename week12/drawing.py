import pygame
import sys

class Game:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))

        # Define some colors
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.CYAN = (0, 255, 255)
        self.YELLOW = (255, 255, 0)
        
    def draw_rectangle(self, x, y, w, h):
        # Draw a red rectangle
        pygame.draw.rect(self.window, self.RED, (x, y, w, h))
        
    def draw_circle(self, center, radius):
        # Draw a green circle
        pygame.draw.circle(self.window, self.GREEN, center, radius)

    def draw_line(self, start_position, end_position, width):
        # Draw a blue line
        pygame.draw.line(self.window, self.BLUE, start_position, end_position, width)

    def draw_triangle(self, point1, point2, point3):
        pygame.draw.polygon(self.window, self.CYAN, (point1, point2, point3))

    def draw_ellipse(self, x, y, w, h):
        pygame.draw.ellipse(self.window, self.YELLOW, (x, y, w, h))


    def draw_shapes(self):
        self.draw_rectangle(50, 50, 200, 100)
        self.draw_circle((400, 300), 50)
        self.draw_line((600, 100), (700, 500), 5)
        self.draw_triangle((100, 500), (200, 500), (150, 400))
        self.draw_ellipse(200, 50, 200, 100)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Fill the window with black
            self.window.fill((0, 0, 0))
            
            # Draw shapes
            self.draw_shapes()
            
            # Update the display
            pygame.display.flip()

# Instantiate and run the game
game = Game()
game.run()
