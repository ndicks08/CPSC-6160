import pygame
import math
import Inventory

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)
    
    def update(self, target):
        # Center the camera on the target (player)
        x = -target.rect.x + int(self.width / 2)
        y = -target.rect.y + int(self.height / 2)

        # Prevent the camera from moving beyond the room boundaries
        # Assuming room size is same as screen size for simplicity
        x = 0
        y = 0

        self.camera = pygame.Rect(x, y, self.width, self.height)

class Character(pygame.sprite.Sprite):
    def __init__(self, position, width, height):
        
        #load sprite sheet
        self.sheet = pygame.image.load('sprites/detective.png').convert_alpha()
        self.position = list(position)
        
        #lighting
        self.fog = pygame.Surface((width, height))
        self.fog.fill((20,20,20))
        self.light_mask = pygame.image.load('images/light3.png').convert_alpha()
        self.light_mask = pygame.transform.scale(self.light_mask, (600,1100))
        self.light_rect = self.light_mask.get_rect()
        
        self.camera = Camera(width, height)
        
        #define frame
        self.rectWidth = 110
        self.rectHeight = 100
        
        #define frame sequences
        self.left_states = [
            (0, 120, self.rectWidth, self.rectHeight),
            (115, 120, self.rectWidth, self.rectHeight),
            (230, 120, self.rectWidth, self.rectHeight),
            (345, 120, self.rectWidth, self.rectHeight),
            (460, 120, self.rectWidth, self.rectHeight),
            (575, 120, self.rectWidth, self.rectHeight),
            (690, 120, self.rectWidth, self.rectHeight),
            (805, 120, self.rectWidth, self.rectHeight)
            
        ]
        
        self.right_states = [
            (0, 340, self.rectWidth, self.rectHeight),
            (115, 340, self.rectWidth, self.rectHeight),
            (230, 340, self.rectWidth, self.rectHeight),
            (345, 340, self.rectWidth, self.rectHeight),
            (460, 340, self.rectWidth, self.rectHeight),
            (575, 340, self.rectWidth, self.rectHeight),
            (690, 340, self.rectWidth, self.rectHeight),
            (889, 340, self.rectWidth, self.rectHeight)
        ]
        
        self.front_states = [
            (0,240, self.rectWidth, self.rectHeight)
        ]
        
        #set initial frame and position
        self.frame = 0
        self.image = self.sheet.subsurface(pygame.Rect(self.front_states[self.frame]))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        
        #set inventory
        self.inventory = Inventory.Inventory()
       
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame >= len(frame_set):
            self.frame = 0
        
        return frame_set[self.frame]
           
    def clip(self, frame_set):
        clip_rect = pygame.Rect(self.get_frame(frame_set))
        self.sheet.set_clip(clip_rect)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
            
    def move(self, direction, speed):
        if direction == 'left':
            self.clip(self.left_states)
            self.position[0] -= speed
        elif direction == 'right':
            self.clip(self.right_states)
            self.position[0] += speed
        elif direction == 'stand':
            self.clip([self.front_states[0]])
             
        self.rect.topleft = self.position    
        self.camera.update(self)
        
        if self.position[0] <= 0:
            self.position[0] = 0
            
        if self.position[0] >= 900:
            self.position[0] = 900
            
    def draw_player(self, screen):
        # Draw glow and sprite on the screen
        screen.blit(self.image, self.rect)
            
    def render_fog(self, screen):
        self.fog.fill((20,20,20))
        self.light_rect.center = self.camera.apply(self).center
        self.fog.blit(self.light_mask, self.light_rect)
        screen.blit(self.fog, (0,0), special_flags=pygame.BLEND_MULT)