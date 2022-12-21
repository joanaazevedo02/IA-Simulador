import pygame as p
from Chess import ChessEngine

WIDTH= HEIGHT = 512
DIMENSION =8
SQ_SIZE = HEIGHT //DIMENSION
IMAGES={}

def LoadImages():
    pieces = ['zombie1', 'zombie2', 'margarida', 'peca1', 'peca2', 'bala', 'mota']
    for piece in pieces:
        IMAGES[piece]=p.tranform.scale(p.image.load("images/" +piece+".png"), (SQ_SIZE, SQ_SIZE))
        
def main():
    p.init()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)