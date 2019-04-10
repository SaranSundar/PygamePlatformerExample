import pygame

from player import Player
from room import Room

# Should only be seen if there is some error
BACKGROUND_COLOR = pygame.Color("red")


class World:
    def __init__(self):
        # Player variables
        self.player = Player(90, 300)
        self.rooms = [Room("level1.txt"), Room("level2.txt")]
        self.current_room = 0
        # Main Game Loop Variables
        self.done = False
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.screen = None

    def run(self, screen):
        self.screen = screen
        while not self.done:
            self.process_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(self.fps)

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.rooms[self.current_room].draw(self.screen)
        self.player.draw(self.screen)

    def update(self):
        # --- Game Logic ---
        self.player.set_room(self.rooms[self.current_room])
        self.player.update()

    def process_events(self):
        keys = pygame.key.get_pressed()
        self.player.process_keys(keys)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
