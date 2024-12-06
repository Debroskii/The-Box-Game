from enum import Enum
import os
import sys

import pygame

class Menus(Enum):
    GAME_OVER = 0
    GAME_START = 1

class Menu:
    def show(surface, menu: Menus, score, difficulty):
        if menu == Menus.GAME_OVER:
            GameOverMenu.draw(surface, score)
            DifficultyMenu.draw(surface, difficulty)
        if menu == Menus.GAME_START:
            GameStartMenu.draw(surface)
            DifficultyMenu.draw(surface, difficulty)

class GameOverMenu:
    def draw(surface, score):
        backdrop = pygame.Surface((900, 900), pygame.SRCALPHA)
        pygame.draw.rect(backdrop, (0, 0, 0, 155), (0, 0, 900, 900))
        surface.blit(backdrop, (0, 0))
        
        game_over = pygame.font.Font(resource_path("8-bit Arcade Out.ttf"), 150).render("GAME OVER", False, (255, 0, 0))
        surface.blit(game_over, game_over.get_rect(center=(pygame.display.get_window_size()[0] / 2, 300)))
        
        score = pygame.font.Font(resource_path("8-bit Arcade In.ttf"), 50).render("Score " + str(score), False, (255, 255, 255))
        surface.blit(score, score.get_rect(center=(pygame.display.get_window_size()[0] / 2, 375)))
        
        cta = pygame.font.Font(resource_path("8-bit Arcade In.ttf"), 65).render("Press ENTER to restart", False, (255, 0, 0))
        surface.blit(cta, cta.get_rect(center=(pygame.display.get_window_size()[0] / 2, 600)))
    
class GameStartMenu: 
    def draw(surface):
        backdrop = pygame.Surface((900, 900), pygame.SRCALPHA)
        pygame.draw.rect(backdrop, (0, 0, 0, 205), (0, 0, 900, 900))
        surface.blit(backdrop, (0, 0))
        
        title_in = pygame.font.Font(resource_path("8-bit Arcade In.ttf"), 135).render("THE BOX GAME", False, (255, 255, 255))
        surface.blit(title_in, title_in.get_rect(center=(pygame.display.get_window_size()[0] / 2, 300)))
        
        description = pygame.font.Font(resource_path("8-bit Arcade In.ttf"), 40).render("Avoid the red boxes", False, (205, 205, 205))
        surface.blit(description, description.get_rect(center=(pygame.display.get_window_size()[0] / 2, 350)))
        
        cta = pygame.font.Font(resource_path("8-bit Arcade In.ttf"), 65).render("Press ENTER to Start", False, (255, 0, 0))
        surface.blit(cta, cta.get_rect(center=(pygame.display.get_window_size()[0] / 2, 600)))
        
class DifficultyMenu:
    def draw(surface, difficulty):
        easy = pygame.font.Font(resource_path("8-bit Arcade In.ttf"), 32).render("1 Easy", False, (255, 255, 255))
        surface.blit(easy, easy.get_rect(midleft=(30, 830)))
        
        normal = pygame.font.Font(resource_path(resource_path("8-bit Arcade In.ttf")), 32).render("2 Normal", False, (255, 255, 255))
        surface.blit(normal, normal.get_rect(midleft=(30, 855)))
        
        hard = pygame.font.Font(resource_path("8-bit Arcade In.ttf"), 32).render("3 Hard", False, (255, 255, 255))
        surface.blit(hard, hard.get_rect(midleft=(30, 880)))
        
        if difficulty == 0:
            pygame.draw.rect(surface, (255, 255, 255), (17.5, 832.5, 5, 5))
        
        if difficulty == 1:
            pygame.draw.rect(surface, (255, 255, 255), (17.5, 857.5, 5, 5))
            
        if difficulty == 2:
            pygame.draw.rect(surface, (255, 255, 255), (17.5, 882.5, 5, 5))
            
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)