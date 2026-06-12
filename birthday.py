import pygame
import random
import math

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Birthday Pratik 🎉")

clock = pygame.time.Clock()

# ---------------------------
# Music
# ---------------------------

try:
    pygame.mixer.music.load("birthday_song.mp3")
    pygame.mixer.music.play(-1)
except:
    print("birthday_song.mp3 not found")

# ---------------------------
# Fonts
# ---------------------------

title_font = pygame.font.SysFont("arial", 60, bold=True)
msg_font = pygame.font.SysFont("arial", 30, bold=True)

# ---------------------------
# Stars
# ---------------------------

stars = []

for _ in range(120):
    stars.append([
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        random.randint(1, 3)
    ])

# ---------------------------
# Balloons
# ---------------------------

class Balloon:

    def __init__(self):

        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(HEIGHT, HEIGHT + 500)

        self.color = random.choice([
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 255, 255)
        ])

        self.speed = random.uniform(1, 3)

    def move(self):

        self.y -= self.speed

        if self.y < -50:

            self.y = HEIGHT + 100
            self.x = random.randint(50, WIDTH - 50)

    def draw(self):

        pygame.draw.ellipse(
            screen,
            self.color,
            (self.x, self.y, 40, 60)
        )

        pygame.draw.line(
            screen,
            (255, 255, 255),
            (self.x + 20, self.y + 60),
            (self.x + 20, self.y + 100),
            2
        )

balloons = [Balloon() for _ in range(25)]

# ---------------------------
# Confetti
# ---------------------------

confetti = []

for _ in range(250):

    confetti.append([
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        random.choice([
            (255, 0, 0),
            (255, 255, 0),
            (0, 255, 0),
            (0, 255, 255),
            (255, 0, 255)
        ]),
        random.randint(2, 5)
    ])

# ---------------------------
# Fireworks
# ---------------------------

class Firework:

    def __init__(self):

        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(80, 300)

        self.color = random.choice([
            (255, 0, 0),
            (255, 255, 0),
            (0, 255, 255),
            (0, 255, 0),
            (255, 0, 255)
        ])

        self.radius = 5

    def draw(self):

        for angle in range(0, 360, 20):

            end_x = self.x + math.cos(
                math.radians(angle)
            ) * self.radius

            end_y = self.y + math.sin(
                math.radians(angle)
            ) * self.radius

            pygame.draw.line(
                screen,
                self.color,
                (self.x, self.y),
                (end_x, end_y),
                3
            )

        self.radius += 2

fireworks = []

timer = 0

# ---------------------------
# Cake
# ---------------------------

def draw_cake():

    pygame.draw.rect(
        screen,
        (139, 69, 19),
        (430, 450, 340, 120)
    )

    pygame.draw.rect(
        screen,
        (255, 182, 193),
        (470, 380, 260, 80)
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (510, 330, 180, 60)
    )

    candle_positions = [540, 600, 660]

    for x in candle_positions:

        pygame.draw.rect(
            screen,
            (255, 255, 0),
            (x, 270, 10, 60)
        )

        flame_color = random.choice([
            (255, 255, 0),
            (255, 165, 0),
            (255, 69, 0)
        ])

        pygame.draw.circle(
            screen,
            flame_color,
            (x + 5, 255),
            10
        )

# ---------------------------
# Main Loop
# ---------------------------

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 10, 30))

    # Stars
    for star in stars:

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (star[0], star[1]),
            star[2]
        )

    # Title Glow
    glow = title_font.render(
        "HAPPY BIRTHDAY PALLAVI",
        True,
        (255, 215, 0)
    )

    screen.blit(
        glow,
        (WIDTH // 2 - glow.get_width() // 2, 40)
    )

    # Message
    msg = msg_font.render(
        "Wishing you happiness, success and lots of fun!",
        True,
        (255, 255, 255)
    )

    screen.blit(
        msg,
        (WIDTH // 2 - msg.get_width() // 2, 120)
    )

    # Balloons
    for balloon in balloons:
        balloon.move()
        balloon.draw()

    # Confetti
    for c in confetti:

        pygame.draw.circle(
            screen,
            c[2],
            (c[0], c[1]),
            c[3]
        )

        c[1] += 1

        if c[1] > HEIGHT:
            c[1] = 0

    # Cake
    draw_cake()

    # Fireworks
    timer += 1

    if timer % 40 == 0:
        fireworks.append(Firework())

    for fw in fireworks[:]:

        fw.draw()

        if fw.radius > 80:
            fireworks.remove(fw)

    pygame.display.flip()

pygame.quit()

