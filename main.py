import pygame
import sys
import threading
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stack Visualization in Real-Time")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.SysFont(None, 24)

array = []  # This array will be shared between threads


def draw_array(array):
    screen.fill(WHITE)
    element_width = 40
    element_height = 50
    array_start_x = (SCREEN_WIDTH - element_width * len(array)) // 2
    array_start_y = (SCREEN_HEIGHT - element_height) // 2

    for i, item in enumerate(array):
        element_x = array_start_x + i * element_width
        element_y = array_start_y
        pygame.draw.rect(screen, BLACK, (element_x, element_y, element_width, element_height), 1)
        text = font.render(str(item), True, BLACK)
        text_x = element_x + (element_width - text.get_width()) // 2
        text_y = element_y + (element_height - text.get_height()) // 2
        screen.blit(text, (text_x, text_y))

    if array:
        last_element_x = array_start_x + (len(array) - 1) * element_width + element_width // 2
        arrow_y = array_start_y + element_height + 10  # Adjust this value as needed
        pygame.draw.polygon(screen, BLACK, [(last_element_x, arrow_y), (last_element_x - 10, arrow_y + 20),
                                            (last_element_x + 10, arrow_y + 20)])

    pygame.display.flip()


def handle_input():
    global array
    print("We will be learning about Data Structures")

    while True:
        item = input("Push a number: ")
        if item.isdigit():
            array.append(int(item))
        elif item == 'quit':
            pygame.quit()
            sys.exit()
        elif item == "pop":
            array.pop()


def main():
    input_thread = threading.Thread(target=handle_input,daemon=True)
    input_thread.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_array(array)
        time.sleep(0.1)  # Adding a slight delay to reduce CPU usage


if __name__ == "__main__":
    main()
