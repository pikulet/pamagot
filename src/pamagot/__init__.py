import logging
import pyxel

from pamagot.engine import PamagotEngine
from pamagot.buttons import *

BUTTON_MAPPINGS = {
    pyxel.KEY_LEFT: BUTTON_A,
    pyxel.KEY_DOWN: BUTTON_B,
    pyxel.KEY_RIGHT: BUTTON_C
}

class Pamagot:

    def __init__(self):
        logging.info("Welcome to Pamagotchii :]")
        self.engine = PamagotEngine()
        pyxel.init(50, 50, caption="Pamagotchii", palette=[0x000000, 0x1D2B53, 0x7E2553, 0x008751, 0xAB5236, 0x5F574F, 0xC2C3C7, 0xFFF1E8, 0xFF004D, 0xFFA300, 0xFFEC27, 0x00E436, 0x29ADFF, 0x83769C, 0xFF77A8, 0xFFCCAA])
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