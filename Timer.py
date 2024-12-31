import pygame
import time

class Timer:
    def __init__(self, start_time):  # Default is 10 minutes (in seconds)
        self.start_time = start_time;
        self.remaining_time = start_time  # Remaining time in seconds
        self.font = pygame.font.Font(None, 56)  # Font for the timer (None uses the default font)
        self.color = (255, 0, 0)  # White text color
        self.last_update = time.time()  # Track the last time the timer was updated

    def update(self):
        current_time = time.time()
        # Update the timer every second
        if current_time - self.last_update >= 1:
            self.remaining_time -= 1
            self.last_update = current_time
            if self.remaining_time <= 0:
                self.remaining_time = 0  # Stop at 0
                
    def get_time_left(self):
        # Return the remaining time in seconds
        return self.remaining_time

    def draw(self, screen):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        time_text = f"{minutes:02}:{seconds:02}"  # Format as MM:SS
        text_surface = self.font.render(time_text, True, self.color)
        text_rect = text_surface.get_rect(topleft=(40, 40))  # Position at top-right corner
        screen.blit(text_surface, text_rect)

    def reset(self):
        self.remaining_time = self.start_time  # Reset to initial time