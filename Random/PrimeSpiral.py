import pygame
import math
import colorsys
from time import sleep

def main():
    pygame.init()
    pygame.font.init()
    modes = ["dots", "dots_with_lines", "numbers", "hex_numbers", "heatmap"]

    # Config
    width = 1000
    height = 1000
    cell_size = 40
    mode = modes[2]

    global screen
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption("Prime Spiral")

    # Running numbers
    number = 1
    count = 0
    turn_count = 0
    moves_per_turn = 1
    x = 0
    y = 0

    global running
    running = True
    screen.fill((0, 0, 0))
    p_x_pos = -1
    p_y_pos = -1

    heatmap_points = []
    max_dist = cell_size * 3
    heatmap_done = False

    while running:
        check_for_interrupt()

        x_pos = width / 2 + x * cell_size
        y_pos = height / 2 + y * cell_size
        
        if x_pos >= 0 and x_pos <= width and y_pos >= 0 and y_pos <= height:
            match mode:
                case "dots":
                    if is_prime(number):
                        pygame.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), cell_size * 0.3)
                    pygame.display.flip()
                    sleep(0.05)
                case "dots_with_lines":
                    if is_prime(number):
                        pygame.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), cell_size * 0.3)
                    if p_x_pos >= 0 and p_y_pos >= 0:
                        pygame.draw.line(screen, (255, 255, 255), (p_x_pos, p_y_pos), (x_pos, y_pos), int(cell_size * 0.1))
                    p_x_pos = x_pos
                    p_y_pos = y_pos
                    pygame.display.flip()
                    sleep(0.05)
                case "numbers":
                    color = (255, 255, 255)
                    if is_prime(number):
                        color = (255, 0, 0)
                    draw_text_centered(number, cell_size * 0.6, (x_pos, y_pos), color)
                    pygame.display.flip()
                    sleep(0.05)
                case "hex_numbers":
                    color = (255, 255, 255)
                    if is_prime(number):
                        color = (255, 0, 0)
                    draw_text_centered(hex(number)[2:].upper(), cell_size * 0.6, (x_pos, y_pos), color)
                    pygame.display.flip()
                    sleep(0.05)
                case "heatmap":
                    if is_prime(number):
                        print(f"{number} is prime")
                        heatmap_points.append((x_pos, y_pos))
                        

            match turn_count % 4:
                case 0:
                    x += 1
                case 1:
                    y += 1
                case 2:
                    x -= 1
                case 3:
                    y -= 1

            number += 1
            count += 1

            if count >= moves_per_turn:
                turn_count += 1
                count = 0
                if turn_count % 2 == 0:
                    moves_per_turn += 1
            
        elif not heatmap_done and mode == "heatmap":
            screen.fill((0, 0, 255))
            for x2 in range(width):
                if check_for_interrupt():
                    break
                print(f"Heatmap progress: {round(((x2 + 1) / width) * 100, 1)}%")
                for y2 in range(height):
                    shortest_dist = width * height
                    for pos in heatmap_points:
                        dist = math.hypot(pos[0] - x2, pos[1] - y2)
                        if dist < shortest_dist:
                            shortest_dist = dist

                    shortest_dist = min(shortest_dist, max_dist)        
                    percent_val = shortest_dist / max_dist

                    color = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(0.83, 1 - percent_val, 1))

                    #val1 = 255 * ((shortest_dist % (max_dist/3)) / (max_dist/3)) if math.floor(shortest_dist / (max_dist/3)) == 0 else 0
                    #val2 = 255 * ((shortest_dist % (max_dist/3)) / (max_dist/3)) if math.floor(shortest_dist / (max_dist/3)) == 1 else 0
                    #val3 = 255 * ((shortest_dist % (max_dist/3)) / (max_dist/3)) if math.floor(shortest_dist / (max_dist/3)) == 2 else 0

                    #color = (val1, val2, val3)
                    screen.set_at((x2, y2), color)
            pygame.display.flip()
            heatmap_done = True


    pygame.quit()

def draw_text_centered(text: str, size: int | float, pos: tuple[int, int], color: tuple[int, int, int] = (0, 0, 0)):
    if len(str(text)) >= 3:
        size *= math.pow(0.8, len(str(text)) - 2)

    if type(text) == int or type(text) == float:
        text = str(text)
    if type(size) == float:
        size = int(size)

    text_font = pygame.font.SysFont("Comic Sans MS", size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()

    new_pos = (pos[0] - text_rect.width / 2, pos[1] - text_rect.height / 2)
    screen.blit(text_surface, new_pos)

def is_prime(number: int):
    if number == 1:
        return False
    i = 2
    max = math.sqrt(number)
    while i <= max:
        if number % i == 0:
            return False
        i += 1
    return True

def check_for_interrupt():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                return True
    return False

main()