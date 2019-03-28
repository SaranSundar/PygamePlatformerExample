import pygame

import constants


class Player(pygame.sprite.Sprite):
    right = False
    left = False
    up = False
    down = False
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
        self.delta_x = 5
        self.delta_y = 5
        self.room = None

    def key_down(self, key):
        if key == pygame.K_LEFT:
            self.left = True
        elif key == pygame.K_RIGHT:
            self.right = True
        elif key == pygame.K_UP:
            self.up = True
            self.jump()
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

    def calc_gravity(self):
        """ Calculate effect of gravity."""
        if self.delta_y == 0:
            self.delta_y = 1
        else:
            # Acceleration for gravity
            self.delta_y += 0.35

        # See if we are on the ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.delta_y >= 0:
            self.delta_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hit's the up arrow key"""
        # move down a bit and see if there is a platform below us
        # Move down 2 pixels because it doesnt work well if we only move down 1 for moving platforms
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.room.collision_blocks, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            # Jump Height
            self.delta_y = -10

    # Use booleans for movement and update based on booleans in update method
    def update(self):
        # Gravity
        self.calc_gravity()

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
        self.rect.y += self.delta_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.room.collision_blocks, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.delta_y < 0:
                self.rect.top = block.rect.bottom
            elif self.delta_y > 0:
                self.rect.bottom = block.rect.top

            # Stop our vertical movement if you hit something
            self.delta_y = 0
