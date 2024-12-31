# Items.py
import pygame
import math
import Popup


class Item:
    def __init__(self, name, image, position, description, game_time):
        self.name = name
        self.image = image
        self.position = position
        self.description = description
        self.rect = self.image.get_rect(topleft=self.position)
        self.state = "default"
        self.font = pygame.font.Font(None, 36)
        self.game_time = game_time
        
        # Pop-ups
        self.key_popup = None
        self.sticky_note_popup = None
        self.text_popup = None
        self.clock_popup = None
        self.keypad_popup = None
        
        self.clock_active = False
    
    def draw(self, screen):
        # Draw the item to the screen
        screen.blit(self.image, self.position)

    def draw_with_camera(self, screen, camera):
        # Draw the item adjusted by the camera position
        adjusted_rect = camera.apply_rect(self.rect)
        screen.blit(self.image, adjusted_rect)

    def interact(self, screen, player, inventory):
        # Handle interaction when player clicks on the item
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            if pygame.mouse.get_pressed()[0]:
                self.handle_interaction(screen, player, inventory)

    def handle_interaction(self, screen, player, inventory):
        # Define interaction based on item name and game state
        if self.name == "Bookshelf":
            if "Key" not in inventory.items:
                # Interaction to find the book
                inventory.add_item("Key")
                self.state = "book_found"
                
            # Show the key pop-up
            if self.key_popup is None:
                self.key_popup = Popup.Popup("images/Key.png", (375, 100), (300, 450), "Key Found!", self.game_time)
            self.key_popup.show()
        
        elif self.name == "Desk":
            if "Key" in inventory.items and "StickyNote" not in inventory.items:
                inventory.add_item("StickyNote")
                self.state = "drawer_opened"
                
                if self.sticky_note_popup is None:
                    self.sticky_note_popup = Popup.Popup("images/StickyNote.png", (300, 150), (350, 300), "A Note? A Clue?", self.game_time)
                self.sticky_note_popup.show()
                
            elif "Key" not in inventory.items:
                # If player doesn't have the key, inform them
                print("The desk is locked. You need a Drawer Key to open it.")
                
            elif "Key" in inventory.items and "StickyNote" in inventory.items:
                if self.sticky_note_popup is None:
                    self.sticky_note_popup = Popup.Popup("images/StickyNote.png", (300, 150), (350, 300), "A Note? A Clue?", self.game_time)
                self.sticky_note_popup.show()
        
        elif self.name == "Blood Spatter":
            if "StickyNote" in inventory.items and "EscapeCode" not in inventory.items:
                if self.text_popup is None:
                    self.text_popup = Popup.Popup("images/Cipher.png", (200, 200), (450, 200), "Zero between, a sum, all in time", self.game_time)
                self.text_popup.show()
                
                # Assign escape code based on decoded text or predefined
                inventory.add_item("CipherKey")
                self.state = "decoded"
                
            elif "CipherKey" in inventory.items:
                print("The cipher has already been decoded.")
        
        elif self.name == "Clock":
            if "SafeCode" not in inventory.items and "Key" in inventory.items and "StickyNote" in inventory.items and "CipherKey" in inventory.items:
                # Solve the clock puzzle to get safe code
                if self.clock_popup is None:
                    self.clock_popup = Popup.DigitalClockPuzzle(self.game_time, inventory)
                self.clock_popup.show()
                
                if self.clock_popup.solved:
                    # If the input matches the correct time, give the player the safe code
                    inventory.add_item("EscapeCode")
                    self.state = "code_solved"                        
            elif "Key" not in inventory.items and "StickyNote" not in inventory.items and "CipherKey" not in inventory.items:
                print("Cannot view clock yet.")
            elif "Key" in inventory.items and "StickyNote" not in inventory.items and "CipherKey" not in inventory.items:
                print("Cannot view clock yet.")
            elif "Key" in inventory.items and "StickyNote" in inventory.items and "CipherKey" not in inventory.items:
                print("Cannot view clock yet.")