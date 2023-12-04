import pygame

# Initialize Pygame
pygame.init()

class Virus:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image

    def move(self):
        self.x += self.speed
        # Optional: Add code for random vertical movement as well

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))





# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Virus Attack Fortress Game")

# Load sprites
# Load and resize the virus sprite
virus_image = pygame.image.load("virus.png")
virus_image = pygame.transform.scale(virus_image, (50, 50))

# Virus list and spawn timer
viruses = []
SPAWN_VIRUS_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_VIRUS_EVENT, 5000)  # 5000 milliseconds = 5 seconds

fortress_sprite = pygame.image.load("fortress.png")
fortress_sprite = pygame.transform.scale(fortress_sprite, (400, 400))  # Resize fortress to 200x200

cannon_sprite = pygame.image.load("cannon.png")
cannon_sprite = pygame.transform.flip(cannon_sprite, True, False)  # Flip cannon horizontally
cannon_sprite = pygame.transform.scale(cannon_sprite, (100, 100))  # Resize cannon 

# Cannon position calculations
cannon_height = 50  # Assuming height of the cannon sprite
cannon_width = 50  # Assuming width of the cannon sprite

fortress_position = (400, 200)

# Positioning two cannons on the fortress
cannon_position1 = (fortress_position[0] + 50 , fortress_position[1] - cannon_height)
cannon_position2 = (fortress_position[0] + 325 - cannon_width, fortress_position[1] - cannon_height)

# Game Variables
virus_position = [0, 300]  # Starting position of the virus
virus_speed = 2  # Speed at which the virus moves

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for the virus spawn event
        if event.type == SPAWN_VIRUS_EVENT:
            for _ in range(12):  # Spawn 12 viruses
                new_virus = Virus(0, random.randint(0, screen_height - 50), random.uniform(0.5, 2), virus_image)
                viruses.append(new_virus)

    # Move and draw each virus
    for virus in viruses:
        virus.move()
        virus.draw(screen)

    # Game logic for cannon shooting would go here
    # This is where you'd handle keyboard/mouse events, collision detection, etc.

    # Drawing
    screen.fill((255, 255, 255))  # Clear screen with white background
    screen.blit(virus_image, virus_position)
    screen.blit(fortress_sprite, fortress_position)  # Adjust position as needed
    screen.blit(cannon_sprite, cannon_position1)  # Draw the first cannon
    screen.blit(cannon_sprite, cannon_position2)  # Draw the second cannon
    # Add cannons with similar blit method

    pygame.display.update()

# Quit Pygame
pygame.quit()
