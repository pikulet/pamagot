import logging
import pyxel

from engine.engine import PamagotEngine
from engine.buttons import *

BUTTON_MAPPINGS = {
    pyxel.KEY_LEFT: BUTTON_A,
    pyxel.KEY_DOWN: BUTTON_B,
    pyxel.KEY_RIGHT: BUTTON_C
}

class Pamagot:

    def __init__(self):
        logging.info("Welcome to Pamagotchii :]")
        self.engine = PamagotEngine()
        pyxel.init(40, 40, caption="Pamagotchii")
        pyxel.run(self.update, self.draw)

    def update(self):
        any_pressed = False
        to_press = [False] * 3
        for key, btn in BUTTON_MAPPINGS.items():
            if pyxel.btnp(key):
                to_press[btn] = True
                any_pressed = True

        if any_pressed:
            print(to_press)

    def draw(self):
        pyxel.cls(0)
        #self.engine.draw()