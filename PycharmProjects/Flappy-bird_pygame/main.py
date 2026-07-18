import pygame
import random
import time
pygame.init()
pygame.mixer.init()
# =========================
# COLORS
# =========================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
GOLD = (255, 215, 0)


# =========================
# SCREEN
# =========================

WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()



# =========================
# LOAD ASSETS
# =========================


# Bird

bird_images = [
    pygame.image.load("assets/flap1.png"),
    pygame.image.load("assets/flap2.png")
]


bird_images[0] = pygame.transform.scale(
    bird_images[0],
    (60, 60)
)

bird_images[1] = pygame.transform.scale(
    bird_images[1],
    (60, 60)
)



# Background

background = pygame.image.load(
    "assets/background.png"
)

background = pygame.transform.scale(
    background,
    (WIDTH, HEIGHT)
)



# Coin

coin_img = pygame.image.load(
    "assets/coin.png"
)

coin_img = pygame.transform.scale(
    coin_img,
    (35, 35)
)



# Sounds

pygame.mixer.music.load(
    "assets/music.mp3"
)


game_over_sound = pygame.mixer.Sound(
    "assets/game_over.wav"
)



# =========================
# VARIABLES
# =========================


bird_width = 60
bird_height = 60


score = 0
high_score = 0


paused = False



# =========================
# TEXT FUNCTION
# =========================


def draw_text(text, size, x, y, color=WHITE):

    font = pygame.font.Font(
        None,
        size
    )

    img = font.render(
        text,
        True,
        color
    )

    screen.blit(
        img,
        (x, y)
    )



# =========================
# START MENU
# =========================


def start_menu():

    while True:


        screen.blit(
            background,
            (0, 0)
        )


        box = pygame.Surface(
            (520, 260)
        )

        box.set_alpha(170)

        box.fill(BLACK)


        screen.blit(
            box,
            (140, 110)
        )



        draw_text(
            "FLAPPY BIRD",
            70,
            205,
            150,
            GOLD
        )


        draw_text(
            "PRESS SPACE TO START",
            35,
            230,
            260
        )


        draw_text(
            "P = Pause",
            25,
            330,
            320
        )



        pygame.display.update()



        for event in pygame.event.get():


            if event.type == pygame.QUIT:

                pygame.quit()
                quit()



            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    return



# =========================
# PAUSE SCREEN
# =========================


def pause_screen():


    while True:


        overlay = pygame.Surface(
            (WIDTH, HEIGHT)
        )

        overlay.set_alpha(150)

        overlay.fill(BLACK)


        screen.blit(
            overlay,
            (0,0)
        )



        draw_text(
            "PAUSED",
            80,
            280,
            180,
            GOLD
        )


        draw_text(
            "Press P to Resume",
            35,
            250,
            280
        )


        pygame.display.update()



        for event in pygame.event.get():


            if event.type == pygame.QUIT:

                pygame.quit()
                quit()



            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_p:

                    return
# =========================
# DRAW PIPES
# =========================


def draw_pipes(pipe_x, pipe_height, gap):

    pygame.draw.rect(
        screen,
        GREEN,
        (
            pipe_x,
            0,
            60,
            pipe_height
        )
    )


    pygame.draw.rect(
        screen,
        GREEN,
        (
            pipe_x,
            pipe_height + gap,
            60,
            HEIGHT
        )
    )



# =========================
# SCORE
# =========================


def show_score():

    draw_text(
        f"Score: {score}",
        30,
        10,
        10
    )


    draw_text(
        f"High Score: {high_score}",
        25,
        10,
        45
    )



# =========================
# GAME OVER
# =========================


def game_over():

    global high_score


    pygame.mixer.music.stop()

    game_over_sound.play()



    if score > high_score:

        high_score = score



    while True:


        screen.blit(
            background,
            (0,0)
        )


        draw_text(
            "GAME OVER",
            80,
            220,
            160,
            GOLD
        )


        draw_text(
            f"Score: {score}",
            40,
            330,
            260
        )


        draw_text(
            "SPACE = Restart",
            35,
            270,
            330
        )



        pygame.display.update()



        for event in pygame.event.get():


            if event.type == pygame.QUIT:

                pygame.quit()
                quit()



            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_SPACE:

                    main()

                    return




# =========================
# MAIN GAME
# =========================


def main():

    global score
    global paused



    x = 150
    y = 220



    velocity = 0

    gravity = 0.4

    jump = -8



    # PIPE

    pipe_x = WIDTH

    pipe_height = random.randint(
        80,
        300
    )

    gap = 190

    pipe_speed = 5



    # COIN

    coin_x = 900

    coin_y = random.randint(
        100,
        350
    )


    coin_taken = False



    score = 0



    pygame.mixer.music.play(-1)



    while True:


        for event in pygame.event.get():


            if event.type == pygame.QUIT:

                pygame.quit()
                quit()



            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_SPACE:

                    velocity = jump



                if event.key == pygame.K_p:

                    pause_screen()



        # Gravity

        velocity += gravity

        y += velocity



        # Background

        screen.blit(
            background,
            (0,0)
        )



        # Bird animation

        screen.blit(
            bird_images[0],
            (x,y)
        )



        # Pipes

        draw_pipes(
            pipe_x,
            pipe_height,
            gap
        )



        pipe_x -= pipe_speed



        if pipe_x < -60:


            pipe_x = WIDTH


            pipe_height = random.randint(
                80,
                300
            )


            score += 1



        # =====================
        # COINS
        # =====================


        if not coin_taken:

            screen.blit(
                coin_img,
                (
                    coin_x,
                    coin_y
                )
            )


        coin_x -= pipe_speed



        if coin_x < -40:


            coin_x = 900

            coin_y = random.randint(
                100,
                350
            )

            coin_taken = False



        bird_rect = pygame.Rect(
            x,
            y,
            bird_width,
            bird_height
        )



        coin_rect = pygame.Rect(
            coin_x,
            coin_y,
            35,
            35
        )



        if bird_rect.colliderect(
            coin_rect
        ):


            coin_taken = True

            score += 5




        # =====================
        # COLLISION
        # =====================


        if y < 0 or y > HEIGHT - bird_height:

            game_over()



        top_pipe = pygame.Rect(
            pipe_x,
            0,
            60,
            pipe_height
        )


        bottom_pipe = pygame.Rect(
            pipe_x,
            pipe_height + gap,
            60,
            HEIGHT
        )



        if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):

            game_over()



        show_score()



        pygame.display.update()


        clock.tick(60)




# =========================
# START PROGRAM
# =========================


start_menu()

main()


pygame.quit()
quit()