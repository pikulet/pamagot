#from engine import PamagotEngine
from buttons import *
import pyxel

BUTTON_MAPPINGS = {
    pyxel.KEY_LEFT: BUTTON_A,
    pyxel.KEY_DOWN: BUTTON_B,
    pyxel.KEY_RIGHT: BUTTON_C
}

class Pamagot:

    def __init__(self):
        print("Pamagotchii :]")
        #self.engine = PamagotEngine()
        self.btns = ButtonManager()
        pyxel.init(80, 80, caption="Pamagotchii")
        pyxel.run(self.update, self.draw)

    def btns_check(self):
        pressed = False
        for key, btn in BUTTON_MAPPINGS.items():
            if pyxel.btnp(key):
                self.btns.press(btn)
                pressed = True
            elif pyxel.btnr(key):
                self.btns.release(btn)

        return pressed

    def update(self):
        x = False

        if self.btns_check():
            print(self.btns.pressed)
        #self.engine.press(self.btns.pressed)
        #self.engine.update()

    def draw(self):
        pyxel.cls(0)
        #self.engine.draw()

if __name__ == '__main__':
    Pamagot()