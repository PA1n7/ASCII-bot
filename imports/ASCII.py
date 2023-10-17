import pygame, os, json
from pixelize import pixel

color_equivalence = json.loads(open("color_equivalence.json", "r", encoding="UTF-8").read())

def convert_to_ascii(source:pygame.Surface, out_file:str):
    out = ""
    size = source.get_size()
    stretch = 2
    for y in range(size[1]):
        for x in range(size[0]):
            color=source.get_at((x, y))[0]
            for k, v in color_equivalence.items():
                if color>int(k):
                    out+=v*stretch
                    break
        out+="\n"
    print(out)
    open(out_file, "w", encoding="UTF-8").write(out)
                
def desaturate(source:pygame.Surface, dest:pygame.Surface):
    size = source.get_size()
    for y in range(size[1]):
        for x in range(size[0]):
            color = source.get_at((x, y))
            avg = sum(color)/len(color)
            pygame.draw.rect(dest, (avg, avg, avg), pygame.Rect(x, y, 1, 1))

def ascii(img_file:str, out_file:str, size:int, debug=False):
    pixel(img_file, "temp.png", size)
    pixelized = pygame.image.load("temp.png")
    size = (size, int((pixelized.get_size()[1]*size)/pixelized.get_size()[0]))
    pixelized = pygame.transform.scale(pixelized, size)
    desaturate(pixelized, pixelized)
    if debug: pygame.image.save(pixelized, "desat.png")
    convert_to_ascii(pixelized, out_file)
    if not debug: os.remove("temp.png")