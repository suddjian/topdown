import pygame

class Map:

    def __init__(self, map_type, map_map,tile_size= 4):
        self.type = map_type
        self.map = map_map
        self.width = len(self.map[0])
        self.height = len(self.map)
        self.tile_size = tile_size
        self.waterline = 0

        self.minimap = pygame.Surface((self.width * self.tile_size,
                                       self.height * self.tile_size))
        self.draw_minimap()
        
        
    def save(self):
        with open("lastmap.txt", "w") as f:
            for y in range(0, self.height):
                print >>f, ",".join(["%s" % int(yy) for yy in self.map[y]])
        pygame.quit()
                    

    def get_waterline(self):

        values = []
        for y in range(0, self.height):
            for x in range(0, self.width):
                values.append(self.map[y][x])
        values.sort()
        waterline = values[int((len(values) - 1) * .45)]
        return waterline
    
    
    def draw_minimap(self, binary=False):
        
        self.waterline = self.get_waterline()    


        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.map[y][x] > 255.0:
                    self.map[y][x] = 255.0
                tile = int(self.map[y][x])
                
                if tile <= self.waterline:
                    self.map[y][x] = 0
                
                if binary:
                    if tile <= self.waterline+10:
                        color = (25, 25, 75)
                    else:
                        color = (255,255,255)
                else:
                    if tile <= self.waterline:
                        color = (25, 25, 75)
                    elif tile > self.waterline and tile <= self.waterline + 10:
                        color = (tile + 80, tile + 80, 100)
                    elif tile > self.waterline + 10 and tile <= self.waterline + 40:
                        color = (0, 255 - tile, 0)
                    elif tile > self.waterline + 40 and tile <= 190:
                        color = (0, 255 - tile, 0)
                    elif tile > 190:
                        color = (255 - tile, 255 - tile, 255 - tile)

#                color = (tile, tile, tile)

                image = pygame.Surface((self.tile_size, self.tile_size))
                image.fill(color)
                self.minimap.blit(image, (x * self.tile_size,
                                          y * self.tile_size))

                
                
if __name__ == "__main__":
    import main
    main.main()
    # cProfile.run("main()")
    pygame.quit()