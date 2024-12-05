import math
import random
import pygame

class PlayerEntity:
    def __init__(self, position: pygame.Vector2, motion: pygame.Vector2):
        self.position: pygame.Vector2 = position
        self.motion: pygame.Vector2 = motion
        
    def update(self, delta_t):
        self.position += self.motion * delta_t
        
        x: float = 0
        y: float = 0
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y = -1
        elif keys[pygame.K_DOWN]:
            y = 1
        
        if keys[pygame.K_LEFT]:
            x = -1
        elif keys[pygame.K_RIGHT]:
            x = 1
        
        self.motion += pygame.Vector2(x * 0.01, y * 0.01)
        if x == 0:
            self.motion.x *= 0.925
        if y == 0:
            self.motion.y *= 0.925
        
        if self.position.x > pygame.display.get_window_size()[0]:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = pygame.display.get_window_size()[0]
            
        if self.position.y > pygame.display.get_window_size()[1]:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = pygame.display.get_window_size()[1]
    
    def show(self, surface: pygame.Surface, score):
        pygame.draw.rect(surface, (255, 255, 255), (*(self.position - pygame.Vector2(5, 5)), 10, 10))
        surface.blit(pygame.font.SysFont("The Bold Font", 20).render(str(score), False, (255, 255, 255)), self.position + pygame.Vector2(5, 5))    
        
class EnemyEntity:
    def __init__(self, position: pygame.Vector2, motion: pygame.Vector2):
        self.position: pygame.Vector2 = position
        self.motion: pygame.Vector2 = motion
        
    def update(self, delta_t):
        self.position += self.motion * delta_t
        self.motion *= 1.0001
        
        # Recycling
        if self.position.x > pygame.display.get_window_size()[0]:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = pygame.display.get_window_size()[0]
            
        if self.position.y > pygame.display.get_window_size()[1]:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = pygame.display.get_window_size()[1]
    
    def show(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (255, 0, 0), (*(self.position - pygame.Vector2(2.5, 2.5)), 5, 5))

def gen_1D_direction():
    if random.uniform(0, 1) < 0.5:
        return 1 
    else:
        return -1

def gen_enemy():
    return EnemyEntity(
        pygame.Vector2(random.randint(0, pygame.display.get_window_size()[0]), random.randint(0, pygame.display.get_window_size()[1])),
        pygame.Vector2(gen_1D_direction() * random.uniform(0.01, 0.1), gen_1D_direction() * random.uniform(0.01, 0.1))
    )