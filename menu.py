from enum import Enum

import pygame

class Menus(Enum):
    GAME_OVER = 0
    GAME_START = 1

class Menu:
    def show(surface, menu: Menus, score, difficulty):
        if menu == Menus.GAME_OVER:
            GameOverMenu.draw(surface, score)
        if menu == Menus.GAME_START:
            GameStartMenu.draw(surface, difficulty)

class GameOverMenu:
    def draw(surface, score):
        game_over = pygame.font.Font("font/8-bit Arcade Out.ttf", 150).render("GAME OVER", False, (255, 0, 0))
        surface.blit(game_over, game_over.get_rect(center=(pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 - 35)))
        
        score = pygame.font.Font("font/8-bit Arcade In.ttf", 50).render("Score " + str(score), False, (255, 255, 255))
        surface.blit(score, score.get_rect(center=(pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 + 35)))
        
class GameStartMenu: 
    def draw(surface, difficulty):
        pass