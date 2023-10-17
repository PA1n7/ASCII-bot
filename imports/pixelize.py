import pygame

def px_by_px(square:pygame.Rect, img:pygame.Surface):
    aver = 0
    pixel_count = square.width**2
    avg = [0, 0, 0]
    for x in range(square.width-1):
        for y in range(square.width-1):
            try:
                color = img.get_at((x+square.left, y+square.top))
            except IndexError:
                continue
            avg = [avg[i] + color[i] for i in range(len(avg))]
    return [i/pixel_count for i in avg]

def pixel(src:str,out:str , subdivisions=1):
    img = pygame.image.load(src)
    size = img.get_size()
    grid = []
    side = size[0]/subdivisions
    side = int(side)
    img = pygame.transform.scale(img, (size[0]-size[0]%subdivisions, size[1]-size[1]%side))
    for y in range(int(size[1]/side)):
        for x in range(subdivisions):
            grid.append(pygame.Rect(side*x, side*y, side, side))
    for square in grid:
        pygame.draw.rect(img, px_by_px(square, img), square)
    pygame.image.save(img, out)
