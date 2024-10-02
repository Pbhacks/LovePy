import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Matrix Sparkling Heart")

# Colors
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
GREEN = (0, 255, 0)

# Font setup for matrix effect
font = pygame.font.Font(None, 20)
matrix_characters = "01"

class MatrixStream:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)
        self.chars = [random.choice(matrix_characters) for _ in range(random.randint(5, 15))]
        self.colors = [(0, random.randint(50, 255), 0) for _ in range(len(self.chars))]

    def update(self):
        self.y += self.speed
        if random.random() < 0.1:
            self.chars = [random.choice(matrix_characters) for _ in range(len(self.chars))]

class Sparkle:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        speed = random.uniform(1, 3)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.lifetime = random.randint(20, 40)
        self.size = random.uniform(1, 3)
        self.color = RED
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1

def create_heart_points(cx, cy, size, num_points=30):
    points = []
    for i in range(num_points):
        t = i / num_points * 2 * math.pi
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        points.append((cx + x * size, cy - y * size))
    return points

def draw_heart(surface, points, color, width=0):
    if len(points) > 2:
        pygame.draw.polygon(surface, color, points, width)

def main():
    clock = pygame.time.Clock()
    sparkles = []
    matrix_streams = []
    base_size = 10
    running = True
    tick = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        
        # Update matrix streams
        if random.random() < 0.1:
            matrix_streams.append(MatrixStream(random.randint(0, width), -50))
        
        remaining_streams = []
        for stream in matrix_streams:
            stream.update()
            if stream.y < height + 50:
                for i, char in enumerate(stream.chars):
                    char_surface = font.render(char, True, stream.colors[i])
                    screen.blit(char_surface, (stream.x, stream.y + i * 20))
                remaining_streams.append(stream)
        matrix_streams = remaining_streams

        # Create pulsating effect
        tick += 1
        pulse = math.sin(tick / 20) * 2
        size = base_size + pulse
        
        # Generate heart points
        heart_points = create_heart_points(width//2, height//2, size)
        
        # Draw glowing effect (multiple layers of hearts)
        for i in range(10, 0, -1):
            glow_size = size + i/2
            glow_points = create_heart_points(width//2, height//2, glow_size)
            glow_color = (min(255, 100 + i * 15), 0, 0)
            draw_heart(screen, glow_points, glow_color, 1)
        
        # Draw solid heart
        draw_heart(screen, heart_points, RED)
        
        # Create sparkles around the heart
        if tick % 2 == 0:
            for _ in range(5):
                point_index = random.randint(0, len(heart_points) - 1)
                point = heart_points[point_index]
                angle = random.uniform(0, 2 * math.pi)
                sparkles.append(Sparkle(point[0], point[1], angle))
        
        # Update and draw sparkles
        remaining_sparkles = []
        for sparkle in sparkles:
            sparkle.update()
            if sparkle.lifetime > 0:
                pygame.draw.circle(screen, sparkle.color, 
                                  (int(sparkle.x), int(sparkle.y)), 
                                  int(sparkle.size))
                remaining_sparkles.append(sparkle)
        sparkles = remaining_sparkles
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
