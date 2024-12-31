import pygame

class Inventory:
    def __init__(self):
        self.items = []  # List to store item names
        self.clues = []  # List to store clues
    
    def add_item(self, item_name):
        if item_name not in self.items:
            self.items.append(item_name)
            print(f"Added '{item_name}' to inventory.")
    
    def add_clue(self, clue):
        if clue not in self.clues:
            self.clues.append(clue)
            print(f"Clue added: {clue}")
    
    def has_item(self, item_name):
        return item_name in self.items
        
    def reset(self):
        self.items.clear()
        
    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("fonts/font.ttf", size)
    
    def draw(self, screen, screen_width):        
        # Draw the inventory on the screen (simple text list)
        font = self.get_font(12)
        y_offset = 10
        inventory_text = "Inventory:"
        text_surface = font.render(inventory_text, True, (255, 255, 255))
        screen.blit(text_surface, (screen_width - 150, y_offset))
        y_offset += 25
        for item in self.items:
            item_text = font.render(f"- {item}", True, (255, 255, 255))
            screen.blit(item_text, (screen_width - 200, y_offset))
            y_offset += 20
