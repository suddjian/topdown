import random

class Character():
    def __init__(self, x=-1, y=-1, world=None):
        self.world = world
        
        if x == -1 or y == -1:
            randx = 0
            randy = 0
            while True:
                randx = random.randrange(1, world.width)
                randy = random.randrange(1, world.height)
                if world.map[randy][randx] > world.get_waterline():
                    break

            self.x = randx
            self.y = randy
                  
                  
    def move(self, dir_y, dir_x):
        nextx = self.x + dir_x
        nexty = self.y + dir_y
        if self.x >= 1 and self.y >= 1 and \
         self.x <= self.world.width and self.y <= self.world.height and \
         self.world.map[nextx][nexty] > self.world.get_waterline():
            self.x = nextx
            self.y = nexty

                            
                            


            
            
if __name__ == "__main__":
    import main, pygame
    main.main()
    # cProfile.run("main()")
    pygame.quit()