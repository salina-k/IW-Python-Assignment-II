# Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.

import pygame as pg

class Mario:
    def __init__(self, name, posx, posy, lives, height, width):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.lives = lives
        self.iskilled = False
        self.direc = "right"
        self.height = height
        self.width = width

    def left_move(self, steps):
        self.posx -= steps

    def right_move(self, steps):
        self.posx += steps

    def up_move(self, steps):
        self.posy -= steps

    def down_move(self, steps):
        self.posy += steps

    def load_sprites(self):
        self.sprite = [
            # 0 Small, stay
            pg.image.load('images/Mario/mario.png'),
            # 1 Small, move 0
            pg.image.load('images/Mario/mario_move0.png'),
            # 7 Small, stop
            pg.image.load('images/Mario/mario_st.png')]



