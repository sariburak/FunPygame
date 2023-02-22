import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200, 800))
background = pygame.Surface(screen.get_size())
background.fill(pygame.Color('#000000'))

clock = pygame.time.Clock()
is_running = True

attractor_position = pygame.math.Vector2(screen.get_size()[0] / 2, screen.get_size()[1] / 2)
attractor_velocity = pygame.Vector2(0, 0)
attractor_acc = pygame.Vector2(0, 0)
attractor_mass = 100

balls_positions = []
balls_velocities = []
balls_accelerations = []
balls_masses = []

for _ in range(200):
    balls_positions.append(pygame.math.Vector2(random.uniform(30, screen.get_size()[0] - 30), random.uniform(30, screen.get_size()[1] - 30))) # 610 and 450 optimized for (640, 480) width and height
    balls_velocities.append(pygame.Vector2(random.random() * 2, random.random() * 2))
    balls_accelerations.append(pygame.Vector2(0, 0))
    balls_masses.append(100)

def calculateAttractionForce(attractorPos, attractorMass, attractedPos, attractedMass):
    direction = attractorPos - attractedPos
    distance_squared = direction.magnitude_squared()
    distance_squared = min(max(distance_squared,  1000), 5000) # 900 is radios squared
    direction.normalize_ip()
    force = (attractorMass * attractedMass) / distance_squared
    return direction * force


def applyAcceleration(velocity, acceleration):
    velocity += acceleration

def applyVelocity(pos, velocity):
    pos += velocity

def findAcceleration(force, mass):
    return force / mass

def game_loop():
    global attractor_position, attractor_velocity, attractor_acc
    for ball_position, ball_velocity, ball_acceleration, ball_mass in zip(balls_positions, balls_velocities, balls_accelerations, balls_masses):
        force = calculateAttractionForce(attractor_position, attractor_mass, ball_position, ball_mass)
        ball_acceleration = findAcceleration(force, ball_mass)
        applyVelocity(ball_position, ball_velocity)
        applyAcceleration(ball_velocity, ball_acceleration)


def draw():
    pygame.draw.circle(screen, (255, 255, 255), attractor_position, 30, 1)
    for ball_position in balls_positions:
        pygame.draw.circle(screen, (255, 255, 255), ball_position, 10, 1)


while is_running:
    time_delta = clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False


    screen.blit(background, (0, 0))
    game_loop()
    draw()
    pygame.display.update()