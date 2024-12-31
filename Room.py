import pygame
import Item
import Timer

# Room class
class Room:
    def __init__(self, game_time):
        # Set screen dimensions for reference
        self.WIDTH = 1000
        self.HEIGHT = 600

        # Load and resize images for room objects
        self.wall_image = pygame.image.load("background_imgs/empty_basement.jpg")
        self.wall_image = pygame.transform.scale(self.wall_image, (self.WIDTH, self.HEIGHT))
        
        self.women_image = pygame.image.load("images/women.png")
        self.women_image = pygame.transform.scale(self.women_image, (130, 150))
        
        self.blood_image = pygame.image.load("images/blood_spatter.png")
        self.blood_image = pygame.transform.scale(self.blood_image, (150, 100))

        self.desk_image = pygame.image.load("images/desk.png")
        self.desk_image = pygame.transform.scale(self.desk_image, (200, 180))

        self.bookshelf_image = pygame.image.load("images/bookshelf.png")
        self.bookshelf_image = pygame.transform.scale(self.bookshelf_image, (220, 200))

        self.safe_image = pygame.image.load("images/safe.png")
        self.safe_image = pygame.transform.scale(self.safe_image, (210, 160))

        self.clock_image = pygame.image.load("images/clock.png")
        self.clock_image = pygame.transform.scale(self.clock_image, (40, 40))

        # Setup puzzles and items (creating item objects with positions)
        self.blood_spatter_item = Item.Item("Blood Spatter", self.blood_image, (250, 225), "Cipher puzzle", game_time)
        self.desk_item = Item.Item("Desk", self.desk_image, (250, 350), "Find drawer key", game_time)
        self.bookshelf_item = Item.Item("Bookshelf", self.bookshelf_image, (600, 375), "Find a book for the key", game_time)
        self.clock_item = Item.Item("Clock", self.clock_image, (485, 410), "Symbol code", game_time)

        # List of all interactive items in the room
        self.items = [self.blood_spatter_item, self.desk_item, self.bookshelf_item, self.clock_item]

    def update(self, screen, player, inventory, camera):
        # Draw the room background (walls, items, puzzles, etc.)
        screen.blit(self.wall_image, (0, 0))
        screen.blit(self.women_image, (600, 250))
        screen.blit(self.safe_image, (400,400))
        
        # Draw each puzzle/item in the room
        for item in self.items:
            item.draw_with_camera(screen, camera)
            item.interact(screen, player, inventory,)  # Handle interaction when player clicks
