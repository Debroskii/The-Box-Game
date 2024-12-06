import pygame

import entity
from menu import Menus, Menu
import menu

# PyGame Initialization
pygame.init()
pygame.display.set_caption("The Box Game")
pygame.display.set_icon(pygame.image.load(menu.resource_path('box_round.png')))

# Window
window: pygame.Surface = pygame.display.set_mode((900, 900))
running: bool = True
delta_t = 0

# Game
game_time: pygame.time.Clock = pygame.time.Clock()
game_score: int = 0
game_speed_modifier = 1
game_started = False
player_alive = True
difficulty = 1

# Test Instances
test_player = entity.PlayerEntity(pygame.Vector2(450, 450), pygame.Vector2(0, 0))
enemies = [entity.gen_enemy()]

# Main Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not game_started or not player_alive:
                if event.key == pygame.K_1:
                    difficulty = 0
                elif event.key == pygame.K_2:
                    difficulty = 1
                elif event.key == pygame.K_3:
                    difficulty = 2
                elif event.key == pygame.K_RETURN:
                    if not player_alive:
                        test_player = entity.PlayerEntity(pygame.Vector2(450, 450), pygame.Vector2(0, 0))
                        enemies = [entity.gen_enemy()]
                        game_score = 0
                        game_speed_modifier = 0
                        player_alive = True
                    game_started = True
            
    game_speed_modifier *= 1.0001
    game_score = len(enemies)    
    
    window.fill((0, 0, 0))
    
    if player_alive and game_started:
        test_player.update(delta_t)
    test_player.show(window, game_score)
        
    for enemy in enemies:
        if player_alive and game_started:
            enemy.update(delta_t, difficulty)
        enemy.show(window)
        
        if (enemy.position - test_player.position).magnitude() < 10:
            player_alive = False
                
    if pygame.time.get_ticks() % round(240 / (difficulty + 1)) == 0 and player_alive and game_started:
        enemies.append(entity.gen_enemy())
        
    if not player_alive and game_started:
        Menu.show(window, Menus.GAME_OVER, game_score, difficulty)
        
    if not game_started:
        Menu.show(window, Menus.GAME_START, game_score, difficulty)
        
    pygame.display.flip()
    delta_t = game_time.tick(60)
    
# PyGame Termination
pygame.quit()