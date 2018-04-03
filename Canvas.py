import pygame

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
light_red = (220, 0, 0)
blue = (0, 0, 255)
light_blue = (0, 0, 220)
green = (0, 255, 0)
light_green = (0, 220, 0)
black = (0, 0, 0)
light_black = (20, 20, 20)
gray = (220, 220, 220)
pink = (231, 62, 238)
light_pink = (236, 67, 242)
orange = (229, 160, 11)
light_orange = (234, 165, 16)
yellow = (238, 228, 62)
light_yellow = (242, 232, 67)
violet = (148, 0, 211)

button_size = 10
pen_size = 3
pen_color = black

screen_size = (1280, 720)

small_font = pygame.font.SysFont("freesansbold.ttf", 25)
large_font = pygame.font.SysFont("freesansbold.ttf", 35)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Paint App")
screen.fill(white)

clock = pygame.time.Clock()
fps = 1000

running = True
connected_to_server = False

while running:
    pygame.draw.rect(screen, gray, (100, 0, 900, 710), 1)
    pygame.draw.rect(screen, blue, (1100, 200, 100, 100)) #Replace by a better solution
    if connected_to_server:
        pen_size_text = small_font.render("Pen Size:", False, black)
        screen.blit(pen_size_text, (15, 20))

        pygame.draw.rect(screen, white, (70, 40, 30, 30))
        plus_pen_size_text = large_font.render("+", True, black)
        screen.blit(plus_pen_size_text, (70, 40))

        pygame.draw.rect(screen, white, (30, 40, 30, 30))
        minus_pen_size_text = large_font.render("-", True, black)
        screen.blit(minus_pen_size_text, (30, 40))

        color_text = small_font.render("Colors:", False, black)
        screen.blit(color_text, (20, 170))
        pygame.draw.rect(screen, red, (20, 200, 20, 20))
        pygame.draw.rect(screen, blue, (40, 200, 20, 20))
        pygame.draw.rect(screen, green, (60, 200, 20, 20))
        pygame.draw.rect(screen, black, (20, 220, 20, 20))
        pygame.draw.rect(screen, gray, (40, 220, 20, 20))
        pygame.draw.rect(screen, pink, (60, 220, 20, 20))
        pygame.draw.rect(screen, orange, (20, 240, 20, 20))
        pygame.draw.rect(screen, yellow, (40, 240, 20, 20))
        pygame.draw.rect(screen, violet, (60, 240, 20, 20))
        eraser_image = pygame.image.load("eraser.png")
        screen.blit(eraser_image, (40, 300))
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            #print(event)

            if event.type == pygame.QUIT:
                running = False

            if 100 < pos[0] < 1000 and 1 < pos[1] < 710: #Fix issue with large pen_size which paints the outside too
                if click[0] == 1:
                    pygame.draw.circle(screen, pen_color, pos, pen_size)

            elif 20 < pos[0] < 40 and 200 < pos[1] < 220: #See how you can make a button highlight
                # while 20 < pos[0] < 40 and 200 < pos[1] < 220:
                #     pygame.draw.rect(screen, light_red, (20, 200, 20, 20))
                # pygame.draw.rect(screen, red, (20, 200, 20, 20))
                if click[0] == 1:
                    pen_color = red

            elif 40 < pos[0] < 60 and 200 < pos[1] < 220:
                #pygame.draw.rect(screen, light_blue, (40, 200, 20, 20))
                if click[0] == 1:
                    pen_color = blue

            elif 60 < pos[0] < 80 and 200 < pos[1] < 220:
                #pygame.draw.rect(screen, light_green, (60, 200, 20, 20))
                if click[0] == 1:
                    pen_color = green

            elif 20 < pos[0] < 40 and 220 < pos[1] < 240:
                #pygame.draw.rect(screen, light_black, (20, 220, 20, 20))
                if click[0] == 1:
                    pen_color = black

            elif 40 < pos[0] < 60 and 220 < pos[1] < 240:
                #pygame.draw.rect(screen, light_red, (40, 220, 20, 20))
                if click[0] == 1:
                    pen_color = gray

            elif 60 < pos[0] < 80 and 220 < pos[1] < 240:
               #pygame.draw.rect(screen, light_pink, (60, 220, 20, 20))
                if click[0] == 1:
                    pen_color = pink

            elif 20 < pos[0] < 40 and 240 < pos[1] < 260:
                #pygame.draw.rect(screen, light_orange, (20, 240, 20, 20))
                if click[0] == 1:
                    pen_color = orange

            elif 40 < pos[0] < 60 and 240 < pos[1] < 260:
                #pygame.draw.rect(screen, light_yellow, (40, 240, 20, 20))
                if click[0] == 1:
                    pen_color = yellow

            elif 60 < pos[0] < 80 and 240 < pos[1] < 260:
                #pygame.draw.rect(screen, light_yellow, (40, 240, 20, 20))
                if click[0] == 1:
                    pen_color = violet

            elif 40 < pos[0] < 72 and 300 < pos[1] < 372:
                #pygame.draw.rect(screen, light_yellow, (40, 240, 20, 20))
                if click[0] == 1:
                    pen_color = white

            elif 70 < pos[0] < 100 and 40 < pos[1] < 70:
                #pygame.draw.rect(screen, light_yellow, (40, 240, 20, 20))
                if click[0] == 1 and pen_size < 40:
                    pen_size += 3

            elif 30 < pos[0] < 60 and 40 < pos[1] < 70:
                #pygame.draw.rect(screen, light_yellow, (40, 240, 20, 20))
                if click[0] == 1 and pen_size > 0:
                    pen_size -= 3

    else:
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if 1100 < pos[0] < 1200 and 200 < pos[1] < 300:
                if click[0] == 1:
                    connected_to_server = True

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()





