import pygame

import constants
from player import Player
from room import Room


class World:
    def __init__(self):
        self.sprites = pygame.sprite.Group()
        self.player = Player(90, 300, 50, 50)
        self.sprites.add(self.player)

        self.rooms = [Room("level1.txt"), Room("level2.txt")]
        self.current_room = 0
        self.boundary_size = 200
        self.right_boundary = constants.SCREEN_WIDTH - self.boundary_size
        self.left_boundary = self.boundary_size

        self.player.set_room(self.rooms[self.current_room])

    def calculate_right_diff(self):
        return self.player.rect.right - self.right_boundary

    def calculate_left_diff(self):
        return self.left_boundary - self.player.rect.left

    def key_down(self, key):
        self.player.key_down(key)

    def key_up(self, key):
        self.player.key_up(key)

    def update(self):
        # --- Game Logic ---
        self.sprites.update()
        self.rooms[self.current_room].update()
        # Player status
        if self.player.rect.right >= constants.SCREEN_WIDTH:
            self.player.rect.right = constants.SCREEN_WIDTH
        elif self.player.rect.left <= 0:
            self.player.rect.left = 0
        # self.shift_world()

    def draw(self, screen):
        self.rooms[self.current_room].draw(screen)
        self.sprites.draw(screen)

    def shift_world(self):
        # current_position_right = self.player.rect.right + self.rooms[self.current_room].world_shift
        # current_position_left = self.player.rect.left + self.rooms[self.current_room].world_shift
        # print(self.rooms[self.current_room].world_shift, current_position_right)
        # # If the player gets near the right side, shift the world left (-x)
        # if current_position_right >= constants.SCREEN_WIDTH - self.boundary_size:
        #     pass
        # el
        if self.player.rect.right >= self.right_boundary:
            diff = self.calculate_right_diff()
            self.player.rect.right = self.right_boundary
            self.rooms[self.current_room].shift_world(-diff)
        # If the player gets near the left side, shift the world right (+x)
        if self.player.rect.left <= self.left_boundary:
            diff = self.calculate_left_diff()
            self.player.rect.left = self.left_boundary
            self.rooms[self.current_room].shift_world(diff)

        # # If the player gets to the end of the level, go to the next level
        current_position = self.player.rect.left + self.rooms[self.current_room].world_shift
        if current_position <= 0:
            self.player.rect.left = self.left_boundary
            if self.current_room < len(self.rooms) - 1:
                self.current_room += 1
                self.player.set_room(self.rooms[self.current_room])
