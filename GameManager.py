# GameManager.py
import pygame
from pygame import mixer
import sys
import Room
import Player
import Inventory
import Timer
import Button

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Your Life or Mine")

# Instantiate features
player = Player.Character((175, 475), WIDTH, HEIGHT)
inventory = Inventory.Inventory()
game_timer = Timer.Timer(start_time=10*60)  # 10 minutes in seconds
room = Room.Room(game_timer)
bg = pygame.image.load("images/main_menu_bg.png")
bg_sized = pygame.transform.scale(bg, (WIDTH, HEIGHT))

#Background music
mixer.music.load("music/background_music.wav")
mixer.music.play(-1)

# Game variables
clock_obj = pygame.time.Clock()
running = True
game_over = False

# Load images for items in Room (Replace with actual paths or handle missing images)
def load_image(path, size=None):
    try:
        image = pygame.image.load(path).convert_alpha()
        if size:
            image = pygame.transform.scale(image, size)
    except pygame.error:
        print(f"Unable to load image at path: {path}. Using placeholder.")
        image = pygame.Surface((50, 50), pygame.SRCALPHA)
        image.fill((255, 0, 255, 128))  # Semi-transparent magenta
    return image

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("fonts/font.ttf", size)
    
def reset_game():
    global player, inventory, game_timer, room
    # Reset all game components
    screen.fill((0,0,0))
    game_timer = Timer.Timer(start_time=10*60)  # Reset timer
    player = Player.Character((175, 475), WIDTH, HEIGHT)  # Reset player position
    inventory.reset()  # Clear inventory
    room = Room.Room(game_timer)  # Reinitialize room and items


def ending_scene(screen):    
    # Load background and message
    font = pygame.font.Font("fonts/font.ttf", 50)
    message = font.render("You Escaped!", True, (0, 255, 0))  # Green text
    message_rect = message.get_rect(center=(screen.get_width() // 2, 150))

    # Display message
    screen.fill((0, 0, 0))  # Black background
    screen.blit(message, message_rect)
    pygame.display.update()

    # Wait a moment before playing the video
    pygame.time.wait(2000)  # 2 seconds

    # Add "Return to Main Menu" button
    font_small = pygame.font.Font("fonts/font.ttf", 30)
    menu_message = font_small.render("Press M to return to Main Menu", True, (255, 255, 255))
    menu_rect = menu_message.get_rect(center=(screen.get_width() // 2, screen.get_height() - 100))
    screen.blit(menu_message, menu_rect)
    pygame.display.update()

    # Wait for input to return to the main menu
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                waiting = False
                
def play():
    global game_timer
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
    
        # Handle events
        events = pygame.event.get()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                return
                
        game_timer.update()

        # Player controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.move('left', 5)
        elif keys[pygame.K_d]:
            player.move('right', 5)
        else:
            player.move('stand', 0)

        # Update camera based on player
        player.camera.update(player)

        # Update and draw room with camera
        room.update(screen, player, inventory, player.camera)
        
        # Render light mask and draw player
        player.render_fog(screen)  # Draws light mask around the player
        player.draw_player(screen)  # Draw player sprite
        
        # Interact with room items (bookshelf, clock, etc.)
        for item in room.items:  # Assuming room has a list of items
            item.interact(screen, player, inventory)
            
            # Show pop-ups based on interaction with items
            if item.key_popup:  # If there's a key pop-up for the bookshelf
                item.key_popup.handle_event(pygame.event.get())
                item.key_popup.draw(screen)
                
            if item.sticky_note_popup:  # If there's a key pop-up for the bookshelf
                item.sticky_note_popup.handle_event(pygame.event.get())
                item.sticky_note_popup.draw(screen)
            
            if item.text_popup:  # If there's a text pop-up for the blood spatter
                item.text_popup.handle_event(pygame.event.get())
                item.text_popup.draw(screen)
            
            if item.clock_popup:  # If there's a clock pop-up
                item.clock_popup.handle_event(events)
                item.clock_popup.draw(screen)
        
        # Draw
        inventory.draw(screen, WIDTH)
        game_timer.draw(screen)
        
        PLAY_BACK = Button.Button(image=None, pos=(85, 18), 
                            text_input="Menu", font=get_font(25), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        if pygame.mouse.get_pressed()[0]:  # Check for mouse click
            if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                return
                
                
        # If the timer reaches 0, show "You Lost" and return to the main menu
        if game_timer.get_time_left() <= 0:
            # Display "You Lost" message
            lost_text = get_font(50).render("You Lost!", True, (255, 0, 0))  # Red color
            text_rect = lost_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(lost_text, text_rect)
            
            # Update the screen and wait for a short time to show the message
            pygame.display.update()
            pygame.time.wait(2000)  # Wait for 2 seconds to let the player see the message
            
            #Reset everything
            game_timer = Timer.Timer(start_time=10*60)
            inventory.reset()
            return
            
        if inventory.has_item("EscapeCode"):  # Replace with your condition for completing the game
            ending_scene(screen)
            reset_game()
            return

        # Update display
        pygame.display.update()
        
        # Control frame rate
        clock_obj.tick(60)

def main_menu():    
    while True:
        screen.blit(bg_sized, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(55).render("Your Life or Mine", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 75))

        PLAY_BUTTON = Button.Button(image=pygame.image.load("images/Play Rect.png"), pos=(500, 275), 
                            text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button.Button(image=pygame.image.load("images/Quit Rect.png"), pos=(500, 450), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False
                    sys.exit()
                    return

        pygame.display.update()

# Main game loop
while running:
    screen.fill((0, 0, 0))  # Clear screen (black background)
    main_menu()
    pygame.display.update()

pygame.quit()  # Quit Pygame once the loop ends
