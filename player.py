import pygame

import constants


class Player(pygame.sprite.Sprite):
    right = False
    left = False
    up = False
    down = False
    speed = 5
    scale = 1.75

    def __init__(self, x, y, w, h):
        super().__init__()
        # self.image = pygame.image.load("metabee_spritesheet.png").convert()
        self.image = pygame.Surface([w, h])
        self.image.fill(constants.TEAL)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set speed vector of player
        self.delta_x = 2
        self.delta_y = 2
        self.room = None

    def key_down(self, key):
        if key == pygame.K_LEFT:
            self.left = True
        elif key == pygame.K_RIGHT:
            self.right = True
        elif key == pygame.K_UP:
            self.up = True
        elif key == pygame.K_DOWN:
            self.down = True

    def key_up(self, key):
        if key == pygame.K_LEFT:
            self.left = False
        elif key == pygame.K_RIGHT:
            self.right = False
        elif key == pygame.K_UP:
            self.up = False
        elif key == pygame.K_DOWN:
            self.down = False

    def set_room(self, room):
        self.room = room

    # Use booleans for movement and update based on booleans in update method
    def update(self):
        """ Move the player. """

        # Move left/right
        if self.right:
            self.rect.x += self.delta_x
        elif self.left:
            self.rect.x -= self.delta_x

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.room.collision_blocks, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.right:
                self.rect.right = block.rect.left
            elif self.left:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        if self.up:
            self.rect.y -= self.delta_y
        elif self.down:
            self.rect.y += self.delta_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.room.collision_blocks, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.up:
                self.rect.top = block.rect.bottom
            elif self.down:
                self.rect.bottom = block.rect.top
