import pygame
import pygame_gui

pygame.init()

# Set up the Pygame window
window_size = (640, 480)
pygame.display.set_mode(window_size)

# Create a Pygame GUI manager
gui_manager = pygame_gui.UIManager(window_size)

# Create a slider element
slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((50, 50), (200, 50)),
    start_value=50,
    value_range=(0, 100),
    manager=gui_manager
)

# Define a global variable to hold the slider value
global slider_value
slider_value = 50

# Main game loop
while True:
    time_delta = pygame.time.Clock().tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Update the Pygame GUI manager with the current event
        gui_manager.process_events(event)

        # Check if the slider value has changed
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                slider_value = int(event.value)

    # Update the Pygame GUI manager
    gui_manager.update(time_delta)

    # Draw the Pygame GUI manager
    gui_manager.draw_ui(pygame.display.get_surface())

    # Update the Pygame display
    pygame.display.update()
