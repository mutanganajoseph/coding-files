import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Simple Ball in a Box')

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up clock for FPS
clock = pygame.time.Clock()

# Ball settings
ball_pos = [250, 250]
ball_radius = 20
ball_velocity = [2, 3]
gravity = 0.1

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen

    # Handle events (keypresses)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update physics (gravity, movement)
    ball_velocity[1] += gravity  # Add gravity to Y velocity
    ball_pos[0] += ball_velocity[0]  # Update X position
    ball_pos[1] += ball_velocity[1]  # Update Y position

    # Ball collision with the walls
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > 500:
        ball_velocity[0] *= -1  # Reverse X direction on hit
    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > 500:
        ball_velocity[1] *= -1  # Reverse Y direction on hit

    # Draw the ball
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Frame rate control (60 FPS)

pygame.quit()
