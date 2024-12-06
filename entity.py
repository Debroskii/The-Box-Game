import math
import random
import pygame

import menu

class PlayerEntity:
    def __init__(self, position: pygame.Vector2, motion: pygame.Vector2):
        self.position: pygame.Vector2 = position
        self.motion: pygame.Vector2 = motion
        self.particles = [
            self.position + pygame.Vector2(random.randint(-4, 4), random.randint(-4, 4)), 
            self.position + pygame.Vector2(random.randint(-4, 4), random.randint(-4, 4))
        ]
        
    def update(self, delta_t):
        self.position += self.motion * delta_t
        
        self.particles.append(self.position + pygame.Vector2(random.randint(-4, 4), random.randint(-4, 4)))
        self.particles.append(self.position + pygame.Vector2(random.randint(-4, 4), random.randint(-4, 4)))
        self.particles.append(self.position + pygame.Vector2(random.randint(-4, 4), random.randint(-4, 4)))
        
        if len(self.particles) / 3 > 10:
            self.particles.pop(2)
            self.particles.pop(1)
            self.particles.pop(0)
        
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
        score = pygame.font.Font(menu.resource_path("8-bit Arcade In.ttf"), 650).render(str(score), False, (8, 8, 8))
        surface.blit(score, score.get_rect(center=(pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 - 75)))
        for particle in self.particles:
            color = (self.particles.index(particle) * 8) ** 0.99
            print(self.particles.index(particle))
            size = random.randint(2, 5)
            pygame.draw.rect(surface, (color, color, color), (*(particle - pygame.Vector2(size / 2, size / 2)), size, size))
        pygame.draw.rect(surface, (255, 255, 255), (*(self.position - pygame.Vector2(5, 5)), 10, 10))
        
class EnemyEntity:
    def __init__(self, position: pygame.Vector2, motion: pygame.Vector2):
        self.position: pygame.Vector2 = position
        self.motion: pygame.Vector2 = motion
        
    def update(self, delta_t, difficulty):
        self.position += self.motion * delta_t
        
        if difficulty == 0:
            self.motion *= 1.0001
        elif difficulty == 1:
            self.motion *= 1.00035
        elif difficulty == 2:
            self.motion *= 1.00065
        
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