import pygame
import pygame_gui

# setup and display a empty pygame screen
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.Surface(screen.get_size())
background.fill(pygame.Color('#000000'))

# Create a Pygame GUI manager
gui_manager = pygame_gui.UIManager((screen_width, screen_height))

shrink_rate = 0.70
rotate_angle = 60

# Create a slider at the top right corner
shrinkRateSlider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((screen_width-210, 10), (200, 50)),
    start_value=shrink_rate * 100,
    value_range=(0, 70),
    manager=gui_manager
)

rotateAngleSlider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((screen_width-210, 70), (200, 50)),
    start_value=rotate_angle,
    value_range=(0, 90),
    manager=gui_manager
)

offsetSlider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((screen_width-210, 130), (200, 50)),
    start_value=100,
    value_range=(100, 200),
    manager=gui_manager
)

# setup clock and running flag
clock = pygame.time.Clock()
is_running = True

# starting pos, direction, offset
initial_sp = sw, sh = (screen_width / 2, screen_height - 10)
initial_direction = pygame.math.Vector2(0, -1)
initial_offset = 100


def drawFractal(sp, direction, offset):
    pygame.draw.line(screen, (255, 255, 255), sp, sp + (direction * offset), 1)
    if offset > 1:
        new_offset = offset * shrink_rate
        new_direction = direction.rotate(rotate_angle)
        drawFractal(sp + (direction * offset), new_direction, new_offset)
        new_direction = direction.rotate(-rotate_angle)
        drawFractal(sp + (direction * offset), new_direction, new_offset)

while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        gui_manager.process_events(event)

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == shrinkRateSlider:
                    shrink_rate = event.value / 100
                elif event.ui_element == rotateAngleSlider:
                    rotate_angle = event.value
                elif event.ui_element == offsetSlider:
                    initial_offset = event.value


    # update
    gui_manager.update(time_delta)

    screen.blit(background, (0, 0))

    # Draw the Pygame GUI manager
    gui_manager.draw_ui(screen)

    drawFractal(initial_sp, initial_direction, initial_offset)
    pygame.display.update()