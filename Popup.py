import pygame
import Inventory

class Popup:
    def __init__(self, image_path, position, size, message, game_time):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=position)
        self.visible = False
        self.game_time = game_time
        
        self.message = message
        self.font = pygame.font.Font("fonts/font.ttf", 18)
        self.font_color = (255,255,255)
        

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self.hide()

    def draw(self, screen):
        if self.game_time.get_time_left() <= 0:
            self.hide()
        
        if self.visible:
            screen.blit(self.image, self.rect)
            
            text_surface = self.font.render(self.message, True, self.font_color)
            text_rect = text_surface.get_rect()
            screen.blit(text_surface, (self.rect.topleft[0] - 50, self.rect.topleft[1] - 50))
            
            text_surface2 = self.font.render("'c' to close", True, self.font_color)
            text_rect2 = text_surface2.get_rect()
            screen.blit(text_surface2, (self.rect.bottomleft[0] + 25, self.rect.bottomleft[1] + 25))
             

class DigitalClockPuzzle:
    def __init__(self, game_time, inventory, correct_time="6:07"):
        # The correct time to solve the puzzle (as a string "HH:MM")
        self.correct_time = correct_time
        self.solved = False

        # Set up font for displaying the clock and input
        self.font = pygame.font.Font("fonts/font.ttf", 18)
        self.input_box = pygame.Rect(375, 100, 250, 75)
        self.enter_box = pygame.Rect(450, 300, 100, 25)
        self.text = ''  # Text input for time
        self.visible = False
        self.color_inactive = (135, 18, 33)
        self.color_active = (214, 36, 59)
        self.color = self.color_inactive
        self.text_color = (255, 255, 255)
        self.inventory = inventory
        
        #game clock
        self.game_time = game_time
        
    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def draw(self, screen):
        if self.game_time.get_time_left() <= 0:
            self.hide()
        
        if self.visible:
            txt_surface = self.font.render(self.text, True, (255, 255, 255))
            txt_surface_2 = self.font.render("Enter a Time", True, (255, 255, 255))
            pygame.draw.rect(screen, self.color, self.input_box)
            screen.blit(txt_surface, (self.input_box.x+10, self.input_box.y+45))
            screen.blit(txt_surface_2, (self.input_box.x+10, self.input_box.y+10))

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.text == self.correct_time:
                        self.inventory.add_item("EscapeCode")
                        self.solved = True
                        self.visible = False
                elif event.key == pygame.K_BACKSPACE:  # Delete last character
                    self.text = self.text[:-1]
                elif event.unicode.isdigit() or event.unicode == ":":  # Add new character
                    if len(self.text) < 5:  # Limit to HH:MM format
                        self.text += event.unicode