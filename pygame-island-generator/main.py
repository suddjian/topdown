# Island Generator  ############
#
#
# Created by Christopher Breinholt      ##
# Breiny Games (c) 2011                 ##
# http://breinygames.blogspot.com/      ##
#
# To Use: Run the main.py file.         ##
# Press spacebar to generate a new      ##
# Island.                               ##
# Press z to decrement the frequency
# and a to increment.
#

import pygame
#from perlin_noise import *
from island_generator import IslandGenerator
from map_file import Map
from character import Character

FPS = 60

WIDTH, HEIGHT = 1024,768
TILE_SIZE = 4

noise_w = WIDTH / TILE_SIZE
noise_h = HEIGHT / TILE_SIZE
noise_f = 1.25
noise_o = 16

noise_increment = .5

def main():

    global noise_f

    pygame.init()
    pygame.display.set_caption("Perlin Noise Terrain Generator")

    resolution = (WIDTH, HEIGHT)

    clock = pygame.time.Clock()

    # screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    screen = pygame.display.set_mode(resolution)

    world = new_island()

    mainchar = Character(world=world)
    characters = {'main':mainchar}

    character_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
    character_image.fill((255,0,0))


    # IslandGenerator().generate_island(noise_w, noise_h, noise_f, noise_o)
    # is the function that generates the random "island" style map in the
    # form of a 2d array, map.Map() is a class that just stores that 2d array
    # and can hold other information about the map, such as type. That way if
    # I add another kind of map generator (dungeons?), I can use the same map
    # class to store them. It could also store multiple 2d arrays ("maps") like
    # a world would. So for a game you could have several 2d arrays all generated
    # from this and other generators so you can have forrests, mountains, island,
    # dungeons, etc all stored in a single "world".
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: running = False
                elif event.key == pygame.K_F11:
                    world.draw_minimap(True) # black and white
                elif event.key == pygame.K_F10:
                    world.draw_minimap()
                elif event.key == pygame.K_F9:
                    world.save()
                elif event.key == pygame.K_UP:
                    characters['main'].move(0,-1)
                elif event.key == pygame.K_DOWN:
                    characters['main'].move(0,1)
                elif event.key == pygame.K_LEFT:
                    characters['main'].move(-1,0)
                elif event.key == pygame.K_RIGHT:
                    characters['main'].move(1,0)
                elif event.key == pygame.K_SPACE:
                    world = new_island()
                elif event.key == pygame.K_z:
                    noise_f = noise_f - noise_increment
                    world = new_island()
                elif event.key == pygame.K_a:
                    noise_f = noise_f + noise_increment
                    world = new_island()

        screen.blit(world.minimap, (0, 0))
        screen.blit(character_image, (characters['main'].y*TILE_SIZE, characters['main'].x*TILE_SIZE))

        pygame.display.flip()

def new_island():
    print(noise_f)
    island = IslandGenerator().generate_island(noise_w, noise_h, noise_f, noise_o)
    world = Map('Island', island, TILE_SIZE)
    return world



if __name__ == "__main__":
    main()
    # cProfile.run("main()")
    pygame.quit()
